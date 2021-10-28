import cern.japc.core
import cern.japc.value
import java.io
import java.lang
import typing



class Transaction:
    """
    Java class 'cern.japc.core.transaction.Transaction'
    
      Attributes:
        IDLE (cern.japc.core.transaction.Transaction$State): final static field
        READY (cern.japc.core.transaction.Transaction$State): final static field
        SENDING (cern.japc.core.transaction.Transaction$State): final static field
        FAILED (cern.japc.core.transaction.Transaction$State): final static field
        ABORTED (cern.japc.core.transaction.Transaction$State): final static field
        COMMITTED (cern.japc.core.transaction.Transaction$State): final static field
    
    """
    IDLE: typing.ClassVar['Transaction.State'] = ...
    READY: typing.ClassVar['Transaction.State'] = ...
    SENDING: typing.ClassVar['Transaction.State'] = ...
    FAILED: typing.ClassVar['Transaction.State'] = ...
    ABORTED: typing.ClassVar['Transaction.State'] = ...
    COMMITTED: typing.ClassVar['Transaction.State'] = ...
    def abort(self) -> None: ...
    def commit(self) -> None: ...
    def commitAndWait(self) -> None: ...
    def getPendingValueCount(self) -> int: ...
    def getState(self) -> 'Transaction.State': ...
    def hasFailed(self) -> bool: ...
    def isReady(self) -> bool: ...
    def registerTransactionStateListener(self, transactionStateListener: 'TransactionStateListener') -> None: ...
    def unregisterTransactionStateListener(self) -> None: ...
    class State(java.io.Serializable):
        """
        Java class 'cern.japc.core.transaction.Transaction$State'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.io.Serializable
        
        """
        def toString(self) -> str: ...

class TransactionException(cern.japc.core.ParameterException):
    """
    Java class 'cern.japc.core.transaction.TransactionException'
    
        Extends:
            cern.japc.core.ParameterException
    
      Constructors:
        * TransactionException(java.lang.String)
        * TransactionException(java.lang.Exception)
        * TransactionException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class TransactionRuntimeException(cern.japc.core.ParameterRuntimeException):
    """
    Java class 'cern.japc.core.transaction.TransactionRuntimeException'
    
        Extends:
            cern.japc.core.ParameterRuntimeException
    
      Constructors:
        * TransactionRuntimeException(java.lang.String, java.lang.Exception)
        * TransactionRuntimeException(java.lang.Exception)
        * TransactionRuntimeException(java.lang.String)
        * TransactionRuntimeException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class TransactionStateListener:
    """
    Java class 'cern.japc.core.transaction.TransactionStateListener'
    
    """
    def transactionCommitted(self) -> None: ...
    def transactionFailed(self, string: str, transactionException: TransactionException) -> None: ...
    def transactionReady(self) -> None: ...

class TransactionalParameter(cern.japc.core.Parameter):
    """
    Java class 'cern.japc.core.transaction.TransactionalParameter'
    
        Interfaces:
            cern.japc.core.Parameter
    
    """
    def prepareValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, compositeTransaction: 'CompositeTransaction') -> None: ...

class BadSettingValueException(TransactionException):
    """
    Java class 'cern.japc.core.transaction.BadSettingValueException'
    
        Extends:
            cern.japc.core.transaction.TransactionException
    
      Constructors:
        * BadSettingValueException(java.lang.String)
        * BadSettingValueException(java.lang.Exception)
        * BadSettingValueException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class CompositeTransaction(Transaction):
    """
    Java class 'cern.japc.core.transaction.CompositeTransaction'
    
        Interfaces:
            cern.japc.core.transaction.Transaction
    
    """
    def add(self, object: typing.Any, transaction: Transaction) -> bool: ...
    def get(self, object: typing.Any) -> Transaction: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.transaction")``.

    BadSettingValueException: typing.Type[BadSettingValueException]
    CompositeTransaction: typing.Type[CompositeTransaction]
    Transaction: typing.Type[Transaction]
    TransactionException: typing.Type[TransactionException]
    TransactionRuntimeException: typing.Type[TransactionRuntimeException]
    TransactionStateListener: typing.Type[TransactionStateListener]
    TransactionalParameter: typing.Type[TransactionalParameter]
