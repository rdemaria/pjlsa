import cern
import cern.japc.core
import cern.japc.core.group
import cern.japc.core.spi.transaction
import cern.japc.value
import typing



class GroupBasedViewParameter(cern.japc.core.spi.transaction.TransactionalParameterSupport):
    """
    public class GroupBasedViewParameter extends :class:`~cern.japc.core.spi.transaction.TransactionalParameterSupport`
    
        A Parameter that represents a read only view on a group of parameters. Only primitive operations for read (get/monitor)
        are supported. When performed on this parameter, they are delegated to the adapted group of parameters. The value
        received are adapted using the given :code:`ParameterGroupValueReceivedAdapter`. Any call to write method on this
        parameter will throw a runtime exception as they are not supported.
    """
    def __init__(self, string: str, immutableParameterGroup: cern.japc.core.group.ImmutableParameterGroup, parameterGroupValueReceivedAdapter: cern.japc.core.group.ParameterGroupValueReceivedAdapter): ...
    def getImmutableParameterGroup(self) -> cern.japc.core.group.ImmutableParameterGroup:
        """
            Getter for the underlying parameter group.
        
            Returns:
                underlying parameter group.
        
        
        """
        ...
    def toString(self) -> str:
        """
            Description copied from class: :meth:`~cern.japc.core.spi.AbstractImmutableParameter.toString`
            Return a string representation of this object.
        
            Overrides:
                :meth:`~cern.japc.core.spi.AbstractImmutableParameter.toString`Â in
                classÂ :class:`~cern.japc.core.spi.AbstractImmutableParameter`
        
            Returns:
                a string representation of this object.
        
        
        """
        ...

class ParameterGroupValueReceivedConcentrator(cern.japc.core.group.ParameterGroupValueReceivedAdapter):
    """
    public class ParameterGroupValueReceivedConcentrator extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.group.ParameterGroupValueReceivedAdapter`
    
        Implementation of :code:`ParameterGroupValueSentAdapter` that provides default behavior to merge the headers be
        retaining only the first one. The values are then concentrated one by one. The default strategy to concentrate the value
        is to merge them. It is possible to change the behavior by overriding :code:`adaptSimpleValue`. TODO support other type
        than map
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, lengthExtractor: 'ConcentratorHelper.LengthExtractor'): ...
    def adaptValueReceived(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> cern.japc.core.AcquiredParameterValue: ...

class SysoutFailSafeParameterValueListener(cern.japc.core.group.FailSafeParameterValueListener):
    """
    public class SysoutFailSafeParameterValueListener extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.group.FailSafeParameterValueListener`
    
        Implements a simple ParameterValueListener that ouput the values and exceptions received on the command line.
    """
    def __init__(self): ...
    def valueReceived(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.FailSafeParameterValueListener.valueReceived`
            Notifies this listener that the new values have been received.
        
            Specified by:
                :meth:`~cern.japc.core.group.FailSafeParameterValueListener.valueReceived`Â in
                interfaceÂ :class:`~cern.japc.core.group.FailSafeParameterValueListener`
        
            Parameters:
                values (:class:`~cern.japc.core.FailSafeParameterValue`[]): the new values received for the monitored parameters.
        
        
        """
        ...

class GroupBasedParameter(GroupBasedViewParameter):
    """
    public class GroupBasedParameter extends :class:`~cern.japc.core.group.support.GroupBasedViewParameter`
    
        A Parameter that is based on a group of parameters. All operations are supported. When performed on this parameter, they
        are delegated to the group of adapted parameters. The value sent are adapted using the given
        :code:`ParameterGroupValueSentAdapter`.
    """
    def __init__(self, string: str, transactionalParameterGroup: cern.japc.core.group.TransactionalParameterGroup, parameterGroupValueReceivedAdapter: cern.japc.core.group.ParameterGroupValueReceivedAdapter, parameterGroupValueSentAdapter: cern.japc.core.group.ParameterGroupValueSentAdapter): ...
    def getTransactionalParameterGroup(self) -> cern.japc.core.group.TransactionalParameterGroup:
        """
            Getter for the underlying parameter group.
        
            Returns:
                the underlying parameter group.
        
        
        """
        ...

class ConcentratorHelper:
    """
    public class ConcentratorHelper extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Provides helper methods to concentrate several parameter values into one.
    
        For example, this is useful when used with a :code:`GroupBasedParameter` where the values of the group needs to be
        concentrated into one.
    """
    def __init__(self): ...
    @staticmethod
    def appendParameterValue(mapParameterValueArray: typing.List[cern.japc.value.MapParameterValue], string: str) -> cern.japc.value.SimpleParameterValue:
        """
            Merges a :code:`fieldName` of :code:`valuesToMerge` into a single scalar value.
        
            Parameters:
                valuesToMerge (cern.japc.value.MapParameterValue[]):         fieldName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                merged value for
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def mergeParameterValue(mapParameterValueArray: typing.List[cern.japc.value.MapParameterValue]) -> cern.japc.value.MapParameterValue:
        """
            Merges :code:`valuesToMerge` into a single :code:`MapParameterValue`.
        
            Parameters:
                valuesToMerge (cern.japc.value.MapParameterValue[]): non-empty array fo values ot merge
        
            Returns:
                merged value containing array values for each field
        
        """
        ...
    @typing.overload
    @staticmethod
    def mergeParameterValue(mapParameterValueArray: typing.List[cern.japc.value.MapParameterValue], string: str) -> cern.japc.value.SimpleParameterValue:
        """
            Merges a :code:`fieldName` of :code:`valuesToMerge` into a single array value.
        
            Parameters:
                valuesToMerge (cern.japc.value.MapParameterValue[]):         fieldName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                merged value for
        
        """
        ...
    @typing.overload
    @staticmethod
    def mergeParameterValue(mapParameterValueArray: typing.List[cern.japc.value.MapParameterValue], string: str, lengthExtractor: 'ConcentratorHelper.LengthExtractor') -> cern.japc.value.SimpleParameterValue:
        """
            Merges a :code:`fieldName` of :code:`valuesToMerge` into a single array value.
        
            Parameters:
                valuesToMerge (cern.japc.value.MapParameterValue[]):         fieldName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                merged value for
        
        
        """
        ...
    class LengthExtractor:
        def extractLength(self, mapParameterValue: cern.japc.value.MapParameterValue, int: int, string: str) -> int: ...
    class NameBasedLengthExtractor(cern.japc.core.group.support.ConcentratorHelper.LengthExtractor):
        def __init__(self, string: str): ...
        def extractLength(self, mapParameterValue: cern.japc.value.MapParameterValue, int: int, string: str) -> int: ...
    class Selector:
        def select(self, simpleParameterValue: cern.japc.value.SimpleParameterValue, int: int) -> bool: ...
    class SelectorBasedLengthExtractor(cern.japc.core.group.support.ConcentratorHelper.LengthExtractor):
        @typing.overload
        def __init__(self, string: str, selector: 'ConcentratorHelper.Selector'): ...
        @typing.overload
        def __init__(self, string: str, selector: 'ConcentratorHelper.Selector', boolean: bool): ...
        def extractLength(self, mapParameterValue: cern.japc.value.MapParameterValue, int: int, string: str) -> int: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.group.support")``.

    ConcentratorHelper: typing.Type[ConcentratorHelper]
    GroupBasedParameter: typing.Type[GroupBasedParameter]
    GroupBasedViewParameter: typing.Type[GroupBasedViewParameter]
    ParameterGroupValueReceivedConcentrator: typing.Type[ParameterGroupValueReceivedConcentrator]
    SysoutFailSafeParameterValueListener: typing.Type[SysoutFailSafeParameterValueListener]
