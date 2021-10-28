import cern.japc.core
import cern.japc.core.spi
import cern.japc.core.transaction
import cern.japc.value
import typing



class AbstractTransaction(cern.japc.core.transaction.Transaction):
    """
    Java class 'cern.japc.core.spi.transaction.AbstractTransaction'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.transaction.Transaction
    
    """
    def abort(self) -> None: ...
    def commit(self) -> None: ...
    def commitAndWait(self) -> None: ...
    def getState(self) -> cern.japc.core.transaction.Transaction.State: ...
    def hasFailed(self) -> bool: ...
    def isReady(self) -> bool: ...
    def registerTransactionStateListener(self, transactionStateListener: cern.japc.core.transaction.TransactionStateListener) -> None: ...
    def unregisterTransactionStateListener(self) -> None: ...

class AbstractTransactionalParameter(cern.japc.core.spi.AbstractParameter, cern.japc.core.transaction.TransactionalParameter):
    """
    Java class 'cern.japc.core.spi.transaction.AbstractTransactionalParameter'
    
        Extends:
            cern.japc.core.spi.AbstractParameter
    
        Interfaces:
            cern.japc.core.transaction.TransactionalParameter
    
      Constructors:
        * AbstractTransactionalParameter(java.lang.String)
    
    """
    def __init__(self, string: str): ...
    def prepareValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, compositeTransaction: cern.japc.core.transaction.CompositeTransaction) -> None: ...

class HardwareAccessTask:
    """
    Java class 'cern.japc.core.spi.transaction.HardwareAccessTask'
    
    """
    def performTask(self) -> None: ...

class TransactionalParameterDecorator(cern.japc.core.spi.ParameterDecorator, cern.japc.core.transaction.TransactionalParameter):
    """
    Java class 'cern.japc.core.spi.transaction.TransactionalParameterDecorator'
    
        Extends:
            cern.japc.core.spi.ParameterDecorator
    
        Interfaces:
            cern.japc.core.transaction.TransactionalParameter
    
      Constructors:
        * TransactionalParameterDecorator(cern.japc.core.transaction.TransactionalParameter)
    
    """
    def __init__(self, transactionalParameter: cern.japc.core.transaction.TransactionalParameter): ...
    def prepareValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, compositeTransaction: cern.japc.core.transaction.CompositeTransaction) -> None: ...

class CompositeTransactionImpl(AbstractTransaction, cern.japc.core.transaction.CompositeTransaction):
    """
    Java class 'cern.japc.core.spi.transaction.CompositeTransactionImpl'
    
        Extends:
            cern.japc.core.spi.transaction.AbstractTransaction
    
        Interfaces:
            cern.japc.core.transaction.CompositeTransaction
    
      Constructors:
        * CompositeTransactionImpl()
    
    """
    def __init__(self): ...
    def add(self, object: typing.Any, transaction: cern.japc.core.transaction.Transaction) -> bool: ...
    def get(self, object: typing.Any) -> cern.japc.core.transaction.Transaction: ...
    def getPendingValueCount(self) -> int: ...

class SequentialTransaction(AbstractTransaction):
    """
    Java class 'cern.japc.core.spi.transaction.SequentialTransaction'
    
        Extends:
            cern.japc.core.spi.transaction.AbstractTransaction
    
    """
    def addSetValueTask(self, hardwareAccessTask: HardwareAccessTask) -> None: ...
    def getPendingValueCount(self) -> int: ...

class TransactionalParameterSupport(AbstractTransactionalParameter):
    """
    Java class 'cern.japc.core.spi.transaction.TransactionalParameterSupport'
    
        Extends:
            cern.japc.core.spi.transaction.AbstractTransactionalParameter
    
      Constructors:
        * TransactionalParameterSupport(java.lang.String)
    
    """
    def __init__(self, string: str): ...

class AsynchronousParameterSupport(TransactionalParameterSupport):
    """
    Java class 'cern.japc.core.spi.transaction.AsynchronousParameterSupport'
    
        Extends:
            cern.japc.core.spi.transaction.TransactionalParameterSupport
    
      Constructors:
        * AsynchronousParameterSupport(java.lang.String)
    
      Attributes:
        DEFAULT_TIMEOUT (long): static field
    
    """
    DEFAULT_TIMEOUT: typing.ClassVar[int] = ...
    def __init__(self, string: str): ...

class SynchronousParameterSupport(TransactionalParameterSupport):
    """
    Java class 'cern.japc.core.spi.transaction.SynchronousParameterSupport'
    
        Extends:
            cern.japc.core.spi.transaction.TransactionalParameterSupport
    
      Constructors:
        * SynchronousParameterSupport(java.lang.String)
    
      Attributes:
        SYSPROP_MAXTHREADS (java.lang.String): final static field
    
    """
    SYSPROP_MAXTHREADS: typing.ClassVar[str] = ...
    def __init__(self, string: str): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.transaction")``.

    AbstractTransaction: typing.Type[AbstractTransaction]
    AbstractTransactionalParameter: typing.Type[AbstractTransactionalParameter]
    AsynchronousParameterSupport: typing.Type[AsynchronousParameterSupport]
    CompositeTransactionImpl: typing.Type[CompositeTransactionImpl]
    HardwareAccessTask: typing.Type[HardwareAccessTask]
    SequentialTransaction: typing.Type[SequentialTransaction]
    SynchronousParameterSupport: typing.Type[SynchronousParameterSupport]
    TransactionalParameterDecorator: typing.Type[TransactionalParameterDecorator]
    TransactionalParameterSupport: typing.Type[TransactionalParameterSupport]
