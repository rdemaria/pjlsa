import cern.japc.core
import cern.japc.core.spi
import cern.japc.core.transaction
import cern.japc.value
import typing



class AbstractTransaction(cern.japc.core.transaction.Transaction):
    """
    public abstract class AbstractTransaction extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.transaction.Transaction`
    
        Provides a first implementation of the :code:`Transaction` interface that manages the state and the notification to a
        potential listener.
    
        The class also implements the commit and abort with an abstract template method that subclasses will implements. The
        implementation of commit and abort make sure the transaction is in the right state to be commited or aborted.
    
        This transaction is not thread safe.
    """
    def abort(self) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.transaction.Transaction.abort`
            Aborts the transaction and leaves the devices untouched. No more value are sent after this called and values already
            sent are cancelled.
        
            Once abort is called the transaction cannot be committed anymore.
        
            Specified by:
                :meth:`~cern.japc.core.transaction.Transaction.abort` in interface :class:`~cern.japc.core.transaction.Transaction`
        
        
        """
        ...
    def commit(self) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.transaction.Transaction.commit`
            Commits this transaction without blocking. This method simply send a singal that the transaction should be commited. The
            commit will automatically take place as soon the transaction is ready. The potential listener on this transaction will
            be notified of the commit or of the failure of the transaction.
        
            Once commit is called the transaction cannot be aborted anymore.
        
            Specified by:
                :meth:`~cern.japc.core.transaction.Transaction.commit` in interface :class:`~cern.japc.core.transaction.Transaction`
        
        
        """
        ...
    def commitAndWait(self) -> None: ...
    def getState(self) -> cern.japc.core.transaction.Transaction.State:
        """
            Description copied from interface: :meth:`~cern.japc.core.transaction.Transaction.getState`
            Returns the current state of this transaction.
        
            Specified by:
                :meth:`~cern.japc.core.transaction.Transaction.getState` in interface :class:`~cern.japc.core.transaction.Transaction`
        
            Returns:
                the state of this transaction between the ones defined in this interface.
        
        
        """
        ...
    def hasFailed(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.transaction.Transaction.hasFailed`
            Returns true if this transaction has failed to send at least one settings and cannot be commited. Trying to commit a
            failed transaction will throw an exception.
        
            Specified by:
                :meth:`~cern.japc.core.transaction.Transaction.hasFailed` in interface :class:`~cern.japc.core.transaction.Transaction`
        
            Returns:
                true if this transaction has failed
        
        
        """
        ...
    def isReady(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.transaction.Transaction.isReady`
            Returns true if this transaction is ready to be committed
        
            Specified by:
                :meth:`~cern.japc.core.transaction.Transaction.isReady` in interface :class:`~cern.japc.core.transaction.Transaction`
        
            Returns:
                true if this transaction is ready to be committed
        
        
        """
        ...
    def registerTransactionStateListener(self, transactionStateListener: cern.japc.core.transaction.TransactionStateListener) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.transaction.Transaction.registerTransactionStateListener`
            Registers a :code:`StateListener` object that can be notified of state changes in the transaction. A given transaction
            does not support more than one listener. Once a listener is registered another cannot be register unless it is
            unregistered before.
        
            Specified by:
                :meth:`~cern.japc.core.transaction.Transaction.registerTransactionStateListener`Â in
                interfaceÂ :class:`~cern.japc.core.transaction.Transaction`
        
            Parameters:
                transactionStateListener (:class:`~cern.japc.core.transaction.TransactionStateListener`): the non null listener to register
        
        
        """
        ...
    def unregisterTransactionStateListener(self) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.transaction.Transaction.unregisterTransactionStateListener`
            Unregisters an eventual :code:`StateListener` object. This method has no effect in no listener was registered.
        
            Specified by:
                :meth:`~cern.japc.core.transaction.Transaction.unregisterTransactionStateListener`Â in
                interfaceÂ :class:`~cern.japc.core.transaction.Transaction`
        
        
        """
        ...

class AbstractTransactionalParameter(cern.japc.core.spi.AbstractParameter, cern.japc.core.transaction.TransactionalParameter):
    def __init__(self, string: str): ...
    def prepareValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, compositeTransaction: cern.japc.core.transaction.CompositeTransaction) -> None: ...

class HardwareAccessTask:
    """
    public interface HardwareAccessTask
    
        Defines an executable task that accesses devices when performed and can therefore throw a TransactionException.
    """
    def performTask(self) -> None: ...

class TransactionalParameterDecorator(cern.japc.core.spi.ParameterDecorator, cern.japc.core.transaction.TransactionalParameter):
    def __init__(self, transactionalParameter: cern.japc.core.transaction.TransactionalParameter): ...
    def prepareValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, compositeTransaction: cern.japc.core.transaction.CompositeTransaction) -> None: ...

class CompositeTransactionImpl(AbstractTransaction, cern.japc.core.transaction.CompositeTransaction):
    """
    public class CompositeTransactionImpl extends :class:`~cern.japc.core.spi.transaction.AbstractTransaction` implements :class:`~cern.japc.core.transaction.CompositeTransaction`
    
        Provides a default implementation of a composite transaction.
    
        This transaction is thread safe.
    """
    def __init__(self): ...
    def add(self, object: typing.Any, transaction: cern.japc.core.transaction.Transaction) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.transaction.CompositeTransaction.add`
            Adds a transaction to this composite transaction. If the given transaction is already part of this composite transaction
            nothing is done and this transaction is left unchanged.
        
            If this transaction is already commited or aborted, trying to add a child transaction is taking as an error and throws
            an exception.
        
            Specified by:
                :meth:`~cern.japc.core.transaction.CompositeTransaction.add`Â in
                interfaceÂ :class:`~cern.japc.core.transaction.CompositeTransaction`
        
            Parameters:
                key (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): an unique key allowing to retrieve the child transaction
                transaction (:class:`~cern.japc.core.transaction.Transaction`): the child transaction controlled by this transaction.
        
            Returns:
                boolean true is the given transaction has been added, false else.
        
        
        """
        ...
    def get(self, object: typing.Any) -> cern.japc.core.transaction.Transaction:
        """
            Description copied from interface: :meth:`~cern.japc.core.transaction.CompositeTransaction.get`
            Retrieves a transaction that has been added to this composite transaction.
        
            Specified by:
                :meth:`~cern.japc.core.transaction.CompositeTransaction.get`Â in
                interfaceÂ :class:`~cern.japc.core.transaction.CompositeTransaction`
        
            Parameters:
                key (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the unique key identifying the child transaction to retrieve
        
            Returns:
                the retrieved transaction or null if the key does not match any transaction.
        
        
        """
        ...
    def getPendingValueCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.transaction.Transaction.getPendingValueCount`
            Returns the number of values that are not yet sent or not yet acknoledged to be received by the device.
        
            Specified by:
                :meth:`~cern.japc.core.transaction.Transaction.getPendingValueCount`Â in
                interfaceÂ :class:`~cern.japc.core.transaction.Transaction`
        
            Returns:
                the number of pending values.
        
        
        """
        ...

class SequentialTransaction(AbstractTransaction):
    """
    public abstract class SequentialTransaction extends :class:`~cern.japc.core.spi.transaction.AbstractTransaction`
    
        This transaction implements an active transaction that sends sequentially values to the hardware. Values to send to the
        hardware are added as tasks that are performed on a FIFO basis.
    
        This transaction is not thread safe.
    """
    def addSetValueTask(self, hardwareAccessTask: HardwareAccessTask) -> None:
        """
            Adds a new executable task that will be scheduled to be executed by this transaction. The task is sending value to
            hardware.
        
            Parameters:
                task (:class:`~cern.japc.core.spi.transaction.HardwareAccessTask`): the task of sending a value to perform
        
        
        """
        ...
    def getPendingValueCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.transaction.Transaction.getPendingValueCount`
            Returns the number of values that are not yet sent or not yet acknoledged to be received by the device.
        
            Returns:
                the number of pending values.
        
        
        """
        ...

class TransactionalParameterSupport(AbstractTransactionalParameter):
    """
    public class TransactionalParameterSupport extends :class:`~cern.japc.core.spi.transaction.AbstractTransactionalParameter`
    
        Support class that implements all abstract methods by throwing a ParameterRuntimeException warning that the method is
        not implemented.
    
        This class can be useful for subclass that do not support variant of get / set and do not want to implement them.
    """
    def __init__(self, string: str): ...

class AsynchronousParameterSupport(TransactionalParameterSupport):
    """
    public class AsynchronousParameterSupport extends :class:`~cern.japc.core.spi.transaction.TransactionalParameterSupport`
    
        This parameter add a default implementation of the synchronous get and set based on the asynchronous versions.
    """
    DEFAULT_TIMEOUT: typing.ClassVar[int] = ...
    """
    public static long DEFAULT_TIMEOUT
    
    
    """
    def __init__(self, string: str): ...

class SynchronousParameterSupport(TransactionalParameterSupport):
    """
    public class SynchronousParameterSupport extends :class:`~cern.japc.core.spi.transaction.TransactionalParameterSupport`
    
        This parameter add a default implementation of the asynchronous get and set based on the synchronous versions.
    """
    SYSPROP_MAXTHREADS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_MAXTHREADS
    
        System property ("japc.async.getset.maxthreads") for maximum number of thread in the pool of executor.
    
    
        Default is 40.
    
        Also see:
            :meth:`~constant`
    
    
    """
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
