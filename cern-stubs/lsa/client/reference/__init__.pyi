import cern.accsoft.commons.util.value
import cern.japc.core
import cern.japc.value
import cern.lsa.client.reference.impl
import java.lang
import java.util
import typing



class ParameterReferences:
    """
    Java class 'cern.lsa.client.reference.ParameterReferences'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ParameterReferences(java.lang.String, java.util.Map)
    
    """
    def __init__(self, string: str, map: typing.Union[java.util.Map[cern.japc.core.Selector, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]], typing.Mapping[cern.japc.core.Selector, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]]]): ...
    def getParameterName(self) -> str: ...
    def getReference(self, selector: cern.japc.core.Selector) -> cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]: ...
    def getReferences(self) -> java.util.Map[cern.japc.core.Selector, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]]: ...
    def getSelectors(self) -> java.util.Set[cern.japc.core.Selector]: ...

class ReferenceController:
    """
    Java class 'cern.lsa.client.reference.ReferenceController'
    
    """
    def addReferenceListener(self, string: str, selector: cern.japc.core.Selector, referenceListener: 'ReferenceListener') -> None: ...
    def getReference(self, string: str, selector: cern.japc.core.Selector) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    def getReferences(self, string: str, collection: typing.Union[java.util.Collection[cern.japc.core.Selector], typing.Sequence[cern.japc.core.Selector]]) -> ParameterReferences: ...
    @typing.overload
    def getReferences(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]], selector: cern.japc.core.Selector) -> java.util.Map[str, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]]: ...
    def removeReferenceListener(self, string: str, selector: cern.japc.core.Selector) -> None: ...

class ReferenceException(java.lang.RuntimeException):
    """
    Java class 'cern.lsa.client.reference.ReferenceException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * ReferenceException(java.lang.String)
        * ReferenceException(java.lang.Throwable)
        * ReferenceException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class ReferenceListener:
    """
    Java class 'cern.lsa.client.reference.ReferenceListener'
    
    """
    def onReferenceChanged(self, string: str, selector: cern.japc.core.Selector, failSafeValue: cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.reference")``.

    ParameterReferences: typing.Type[ParameterReferences]
    ReferenceController: typing.Type[ReferenceController]
    ReferenceException: typing.Type[ReferenceException]
    ReferenceListener: typing.Type[ReferenceListener]
    impl: cern.lsa.client.reference.impl.__module_protocol__
