import cern.japc.core
import cern.japc.core.spi.provider
import cern.japc.core.spi.transaction
import cern.japc.core.transaction
import cern.japc.value
import typing



class AcquiredParameterValueAdapter:
    """
    Java class 'cern.japc.core.spi.adaptation.AcquiredParameterValueAdapter'
    
    """
    def adaptValueReceived(self, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> cern.japc.core.AcquiredParameterValue: ...

class ConstantParameter(cern.japc.core.spi.transaction.AbstractTransactionalParameter):
    """
    Java class 'cern.japc.core.spi.adaptation.ConstantParameter'
    
        Extends:
            cern.japc.core.spi.transaction.AbstractTransactionalParameter
    
      Constructors:
        * ConstantParameter(java.lang.String, cern.japc.value.ParameterValue)
    
    """
    def __init__(self, string: str, parameterValue: cern.japc.value.ParameterValue): ...
    @typing.overload
    def setParameterDescriptor(self, parameterDescriptor: cern.japc.core.ParameterDescriptor, descriptorProvider: cern.japc.core.spi.provider.DescriptorProvider) -> None: ...
    @typing.overload
    def setParameterDescriptor(self, parameterDescriptor: cern.japc.core.ParameterDescriptor) -> None: ...
    @typing.overload
    def setValueDescriptor(self, valueDescriptor: cern.japc.value.ValueDescriptor, descriptorProvider: cern.japc.core.spi.provider.DescriptorProvider) -> None: ...
    @typing.overload
    def setValueDescriptor(self, valueDescriptor: cern.japc.value.ValueDescriptor) -> None: ...

class ParameterValueSentAdapter:
    """
    Java class 'cern.japc.core.spi.adaptation.ParameterValueSentAdapter'
    
    """
    def adaptValueSent(self, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.value.ParameterValue: ...

class ViewParameter(cern.japc.core.spi.transaction.TransactionalParameterDecorator):
    """
    Java class 'cern.japc.core.spi.adaptation.ViewParameter'
    
        Extends:
            cern.japc.core.spi.transaction.TransactionalParameterDecorator
    
      Constructors:
        * ViewParameter(java.lang.String, cern.japc.core.transaction.TransactionalParameter, cern.japc.core.spi.adaptation.AcquiredParameterValueAdapter)
    
    """
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
    Java class 'cern.japc.core.spi.adaptation.VirtualParameterUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * VirtualParameterUtil()
    
    """
    def __init__(self): ...
    @staticmethod
    def createAdapterParameter(string: str, string2: str, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, class_: typing.Type, transactionalParameter2: cern.japc.core.transaction.TransactionalParameter, class2: typing.Type) -> 'AdapterParameter': ...
    @staticmethod
    def createAdapterParameterWithAdapterInstances(string: str, string2: str, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, acquiredParameterValueAdapter: AcquiredParameterValueAdapter, transactionalParameter2: cern.japc.core.transaction.TransactionalParameter, parameterValueSentAdapter: ParameterValueSentAdapter) -> 'AdapterParameter': ...
    @staticmethod
    def createInstance(class_: typing.Type, string: str) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def createViewParameter(string: str, string2: str, transactionalParameter: cern.japc.core.transaction.TransactionalParameter) -> ViewParameter: ...
    @typing.overload
    @staticmethod
    def createViewParameter(string: str, string2: str, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, acquiredParameterValueAdapter: AcquiredParameterValueAdapter) -> ViewParameter: ...
    @typing.overload
    @staticmethod
    def createViewParameter(string: str, string2: str, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, class_: typing.Type) -> ViewParameter: ...

class AbstractAcquiredParameterValueAdapter(AcquiredParameterValueAdapter):
    """
    Java class 'cern.japc.core.spi.adaptation.AbstractAcquiredParameterValueAdapter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.spi.adaptation.AcquiredParameterValueAdapter
    
      Constructors:
        * AbstractAcquiredParameterValueAdapter(java.lang.String)
    
    """
    def __init__(self, string: str): ...
    def adaptValueReceived(self, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> cern.japc.core.AcquiredParameterValue: ...

class AdapterParameter(ViewParameter):
    """
    Java class 'cern.japc.core.spi.adaptation.AdapterParameter'
    
        Extends:
            cern.japc.core.spi.adaptation.ViewParameter
    
      Constructors:
        * AdapterParameter(java.lang.String, cern.japc.core.transaction.TransactionalParameter, cern.japc.core.spi.adaptation.AcquiredParameterValueAdapter, cern.japc.core.transaction.TransactionalParameter, cern.japc.core.spi.adaptation.ParameterValueSentAdapter)
    
    """
    def __init__(self, string: str, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, acquiredParameterValueAdapter: AcquiredParameterValueAdapter, transactionalParameter2: cern.japc.core.transaction.TransactionalParameter, parameterValueSentAdapter: ParameterValueSentAdapter): ...
    def prepareValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, compositeTransaction: cern.japc.core.transaction.CompositeTransaction) -> None: ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue) -> None: ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...

class FieldFilteringParameterAdapter(AdapterParameter):
    """
    Java class 'cern.japc.core.spi.adaptation.FieldFilteringParameterAdapter'
    
        Extends:
            cern.japc.core.spi.adaptation.AdapterParameter
    
      Constructors:
        * FieldFilteringParameterAdapter(cern.japc.core.transaction.TransactionalParameter, java.lang.String, java.lang.String)
    
    """
    def __init__(self, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, string: str, string2: str): ...
    def getParameterDescriptor(self) -> cern.japc.core.ParameterDescriptor: ...
    def getValueDescriptor(self) -> cern.japc.value.ValueDescriptor: ...

class IdentityValueAdapter(AbstractAcquiredParameterValueAdapter, ParameterValueSentAdapter):
    """
    Java class 'cern.japc.core.spi.adaptation.IdentityValueAdapter'
    
        Extends:
            cern.japc.core.spi.adaptation.AbstractAcquiredParameterValueAdapter
    
        Interfaces:
            cern.japc.core.spi.adaptation.ParameterValueSentAdapter
    
      Constructors:
        * IdentityValueAdapter(java.lang.String)
    
    """
    def __init__(self, string: str): ...
    def adaptValueSent(self, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.value.ParameterValue: ...


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
