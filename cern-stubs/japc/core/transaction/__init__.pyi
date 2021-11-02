import cern.japc.core
import cern.japc.value
import java.io
import java.lang
import typing



class Transaction:
    """
    public interface Transaction
    
        A class implementing this interface represents a transaction grouping a set of write accesses to the equipment.
        Typically, a transaction will group many setValue commands sent to different parameters of physical devices.
    
        As setting a value on the hardware parameters is an asynchronous action, the transaction keeps track of the status of
        each sending and provided a single entry point to commit or abort the sending. The transaction provide an atomic service
        for validating or enabling all sent values when commit is called.
    """
    IDLE: typing.ClassVar['Transaction.State'] = ...
    """
    static final :class:`~cern.japc.core.transaction.Transaction.State` IDLE
    
        The transaction does not hold anything. This is the initial state before the transaction get used
    
    """
    READY: typing.ClassVar['Transaction.State'] = ...
    """
    static final :class:`~cern.japc.core.transaction.Transaction.State` READY
    
        The transaction is ready to be commited, all values have been sent successfully
    
    """
    SENDING: typing.ClassVar['Transaction.State'] = ...
    """
    static final :class:`~cern.japc.core.transaction.Transaction.State` SENDING
    
        The transaction is sending values to the devices
    
    """
    FAILED: typing.ClassVar['Transaction.State'] = ...
    """
    static final :class:`~cern.japc.core.transaction.Transaction.State` FAILED
    
        The transaction failed to send one or more values
    
    """
    ABORTED: typing.ClassVar['Transaction.State'] = ...
    """
    static final :class:`~cern.japc.core.transaction.Transaction.State` ABORTED
    
        The transaction has been aborted
    
    """
    COMMITTED: typing.ClassVar['Transaction.State'] = ...
    """
    static final :class:`~cern.japc.core.transaction.Transaction.State` COMMITTED
    
        The transaction has been commited and is finished
    
    """
    def abort(self) -> None:
        """
            Aborts the transaction and leaves the devices untouched. No more value are sent after this called and values already
            sent are cancelled.
        
            Once abort is called the transaction cannot be committed anymore.
        
            Raises:
                :class:`~cern.japc.core.transaction.TransactionRuntimeException`: is abort is called after commit
        
        
        """
        ...
    def commit(self) -> None:
        """
            Commits this transaction without blocking. This method simply send a singal that the transaction should be commited. The
            commit will automatically take place as soon the transaction is ready. The potential listener on this transaction will
            be notified of the commit or of the failure of the transaction.
        
            Once commit is called the transaction cannot be aborted anymore.
        
            Raises:
                :class:`~cern.japc.core.transaction.TransactionRuntimeException`: is commit is called after abort
        
        
        """
        ...
    def commitAndWait(self) -> None: ...
    def getPendingValueCount(self) -> int:
        """
            Returns the number of values that are not yet sent or not yet acknoledged to be received by the device.
        
            Returns:
                the number of pending values.
        
        
        """
        ...
    def getState(self) -> 'Transaction.State':
        """
            Returns the current state of this transaction.
        
            Returns:
                the state of this transaction between the ones defined in this interface.
        
        
        """
        ...
    def hasFailed(self) -> bool:
        """
            Returns true if this transaction has failed to send at least one settings and cannot be commited. Trying to commit a
            failed transaction will throw an exception.
        
            Returns:
                true if this transaction has failed
        
        
        """
        ...
    def isReady(self) -> bool:
        """
            Returns true if this transaction is ready to be committed
        
            Returns:
                true if this transaction is ready to be committed
        
        
        """
        ...
    def registerTransactionStateListener(self, transactionStateListener: 'TransactionStateListener') -> None:
        """
            Registers a :code:`StateListener` object that can be notified of state changes in the transaction. A given transaction
            does not support more than one listener. Once a listener is registered another cannot be register unless it is
            unregistered before.
        
            Parameters:
                transactionStateListener (:class:`~cern.japc.core.transaction.TransactionStateListener`): the non null listener to register
        
            Raises:
                :class:`~cern.japc.core.transaction.TransactionRuntimeException`: if a listener is already registered.
        
        
        """
        ...
    def unregisterTransactionStateListener(self) -> None:
        """
            Unregisters an eventual :code:`StateListener` object. This method has no effect in no listener was registered.
        
        """
        ...
    class State(java.io.Serializable):
        def toString(self) -> str: ...

class TransactionException(cern.japc.core.ParameterException):
    """
    public class TransactionException extends :class:`~cern.japc.core.ParameterException`
    
        Thrown when a problem occurs with a hardware transaction.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class TransactionRuntimeException(cern.japc.core.ParameterRuntimeException):
    """
    public class TransactionRuntimeException extends :class:`~cern.japc.core.ParameterRuntimeException`
    
        Thrown when a problem occurs with a hardware transaction.
    
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

class TransactionStateListener:
    """
    public interface TransactionStateListener
    
        A class implementing this interface listens on the state changes of the transaction and receives notification.
    """
    def transactionCommitted(self) -> None:
        """
            Notifies that the transaction is in the committed state
        
        """
        ...
    def transactionFailed(self, string: str, transactionException: TransactionException) -> None:
        """
            Notifies that the transaction is in the failed state
        
            Parameters:
                failureDetail (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): gives a description of the failure.
                failureException (:class:`~cern.japc.core.transaction.TransactionException`): gives a potential exception source of the failure. Can be null.
        
        
        """
        ...
    def transactionReady(self) -> None:
        """
            Notifies that the transaction is in the ready state
        
        """
        ...

class TransactionalParameter(cern.japc.core.Parameter):
    def prepareValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, compositeTransaction: 'CompositeTransaction') -> None: ...

class BadSettingValueException(TransactionException):
    """
    public class BadSettingValueException extends :class:`~cern.japc.core.transaction.TransactionException`
    
        Thrown when a setting value is incorrect and cause the device to reject it.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class CompositeTransaction(Transaction):
    """
    public interface CompositeTransaction extends :class:`~cern.japc.core.transaction.Transaction`
    
        A :code:`CompositeTransaction` is a transaction that can be made of child transactions. A composite transaction allows
        to expose a single transaction to a client, while the underlying implementation is made of several transactions.
    
        This type of transaction could be useful if it is necessary to use one transaction per group of similar devices instead
        of one single transaction for all devices.
    """
    def add(self, object: typing.Any, transaction: Transaction) -> bool:
        """
            Adds a transaction to this composite transaction. If the given transaction is already part of this composite transaction
            nothing is done and this transaction is left unchanged.
        
            If this transaction is already commited or aborted, trying to add a child transaction is taking as an error and throws
            an exception.
        
            Parameters:
                key (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): an unique key allowing to retrieve the child transaction
                childTransaction (:class:`~cern.japc.core.transaction.Transaction`): the child transaction controlled by this transaction.
        
            Returns:
                boolean true is the given transaction has been added, false else.
        
            Raises:
                :class:`~cern.japc.core.transaction.TransactionRuntimeException`: if the method is called on a commited or aborted transaction
        
        
        """
        ...
    def get(self, object: typing.Any) -> Transaction:
        """
            Retrieves a transaction that has been added to this composite transaction.
        
            Parameters:
                key (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the unique key identifying the child transaction to retrieve
        
            Returns:
                the retrieved transaction or null if the key does not match any transaction.
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.transaction")``.

    BadSettingValueException: typing.Type[BadSettingValueException]
    CompositeTransaction: typing.Type[CompositeTransaction]
    Transaction: typing.Type[Transaction]
    TransactionException: typing.Type[TransactionException]
    TransactionRuntimeException: typing.Type[TransactionRuntimeException]
    TransactionStateListener: typing.Type[TransactionStateListener]
    TransactionalParameter: typing.Type[TransactionalParameter]
