import cern
import cern.japc.core
import cern.japc.core.group
import cern.japc.core.spi.transaction
import cern.japc.value
import typing



class GroupBasedViewParameter(cern.japc.core.spi.transaction.TransactionalParameterSupport):
    """
    Java class 'cern.japc.core.group.support.GroupBasedViewParameter'
    
        Extends:
            cern.japc.core.spi.transaction.TransactionalParameterSupport
    
      Constructors:
        * GroupBasedViewParameter(java.lang.String, cern.japc.core.group.ImmutableParameterGroup, cern.japc.core.group.ParameterGroupValueReceivedAdapter)
    
    """
    def __init__(self, string: str, immutableParameterGroup: cern.japc.core.group.ImmutableParameterGroup, parameterGroupValueReceivedAdapter: cern.japc.core.group.ParameterGroupValueReceivedAdapter): ...
    def getImmutableParameterGroup(self) -> cern.japc.core.group.ImmutableParameterGroup: ...
    def toString(self) -> str: ...

class ParameterGroupValueReceivedConcentrator(cern.japc.core.group.ParameterGroupValueReceivedAdapter):
    """
    Java class 'cern.japc.core.group.support.ParameterGroupValueReceivedConcentrator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.group.ParameterGroupValueReceivedAdapter
    
      Constructors:
        * ParameterGroupValueReceivedConcentrator(java.lang.String)
        * ParameterGroupValueReceivedConcentrator(java.lang.String, cern.japc.core.group.support.ConcentratorHelper.LengthExtractor)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, lengthExtractor: 'ConcentratorHelper.LengthExtractor'): ...
    def adaptValueReceived(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> cern.japc.core.AcquiredParameterValue: ...

class SysoutFailSafeParameterValueListener(cern.japc.core.group.FailSafeParameterValueListener):
    """
    Java class 'cern.japc.core.group.support.SysoutFailSafeParameterValueListener'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.group.FailSafeParameterValueListener
    
      Constructors:
        * SysoutFailSafeParameterValueListener()
    
    """
    def __init__(self): ...
    def valueReceived(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> None: ...

class GroupBasedParameter(GroupBasedViewParameter):
    """
    Java class 'cern.japc.core.group.support.GroupBasedParameter'
    
        Extends:
            cern.japc.core.group.support.GroupBasedViewParameter
    
      Constructors:
        * GroupBasedParameter(java.lang.String, cern.japc.core.group.TransactionalParameterGroup, cern.japc.core.group.ParameterGroupValueReceivedAdapter, cern.japc.core.group.ParameterGroupValueSentAdapter)
    
    """
    def __init__(self, string: str, transactionalParameterGroup: cern.japc.core.group.TransactionalParameterGroup, parameterGroupValueReceivedAdapter: cern.japc.core.group.ParameterGroupValueReceivedAdapter, parameterGroupValueSentAdapter: cern.japc.core.group.ParameterGroupValueSentAdapter): ...
    def getTransactionalParameterGroup(self) -> cern.japc.core.group.TransactionalParameterGroup: ...

class ConcentratorHelper:
    """
    Java class 'cern.japc.core.group.support.ConcentratorHelper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConcentratorHelper()
    
    """
    def __init__(self): ...
    @staticmethod
    def appendParameterValue(mapParameterValueArray: typing.List[cern.japc.value.MapParameterValue], string: str) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def mergeParameterValue(mapParameterValueArray: typing.List[cern.japc.value.MapParameterValue]) -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def mergeParameterValue(mapParameterValueArray: typing.List[cern.japc.value.MapParameterValue], string: str) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def mergeParameterValue(mapParameterValueArray: typing.List[cern.japc.value.MapParameterValue], string: str, lengthExtractor: 'ConcentratorHelper.LengthExtractor') -> cern.japc.value.SimpleParameterValue: ...
    class LengthExtractor:
        """
        Java class 'cern.japc.core.group.support.ConcentratorHelper$LengthExtractor'
        
        """
        def extractLength(self, mapParameterValue: cern.japc.value.MapParameterValue, int: int, string: str) -> int: ...
    class NameBasedLengthExtractor(cern.japc.core.group.support.ConcentratorHelper.LengthExtractor):
        """
        Java class 'cern.japc.core.group.support.ConcentratorHelper$NameBasedLengthExtractor'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                cern.japc.core.group.support.ConcentratorHelper.LengthExtracto
                r
        
          Constructors:
            * NameBasedLengthExtractor(java.lang.String)
        
        """
        def __init__(self, string: str): ...
        def extractLength(self, mapParameterValue: cern.japc.value.MapParameterValue, int: int, string: str) -> int: ...
    class Selector:
        """
        Java class 'cern.japc.core.group.support.ConcentratorHelper$Selector'
        
        """
        def select(self, simpleParameterValue: cern.japc.value.SimpleParameterValue, int: int) -> bool: ...
    class SelectorBasedLengthExtractor(cern.japc.core.group.support.ConcentratorHelper.LengthExtractor):
        """
        Java class 'cern.japc.core.group.support.ConcentratorHelper$SelectorBasedLengthExtractor'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                cern.japc.core.group.support.ConcentratorHelper.LengthExtracto
                r
        
          Constructors:
            * SelectorBasedLengthExtractor(java.lang.String, cern.japc.core.group.support.ConcentratorHelper.Selector)
            * SelectorBasedLengthExtractor(java.lang.String, cern.japc.core.group.support.ConcentratorHelper.Selector, boolean)
        
        """
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
