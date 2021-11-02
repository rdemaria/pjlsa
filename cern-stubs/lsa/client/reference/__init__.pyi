import cern.accsoft.commons.util.value
import cern.japc.core
import cern.japc.value
import cern.lsa.client.reference.impl
import java.lang
import java.util
import typing



class ParameterReferences:
    """
    public class ParameterReferences extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Container for single parameter references for different selectors.
    """
    def __init__(self, string: str, map: typing.Union[java.util.Map[cern.japc.core.Selector, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]], typing.Mapping[cern.japc.core.Selector, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]]]): ...
    def getParameterName(self) -> str:
        """
        
            Returns:
                parameter name (never :code:`null`)
        
        
        """
        ...
    def getReference(self, selector: cern.japc.core.Selector) -> cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]:
        """
        
            Parameters:
                selector (cern.japc.core.Selector): 
            Returns:
                parameter reference for selector (never :code:`null`). The reference can be one of:
        
                  - :code:`SimpleParameterValue` if the reference is found
                  - an exception specifying the problem while searching for reference
                  - empty if the reference value does not exist for requested parameter and selector
        
        
        
        """
        ...
    def getReferences(self) -> java.util.Map[cern.japc.core.Selector, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]]: ...
    def getSelectors(self) -> java.util.Set[cern.japc.core.Selector]: ...

class ReferenceController:
    """
    public interface ReferenceController
    
        The controller provides read-only access to LSA references.
    """
    def addReferenceListener(self, string: str, selector: cern.japc.core.Selector, referenceListener: 'ReferenceListener') -> None:
        """
            Adds a :class:`~cern.lsa.client.reference.ReferenceListener`.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name
                selector (cern.japc.core.Selector): selector specifying the timing user
                listener (:class:`~cern.lsa.client.reference.ReferenceListener`): listener
        
        
        """
        ...
    def getReference(self, string: str, selector: cern.japc.core.Selector) -> cern.japc.value.SimpleParameterValue:
        """
            Gets the reference value for the given parameter and selector.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a parameter name
                selector (cern.japc.core.Selector): selector specifying the timing user
        
            Returns:
                :code:`ParameterValue` or :code:`null` if the reference doesn't exist or no context is mapped to the timing user
        
            Raises:
                : if:
        
                      - PPM parameter and non-PPM selector is specified
                      - non-PPM parameter and PPM selector is specified
                      - "all timing user" selector (*.USER.ALL) is specified
        
                :class:`~cern.lsa.client.reference.ReferenceException`: if there was a problem with data retrieving
        
        
        """
        ...
    @typing.overload
    def getReferences(self, string: str, collection: typing.Union[java.util.Collection[cern.japc.core.Selector], typing.Sequence[cern.japc.core.Selector]]) -> ParameterReferences: ...
    @typing.overload
    def getReferences(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]], selector: cern.japc.core.Selector) -> java.util.Map[str, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]]: ...
    def removeReferenceListener(self, string: str, selector: cern.japc.core.Selector) -> None:
        """
            Removes a :class:`~cern.lsa.client.reference.ReferenceListener`.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name
                selector (cern.japc.core.Selector): selector specifying the timing user
        
        
        """
        ...

class ReferenceException(java.lang.RuntimeException):
    """
    public class ReferenceException extends `RuntimeException <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>`
    
        Indicates a problem related to LSA parameter references.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class ReferenceListener:
    """
    public interface ReferenceListener
    
        Listener for reference changes.
    """
    def onReferenceChanged(self, string: str, selector: cern.japc.core.Selector, failSafeValue: cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]) -> None:
        """
            Callback on reference update.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`):         selector (cern.japc.core.Selector):         newValue (cern.accsoft.commons.util.value.FailSafeValue<cern.japc.value.SimpleParameterValue> newValue): 
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.reference")``.

    ParameterReferences: typing.Type[ParameterReferences]
    ReferenceController: typing.Type[ReferenceController]
    ReferenceException: typing.Type[ReferenceException]
    ReferenceListener: typing.Type[ReferenceListener]
    impl: cern.lsa.client.reference.impl.__module_protocol__
