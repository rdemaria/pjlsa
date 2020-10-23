from typing import Any as _py_Any
from typing import ClassVar as _py_ClassVar
from typing import overload
import cern.japc.core
import cern.japc.value
import java.io
import java.lang


class Transaction:
    IDLE: _py_ClassVar['Transaction.State'] = ...
    READY: _py_ClassVar['Transaction.State'] = ...
    SENDING: _py_ClassVar['Transaction.State'] = ...
    FAILED: _py_ClassVar['Transaction.State'] = ...
    ABORTED: _py_ClassVar['Transaction.State'] = ...
    COMMITTED: _py_ClassVar['Transaction.State'] = ...
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
        def toString(self) -> str: ...

class TransactionException(cern.japc.core.ParameterException):
    @overload
    def __init__(self, exception: java.lang.Exception): ...
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class TransactionRuntimeException(cern.japc.core.ParameterRuntimeException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, exception: java.lang.Exception): ...
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class TransactionStateListener:
    def transactionCommitted(self) -> None: ...
    def transactionFailed(self, string: str, transactionException: TransactionException) -> None: ...
    def transactionReady(self) -> None: ...

class TransactionalParameter(cern.japc.core.Parameter):
    def prepareValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, compositeTransaction: 'CompositeTransaction') -> None: ...

class BadSettingValueException(TransactionException):
    @overload
    def __init__(self, exception: java.lang.Exception): ...
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class CompositeTransaction(Transaction):
    def add(self, object: _py_Any, transaction: Transaction) -> bool: ...
    def get(self, object: _py_Any) -> Transaction: ...