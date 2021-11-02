import java.lang.reflect
import java.util.concurrent
import typing



class MethodInvoker:
    """
    public interface MethodInvoker
    
        Interface that allows providing different strategies of calling a specific method with the same arguments on several
        target objects.
    
        The interface was introduced to support :code:`Observer` pattern when one entity wants to notify several listeners about
        an event.
    """
    def invoke(self, objectArray: typing.List[typing.Any], method: java.lang.reflect.Method, objectArray2: typing.List[typing.Any]) -> typing.List[typing.Any]:
        """
            Invokes the specified method on all given targets.
        
            Parameters:
                targets (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`[]): target objects
                method (`Method <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/reflect/Method.html?is-external=true>`): method to be called
                args (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`[]): method arguments
        
            Returns:
                non-null array of method invocation results
        
        
        """
        ...

class AbstractMethodInvoker(MethodInvoker):
    """
    public abstract class AbstractMethodInvoker extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.reflect.MethodInvoker`
    
        Abstract implementation of the :code:`MethodInvoker` interface providing some common operations.
    """
    def __init__(self): ...
    def invoke(self, objectArray: typing.List[typing.Any], method: java.lang.reflect.Method, objectArray2: typing.List[typing.Any]) -> typing.List[typing.Any]:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.reflect.MethodInvoker.invoke`
            Invokes the specified method on all given targets.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.reflect.MethodInvoker.invoke`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.reflect.MethodInvoker`
        
            Parameters:
                targets (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`[]): target objects
                method (`Method <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/reflect/Method.html?is-external=true>`): method to be called
                args (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`[]): method arguments
        
            Returns:
                non-null array of method invocation results
        
            To be used by extending classes. Calls :meth:`~cern.accsoft.commons.util.ReflectionUtils.invokeMethod`.
        
        """
        ...

class ExecutorServiceMethodInvoker(AbstractMethodInvoker):
    """
    public class ExecutorServiceMethodInvoker extends :class:`~cern.accsoft.commons.util.reflect.AbstractMethodInvoker`
    
        Method invoker that uses internally an `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/ExecutorService.html?is-external=true>` to call
        given method on specified target objects.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, executorService: java.util.concurrent.ExecutorService, long: int): ...
    def getExecutorService(self) -> java.util.concurrent.ExecutorService:
        """
        
            Returns:
                the executorService used by this invoker
        
        
        """
        ...
    def getMethodInvocationTimeout(self) -> int:
        """
            Returns timeout (in milliseconds) used when waiting for method execution result. If negative (or zero) timeout is
            specified, the timeout is not used.
        
            Also see:
                :meth:`~cern.accsoft.commons.util.reflect.ExecutorServiceMethodInvoker.%3Cinit%3E`, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/Future.html?is-external=true#get(long,java.util.concurrent.TimeUnit)>`
        
        
        """
        ...

class SameThreadMethodInvoker(AbstractMethodInvoker):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...

class SwingThreadMethodInvoker(AbstractMethodInvoker):
    """
    public class SwingThreadMethodInvoker extends :class:`~cern.accsoft.commons.util.reflect.AbstractMethodInvoker`
    
        Method invoker that delegates all method calls to the Event Dispatching Thread using `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/swing/SwingUtilities.html?is-external=true#invokeLater(java.lang.Runnable)>`
        construct. The method call runnables are added to the Swing event queue in the same order as given targets i.e. the
        specified targets will be called sequentially, preserving the specified order.
    
        This invoker can be used only with methods that don't return any results, since internally it uses :code:`Runnable`s
        (that have :code:`void run()` method).
    """
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.reflect")``.

    AbstractMethodInvoker: typing.Type[AbstractMethodInvoker]
    ExecutorServiceMethodInvoker: typing.Type[ExecutorServiceMethodInvoker]
    MethodInvoker: typing.Type[MethodInvoker]
    SameThreadMethodInvoker: typing.Type[SameThreadMethodInvoker]
    SwingThreadMethodInvoker: typing.Type[SwingThreadMethodInvoker]
