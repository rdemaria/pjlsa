import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.domain.zones
import cern.accsoft.commons.value
import cern.lsa.domain.commons
import cern.lsa.domain.commons.spi
import cern.lsa.domain.devices
import cern.lsa.domain.devices.type
import cern.lsa.domain.settings
import cern.lsa.domain.settings.spi
import cern.lsa.domain.settings.type
import datetime
import java.time
import java.util
import typing



_AbstractKnobBuilder__T = typing.TypeVar('_AbstractKnobBuilder__T', bound='AbstractKnobBuilder')  # <T>
class AbstractKnobBuilder(typing.Generic[_AbstractKnobBuilder__T]):
    """
    public abstract class AbstractKnobBuilder<T extends AbstractKnobBuilder<T>> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder for :class:`~cern.lsa.domain.settings.Knob`.
    
        It can be used for to create a new :class:`~cern.lsa.domain.settings.Knob` from scratch or basing on an existing one.
    """
    @typing.overload
    def addFactor(self, knobFactor: cern.lsa.domain.settings.KnobFactor) -> _AbstractKnobBuilder__T:
        """
            Adds a knob factor.
        
            Parameters:
                knobFactor (:class:`~cern.lsa.domain.settings.KnobFactor`): factor for a component-optic pair
        
            Returns:
                this builder for chaining
        
            Raises:
                : if a factor is already defined for this component-optic pair
        
        
        """
        ...
    @typing.overload
    def addFactor(self, string: str, string2: str, double: float) -> _AbstractKnobBuilder__T:
        """
            Adds a knob factor.
        
            Parameters:
                componentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of a knob component
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): optic name of an optic
                factor (double): factor for this component-optic pair
        
            Returns:
                this builder for chaining
        
            Raises:
                : if a factor is already defined for this component-optic pair
        
        """
        ...
    @typing.overload
    def addOrUpdateFactor(self, knobFactor: cern.lsa.domain.settings.KnobFactor) -> _AbstractKnobBuilder__T:
        """
            Adds or updates a knob factor.
        
            This methods adds a factor if it is not defined yet or updates an existing one.
        
            Parameters:
                knobFactor (:class:`~cern.lsa.domain.settings.KnobFactor`): factor for a component-optic pair
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    @typing.overload
    def addOrUpdateFactor(self, string: str, string2: str, double: float) -> _AbstractKnobBuilder__T:
        """
            Adds or updates a knob factor.
        
            This methods adds a factor if it is not defined yet or updates an existing one.
        
            Parameters:
                componentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of a knob component
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): optic name of an optic
                factor (double): factor for this component-optic pair
        
            Returns:
                this builder for chaining
        
        """
        ...
    def build(self) -> cern.lsa.domain.settings.Knob:
        """
            Builds the knob with all the supplied data.
        
            Returns:
                a fully configured knob
        
            Raises:
                : if the provided data was inconsistent or missing, or if a knob has already been created with this builder
        
        
        """
        ...
    def clear(self) -> _AbstractKnobBuilder__T:
        """
            Cleans all the factors.
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    def removeFactor(self, string: str, string2: str) -> _AbstractKnobBuilder__T:
        """
            Cleans a knob factor.
        
            Parameters:
                componentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of a knob component
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): optic name of an optic
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    @typing.overload
    def updateFactor(self, knobFactor: cern.lsa.domain.settings.KnobFactor) -> _AbstractKnobBuilder__T:
        """
            Updates a knob factor.
        
            Parameters:
                knobFactor (:class:`~cern.lsa.domain.settings.KnobFactor`): factor for a component-optic pair
        
            Returns:
                this builder for chaining
        
            Raises:
                : if a factor is not yet defined for this component-optic pair
        
        
        """
        ...
    @typing.overload
    def updateFactor(self, string: str, string2: str, double: float) -> _AbstractKnobBuilder__T:
        """
            Updates a knob factor.
        
            Parameters:
                componentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of a knob component
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): optic name of an optic
                factor (double): factor for this component-optic pair
        
            Returns:
                this builder for chaining
        
            Raises:
                : if a factor is not yet defined for this component-optic pair
        
        """
        ...

class BeamProcessIncorporationRequestBuilder(cern.lsa.domain.commons.spi.AbstractPropertiesHolder):
    """
    public class BeamProcessIncorporationRequestBuilder extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder`
    
        Builder for instances of the :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest` interface covering the
        use-case of incorporation of a point from a source beam process into a point in destination beam process (for all or
        selected parameters) Example of usage:
    
        .. code-block: java
        
         BeamProcessIncorporationRequestBuilder builder = BeamProcessIncorporationRequestBuilder.newInstance();
         builder.setSourceBeamProcess(sourceBeamProcess);
         builder.setDestBeamProcess(destBeamProcess);
         builder.setSourcePoint(sourcePointInTime); // not needed in case of an actual source beam process
         builder.setDestPoint(destPointInTime);
         builder.setParameters(parameters); // all parameters of the source beam process if not specified
         builder.setSettingPart(SettingPartEnum.TARGET_AND_CORRECTION); // default VALUE
         IncorporationRequest request = builder.build();
         // Call the incorporate API
         trimService.incorporate(request);
         
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.settings.BeamProcessIncorporationRequest:
        """
        
            Returns:
                new instance of :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest`
        
        
        """
        ...
    def setDescription(self, string: str) -> 'BeamProcessIncorporationRequestBuilder':
        """
        
            Parameters:
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setDestBeamProcess(self, beamProcess: cern.lsa.domain.settings.BeamProcess) -> 'BeamProcessIncorporationRequestBuilder':
        """
        
            Parameters:
                destBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): 
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setDestPointInTime(self, double: float) -> 'BeamProcessIncorporationRequestBuilder':
        """
        
            Parameters:
                destPointInTime (double): 
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setDrive(self, boolean: bool) -> 'BeamProcessIncorporationRequestBuilder':
        """
        
            Parameters:
                drive (boolean): :code:`true` to drive the incorporated settings
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setIncorporateAllParameters(self) -> 'BeamProcessIncorporationRequestBuilder':
        """
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setParameters(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> 'BeamProcessIncorporationRequestBuilder': ...
    def setSettingPart(self, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'BeamProcessIncorporationRequestBuilder':
        """
        
            Parameters:
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): 
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setSettingsSource(self, settingsSource: cern.lsa.domain.settings.SettingsSource) -> 'BeamProcessIncorporationRequestBuilder':
        """
        
            Parameters:
                settingsSource (:class:`~cern.lsa.domain.settings.SettingsSource`): 
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setSourceBeamProcess(self, beamProcess: cern.lsa.domain.settings.BeamProcess) -> 'BeamProcessIncorporationRequestBuilder':
        """
        
            Parameters:
                sourceBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): 
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setSourcePointInTime(self, double: float) -> 'BeamProcessIncorporationRequestBuilder':
        """
        
            Parameters:
                sourcePointInTime (double): 
            Returns:
                this instance for chaining
        
        
        """
        ...

class ContextSettingsBuilder:
    """
    public class ContextSettingsBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder for instances of the :class:`~cern.lsa.domain.settings.ContextSettings` interface. The typical usage of the
        builder is following:
    
    
        .. code-block: java
        
         ContextSettingsBuilder builder = new ContextSettingsBuilder();
         builder.context(myCycle);
         builder.addFunction(myParam, myFunction);
         builder.addScalar(myParam2, myScalar);
         ContextSettings ctxSettings = builder.build();
         
    
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, contextSettings: cern.lsa.domain.settings.ContextSettings): ...
    def addFunction(self, parameter: cern.lsa.domain.settings.Parameter, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> 'ContextSettingsBuilder':
        """
            Adds new function value for given parameter. The function is expected to have X coordinates within the
            :class:`~cern.lsa.domain.settings.StandAloneContext`
        
            Given function is cut into segments corresponding to intersected beam process.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter for which to add the function
                function (cern.accsoft.commons.value.ImmutableDiscreteFunction): new parameter value
        
            Returns:
                this instance for chaining
        
            Raises:
                : if either parameter or function is :code:`null` or if the function can't be mapped to any beam process from the given
                    context e.g. if the cycle is from 0 to 1000 but the function starts at X=2000
        
        
        """
        ...
    def addFunctionsArray(self, parameter: cern.lsa.domain.settings.Parameter, immutableDiscreteFunctionsArray: cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray) -> 'ContextSettingsBuilder':
        """
            Adds new functionsArray value for given parameter. The functions within the functions array are expected to have X
            coordinates within the :class:`~cern.lsa.domain.settings.StandAloneContext`.
        
            Given functionsArray is cut into segments corresponding to intersected beam process.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter for which to add a setting
                functionsArray (cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray): new parameter value
        
            Returns:
                this instance for chaining
        
            Raises:
                : if either parameter or functionsArray is :code:`null` or if the functionsArray can't be mapped to any beam process from
                    the given context e.g. if the cycle is from 0 to 1000 but the function starts at X=2000
        
        
        """
        ...
    @typing.overload
    def addScalar(self, parameter: cern.lsa.domain.settings.Parameter, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> 'ContextSettingsBuilder':
        """
            Adds scalar value for the given parameter to the current context.
        
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter for wich to add a scalar
                scalar (cern.accsoft.commons.value.ImmutableScalar): new parameter value (or delta)
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.factory.ContextSettingsBuilder.addScalar`
        
            Adds new scalar value for given parameter and context.
        
            The method searches for all compatible beam processes with given parameter that intersect with specified drivable
            context. If there is more than one beam process matching, the method adds scalar to the first matching beam process with
            preference for beam-in (and discrete) i.e. if the first beam process is beam-out and then there are few beam-in beam
            processes - the method will add value to the first beam-in. If there are only beam-out beam processes, the method will
            add the value to the first beam-out.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter for which to add the scalar
                ctx (:class:`~cern.lsa.domain.settings.DrivableContext`): drivable context for which the scalar should be used: cycle or beam process
                scalar (cern.accsoft.commons.value.ImmutableScalar): new parameter value (or delta)
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.factory.ContextSettingsBuilder.addScalar`
        
        
        """
        ...
    @typing.overload
    def addScalar(self, parameter: cern.lsa.domain.settings.Parameter, drivableContext: cern.lsa.domain.settings.DrivableContext, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> 'ContextSettingsBuilder': ...
    def addSetting(self, setting: cern.lsa.domain.settings.Setting) -> 'ContextSettingsBuilder':
        """
            Adds new setting.
        
            Parameters:
                setting (:class:`~cern.lsa.domain.settings.Setting`): the new setting to add
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def addValue(self, parameter: cern.lsa.domain.settings.Parameter, beamProcess: cern.lsa.domain.settings.BeamProcess, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> 'ContextSettingsBuilder':
        """
            Adds new value for given parameter and beam process. The value is expected to be "appropriate" for the given beam
            process e.g. if it is a function it is expected to have length corresponding to the length of beam process. If the beam
            process is :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getCategory` then the value is expected to be a scalar
            (or array of scalars).
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter for whcih to add the immutable value
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process the value belongs to
                value (cern.accsoft.commons.value.ImmutableValue): the new setting value
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def build(self) -> cern.lsa.domain.settings.ContextSettings:
        """
            Returns the constructed context settings
        
            Returns:
                the constructed context settings
        
        
        """
        ...
    def context(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> 'ContextSettingsBuilder':
        """
            Defines the :code:`StandAloneContext` for which to create the :class:`~cern.lsa.domain.settings.ContextSettings`.
        
            If the builder was already initialized with another context - the corresponding settings and context will be
            re-initialized with specified context.
        
            Parameters:
                context (:class:`~cern.lsa.domain.settings.StandAloneContext`): new context
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def parameterSettingMap(self, map: typing.Union[java.util.Map[str, cern.lsa.domain.settings.spi.ParameterSettingsImpl], typing.Mapping[str, cern.lsa.domain.settings.spi.ParameterSettingsImpl]]) -> 'ContextSettingsBuilder': ...
    def parameterSettings(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.spi.ParameterSettingsImpl], typing.Sequence[cern.lsa.domain.settings.spi.ParameterSettingsImpl]]) -> 'ContextSettingsBuilder': ...

class ParameterTreesRequestBuilder:
    """
    public class ParameterTreesRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder to be used when creating instances of :class:`~cern.lsa.domain.settings.ParameterTreesRequest` class. The
        typical usage is following:
    
        .. code-block: java
        
         ParameterTreesRequestBuilder builder = ParameterTreesRequestBuilder.newInstance();
         // Set search criteria
         builder.setParameterNames("HC.BLM.SR1.L/param");
         // Build the request
         ParameterTreesRequest request = builder.build();
         // Call the ParameterService passing the request.
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.settings.ParameterTreesRequest:
        """
            Creates and returns an instance of the :code:`ParameterTreesRequest`.
        
        """
        ...
    @staticmethod
    def byParameterAndHierarchyFindDependentTrees(string: str, string2: str) -> cern.lsa.domain.settings.ParameterTreesRequest: ...
    @staticmethod
    def byParameterAndHierarchyFindSourceTrees(string: str, string2: str) -> cern.lsa.domain.settings.ParameterTreesRequest: ...
    @staticmethod
    def byParameterFindDependentTrees(string: str) -> cern.lsa.domain.settings.ParameterTreesRequest: ...
    @staticmethod
    def byParameterFindSourceTrees(string: str) -> cern.lsa.domain.settings.ParameterTreesRequest: ...
    def setHierarchy(self, string: str) -> 'ParameterTreesRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParameterTreesRequest.getHierarchy`
        
        
        """
        ...
    def setParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'ParameterTreesRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParameterTreesRequest.getParameters`
        
        
        """
        ...
    def setParameterName(self, string: str) -> 'ParameterTreesRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParameterTreesRequest.getParameterNames`
        
        
        """
        ...
    def setParameterNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'ParameterTreesRequestBuilder': ...
    def setParameters(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> 'ParameterTreesRequestBuilder': ...
    def setTreeDirection(self, treeDirection: cern.lsa.domain.settings.ParameterTreesRequest.TreeDirection) -> 'ParameterTreesRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParameterTreesRequest.getTreeDirection`
        
        
        """
        ...

class ParameterTypesRequestBuilder:
    """
    public class ParameterTypesRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder to be used when creating instances of :class:`~cern.lsa.domain.settings.ParameterTypesRequest` class. The
        typical usage is following:
    
        .. code-block: java
        
         ParameterTypesRequestBuilder builder = ParameterTypesRequestBuilder.newInstance();
         // Set search criteria
         builder.setParameterTypeName("PT1");
         // Build the request 
         ParameterTypesRequest request = builder.build();
         //Call the ParameterService or ParameterTypeFinder passing the request.  
         
    
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    """
    ALL_PARAMETER_TYPES: typing.ClassVar[cern.lsa.domain.settings.ParameterTypesRequest] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.ParameterTypesRequest` ALL_PARAMETER_TYPES
    
        Request for all the parameter types
    
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.settings.ParameterTypesRequest:
        """
            Creates and returns an instance of the :code:`ParameterTypesRequest`.
        
        """
        ...
    @staticmethod
    def byParameterTypeName(string: str) -> cern.lsa.domain.settings.ParameterTypesRequest:
        """
        
            Returns:
                parameter types request for specified parameter type name
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def byParameterTypeNames(stringArray: typing.List[str]) -> cern.lsa.domain.settings.ParameterTypesRequest: ...
    @typing.overload
    @staticmethod
    def byParameterTypeNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.settings.ParameterTypesRequest: ...
    def setParameterTypeName(self, string: str) -> 'ParameterTypesRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParameterTypesRequest.getParameterTypeNames`
        
        
        """
        ...
    def setParameterTypeNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'ParameterTypesRequestBuilder': ...

class ParametersRequestBuilder:
    """
    public class ParametersRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder to be used when creating instances of :class:`~cern.lsa.domain.settings.ParametersRequest` class. The typical
        usage is following:
    
        .. code-block: java
        
         ParametersRequestBuilder builder = new ParametersRequestBuilder();
         // Set search criteria
         builder.setDeviceNames(Arrays.asList("HC.BLM.SR1.L"));
         builder.setParticleTransfer(SpsParticleTransfer.SPSRING);
         // Build the request 
         ParametersRequest request = builder.build();
         //Call the ParameterFinder or ParameterService passing the request.
         ParameterService service = ServiceLocator.getService(ParameterService.class);
         Set<Parameter> parameters = service.findParameters(request);
         
         //Alternatively, if only a single criteria is used consider using one of the static factory methods e.g.:
         import static cern.lsa.domain.settings.factory.ParametersRequestBuilder.*;
         ...
         Set<Parameter> parameters = service.findParameters(byAcceleratorZone(SpsAcceleratorZone.TT40)); 
         
    
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.settings.ParametersRequest:
        """
            Creates and returns an instance of the :code:`ParametersRequest`.
        
        """
        ...
    @staticmethod
    def byAccelerator(accelerator: cern.accsoft.commons.domain.Accelerator) -> cern.lsa.domain.settings.ParametersRequest:
        """
        
            Returns:
                parameters request for specified accelerator
        
        
        """
        ...
    @staticmethod
    def byAcceleratorZone(acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.settings.ParametersRequest:
        """
        
            Returns:
                parameters request for specified accelerator zone
        
        
        """
        ...
    @staticmethod
    def byAcceleratorZones(collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.zones.AcceleratorZone], typing.Sequence[cern.accsoft.commons.domain.zones.AcceleratorZone]]) -> cern.lsa.domain.settings.ParametersRequest: ...
    @staticmethod
    def byDevice(device: cern.lsa.domain.devices.Device) -> cern.lsa.domain.settings.ParametersRequest:
        """
        
            Returns:
                parameters request for specified device
        
        
        """
        ...
    @staticmethod
    def byDeviceName(string: str) -> cern.lsa.domain.settings.ParametersRequest:
        """
        
            Returns:
                parameters request for specified device name
        
        
        """
        ...
    @staticmethod
    def byDeviceNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.settings.ParametersRequest: ...
    @staticmethod
    def byDevices(collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.Device], typing.Sequence[cern.lsa.domain.devices.Device]]) -> cern.lsa.domain.settings.ParametersRequest: ...
    @staticmethod
    def byParameterGroup(string: str) -> cern.lsa.domain.settings.ParametersRequest:
        """
        
            Returns:
                parameters request for specified parameter group name
        
        
        """
        ...
    @staticmethod
    def byParameterGroups(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.settings.ParametersRequest: ...
    @staticmethod
    def byParameterName(string: str) -> cern.lsa.domain.settings.ParametersRequest:
        """
        
            Returns:
                parameters request for specified parameter name
        
        
        """
        ...
    @staticmethod
    def byParameterNamePattern(string: str) -> cern.lsa.domain.settings.ParametersRequest:
        """
        
            Returns:
                parameters request for specified parameter name pattern
        
        
        """
        ...
    @staticmethod
    def byParameterNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.settings.ParametersRequest: ...
    @staticmethod
    def byParameterType(string: str) -> cern.lsa.domain.settings.ParametersRequest:
        """
        
            Returns:
                parameters request for specified parameter type
        
        
        """
        ...
    @staticmethod
    def byParameterTypes(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.settings.ParametersRequest: ...
    @staticmethod
    def byParticleTransfer(particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> cern.lsa.domain.settings.ParametersRequest:
        """
        
            Returns:
                parameters request for specified particle transfer
        
        
        """
        ...
    @staticmethod
    def byParticleTransfers(collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]]) -> cern.lsa.domain.settings.ParametersRequest: ...
    @staticmethod
    def byPropertyField(propertyField: cern.lsa.domain.devices.type.PropertyField) -> cern.lsa.domain.settings.ParametersRequest:
        """
        
            Returns:
                parameters request for specified property field
        
        
        """
        ...
    @staticmethod
    def byPropertyFields(collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.type.PropertyField], typing.Sequence[cern.lsa.domain.devices.type.PropertyField]]) -> cern.lsa.domain.settings.ParametersRequest: ...
    def setAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.getAccelerator`
        
        
        """
        ...
    def setAcceleratorZone(self, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.getAcceleratorZones`
        
        
        """
        ...
    def setAcceleratorZones(self, collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.zones.AcceleratorZone], typing.Sequence[cern.accsoft.commons.domain.zones.AcceleratorZone]]) -> 'ParametersRequestBuilder': ...
    def setCritical(self, boolean: bool) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.isCritical`
        
        
        """
        ...
    def setDevice(self, device: cern.lsa.domain.devices.Device) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.getDevices`
        
        
        """
        ...
    def setDeviceName(self, string: str) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.getDeviceNames`
        
        
        """
        ...
    def setDeviceNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'ParametersRequestBuilder': ...
    def setDevices(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.Device], typing.Sequence[cern.lsa.domain.devices.Device]]) -> 'ParametersRequestBuilder': ...
    def setIncludeSignatures(self, boolean: bool) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.isIncludeSignatures`
        
        
        """
        ...
    def setLsaImplementation(self, boolean: bool) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.isLsaImplementation`
        
        
        """
        ...
    def setMultiplexed(self, boolean: bool) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.isMultiplexed`
        
        
        """
        ...
    def setParameterGroup(self, string: str) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.getParameterGroups`
        
        
        """
        ...
    def setParameterGroups(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'ParametersRequestBuilder': ...
    def setParameterName(self, string: str) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.getParameterNames`
        
        
        """
        ...
    def setParameterNamePattern(self, string: str) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.getParameterNamePattern`
        
        
        """
        ...
    def setParameterNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'ParametersRequestBuilder': ...
    def setParameterTypeName(self, string: str) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.getParameterTypeNames`
        
        
        """
        ...
    def setParameterTypeNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'ParametersRequestBuilder': ...
    def setParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.getParticleTransfers`
        
        
        """
        ...
    def setParticleTransfers(self, collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]]) -> 'ParametersRequestBuilder': ...
    def setPropertyFields(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.type.PropertyField], typing.Sequence[cern.lsa.domain.devices.type.PropertyField]]) -> 'ParametersRequestBuilder': ...
    def setPropertyName(self, string: str) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.getPropertyNames`
        
        
        """
        ...
    def setPropertyNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'ParametersRequestBuilder': ...
    def setReadable(self, boolean: bool) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.isReadable`
        
        
        """
        ...
    def setValueType(self, type: cern.accsoft.commons.value.Type) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.getValueTypes`
        
        
        """
        ...
    def setValueTypes(self, collection: typing.Union[java.util.Collection[cern.accsoft.commons.value.Type], typing.Sequence[cern.accsoft.commons.value.Type]]) -> 'ParametersRequestBuilder': ...
    def setVirtual(self, boolean: bool) -> 'ParametersRequestBuilder': ...
    def setWritable(self, boolean: bool) -> 'ParametersRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.isWritable`
        
        
        """
        ...

class SettingComparisonRequestBuilder:
    """
    public class SettingComparisonRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        **Greg: The class is under construction. Don't use it YET.**
    
    
        Builds a comparison request, :class:`~cern.lsa.domain.settings.SettingComparisonRequest`. This builder makes sure that
        the resulting comparison request is valid, by throwing `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` if
        inconsistent data is supplied. Note, though, that some checks will only be done while attempting to execute the actual
        comparison.
    
        If no parameters are provided, the comparison will be performed for all related parameters. This has two important
        implications:
    
          - No results are returned for parameters that match.
          - The flag :code:`#requestSettings` is not valid: the settings are never returned (it'd be too many)
    
    
        Usage examples:
    
        .. code-block: java
        
         SettingComparisonRequest comparisonRequest = new SettingComparisonRequestBuilder()
                 .setSourceContext(contextFinder.findCycle("LHCFAST_L7200_2009_V1"))
                 .setDestContext(contextFinder.findCycle("LHCFAST_L7200_2009_V1"))
                 .setDestTimestamp(Timestamp.valueOf("2009-07-11 09:10:48.191000000"))
                 .addParameter("logical.MSE618/K")
                 .addParameter("RBAWV.R2/KICK")
                 .addParameter("RCBCH10.L2B2/KICK")
                 .requestSettings(true)
                 .build();
         
         
    
        .. code-block: java
        
         SettingComparisonRequest comparisonRequest = new SettingComparisonRequestBuilder()
                 .setSourceArchiveVersion(myArchiveVersion1)
                 .setDestArchiveVersion(myArchiveVersion2)
                 .build();
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.settings.SettingComparisonRequest:
        """
            Builds a :class:`~cern.lsa.domain.settings.SettingComparisonRequest`, using the information supplied by the other
            methods in the builder.
        
            Returns:
                new setting comparison request instance
        
        
        """
        ...
    def setCompareAllParameters(self, boolean: bool) -> 'SettingComparisonRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.compareAllParameters`
        
        
        """
        ...
    def setDestinationBeamProcesses(self, list: java.util.List[cern.lsa.domain.settings.BeamProcess]) -> 'SettingComparisonRequestBuilder': ...
    def setDestinationSettingsSource(self, settingsSource: cern.lsa.domain.settings.SettingsSource) -> 'SettingComparisonRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getDestinationSettingsSource`
        
        
        """
        ...
    def setIgnoreFlatFunctionsLength(self, boolean: bool) -> 'SettingComparisonRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.ignoreFlatFunctionsLength`
        
        
        """
        ...
    def setParameters(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> 'SettingComparisonRequestBuilder': ...
    def setPointInDestFunction(self, int: int) -> 'SettingComparisonRequestBuilder':
        """
            Sets the flag that indicates that, instead of comparing the whole function, only the value for a specific point in time
            should be taken for the value in the destination context. This allows to compare a function parameter to a discrete one
            or to the value in an actual.
        
            Parameters:
                pointInFunction (int): specific point in the destination function at which to take the value
        
            Returns:
                this builder
        
        
        """
        ...
    def setPointInSourceFunction(self, int: int) -> 'SettingComparisonRequestBuilder':
        """
            Sets the flag that indicates that, instead of comparing the whole function, only the value for a specific point in time
            should be taken for the value in the source context. This allows to compare a function parameter to a discrete one or to
            the value in an actual.
        
            Parameters:
                pointInFunction (int): specific point in the source function at which to take the value
        
            Returns:
                this builder
        
        
        """
        ...
    def setSourceBeamProcesses(self, list: java.util.List[cern.lsa.domain.settings.BeamProcess]) -> 'SettingComparisonRequestBuilder': ...
    def setSourceSettingsSource(self, settingsSource: cern.lsa.domain.settings.SettingsSource) -> 'SettingComparisonRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getSourceSettingsSource`
        
        
        """
        ...

class StandAloneContextCloneRequestBuilder(cern.lsa.domain.commons.spi.AbstractPropertiesHolder):
    """
    public class StandAloneContextCloneRequestBuilder extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder`
    
        Builder for instances of the :class:`~cern.lsa.domain.settings.StandAloneContextCloneRequest` interface. The typical
        usage of the builder is as follows:
    
        .. code-block: java
        
         StandAloneContextCloneRequest request = new StandAloneContextCloneRequestBuilder()
              .setName(beamProcessName);
              .setSource(sourceBeamProcess);
              .setAttributes(beamProcessAttributes);
            .build();
        
         // Call the generation API
         generationService.cloneStandAloneContext(request);
         
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.settings.StandAloneContextCloneRequest: ...
    def setAttributes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.commons.Attribute], typing.Sequence[cern.lsa.domain.commons.Attribute]]) -> 'StandAloneContextCloneRequestBuilder': ...
    def setCloneName(self, string: str) -> 'StandAloneContextCloneRequestBuilder':
        """
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): desired name of the clone
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setContextCategory(self, contextCategory: cern.lsa.domain.settings.ContextCategory) -> 'StandAloneContextCloneRequestBuilder': ...
    def setDescription(self, string: str) -> 'StandAloneContextCloneRequestBuilder':
        """
        
            Parameters:
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): description of the clone
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setHistoryCutOffDate(self, instant: typing.Union[java.time.Instant, datetime.datetime]) -> 'StandAloneContextCloneRequestBuilder':
        """
        
            Parameters:
                historyCutOff (`Instant <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Instant.html?is-external=true>`): indicates if the settings of the source context should also be cloned starting at the given cut-off date
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setSource(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> 'StandAloneContextCloneRequestBuilder':
        """
        
            Parameters:
                source (:class:`~cern.lsa.domain.settings.StandAloneContext`): context, which will be taken as a patter for the created clone
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setWithHistory(self, boolean: bool) -> 'StandAloneContextCloneRequestBuilder':
        """
        
            Parameters:
                withHistory (`Boolean <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true>`): indicates if the setting of the source context should also be cloned
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def shouldCloneType(self, boolean: bool) -> 'StandAloneContextCloneRequestBuilder':
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCloneRequest.shouldCloneType`
        
        
        """
        ...

class StandAloneContextCreationRequestBuilder(cern.lsa.domain.commons.spi.AbstractPropertiesHolder):
    """
    public class StandAloneContextCreationRequestBuilder extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder`
    
        Builder for instances of the :class:`~cern.lsa.domain.settings.StandAloneContextCreationRequest` interface. The typical
        usage of the builder is as follows:
    
        .. code-block: java
        
         StandAloneContextCreationRequest request = new StandAloneContextCreationRequestBuilder()
              .setName(beamProcessName);
              .setContextType(beamProcessContextType);
              .setAttributes(beamProcessAttributes);
            .build();
            
         // Call the generation API
         generationService.createStandAloneContext(request);
         
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.settings.StandAloneContextCreationRequest: ...
    def setAttributes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.commons.Attribute], typing.Sequence[cern.lsa.domain.commons.Attribute]]) -> 'StandAloneContextCreationRequestBuilder': ...
    def setContextCategory(self, contextCategory: cern.lsa.domain.settings.ContextCategory) -> 'StandAloneContextCreationRequestBuilder':
        """
        
            Parameters:
                contextCategory (:class:`~cern.lsa.domain.settings.ContextCategory`): categorizes the context to be created
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setContextType(self, contextType: cern.lsa.domain.settings.type.ContextType) -> 'StandAloneContextCreationRequestBuilder':
        """
        
            Parameters:
                type (:class:`~cern.lsa.domain.settings.type.ContextType`): containing common characteristics of the created context
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setDescription(self, string: str) -> 'StandAloneContextCreationRequestBuilder':
        """
        
            Parameters:
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): description of the context
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setLength(self, integer: int) -> 'StandAloneContextCreationRequestBuilder':
        """
        
            Parameters:
                length (`Integer <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Integer.html?is-external=true>`): length of the context in ms
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setMultiplexed(self, boolean: bool) -> 'StandAloneContextCreationRequestBuilder':
        """
        
            Parameters:
                multipexity (boolean): multiplexity of the context
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setName(self, string: str) -> 'StandAloneContextCreationRequestBuilder':
        """
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): desired name of the new context
        
            Returns:
                this instance for chaining
        
        
        """
        ...

class TrimRequestBuilder:
    """
    public class TrimRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder for instances of the :class:`~cern.lsa.domain.settings.TrimRequest` interface. The typical usage of the builder
        is following:
    
        .. code-block: java
        
         TrimRequestBuilder builder = TrimRequestBuilder.newInstance();
         builder.setContext(myCycle);
         builder.addFunction(myParam, myFunction);
         builder.addScalar(myParam2, myScalar);
         builder.setDescription("A test trim"); // Trim comment
         TrimRequest request = builder.build();
         // Call the trim API
         trimService.trimSetting(request);
         
        With the :code:`TrimRequest` one can also control whether settings should be sent to hardware (in case the context is
        resident), what setting part or hierarchy should be while trimming parameter settings, and many other features.
    
        In order to simulate a trim that won't be persisted in the database or sent to the hardware, both properties should be
        set to false:
    
        .. code-block: java
        
         builder.setPersistSettings(false); // Don't save settings in the database
         builder.setDrive(false); // Don't send settings to the hardware
         
    
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, trimRequest: cern.lsa.domain.settings.TrimRequest): ...
    def addCustomSettingPart(self, parameter: cern.lsa.domain.settings.Parameter, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'TrimRequestBuilder':
        """
            Adds a custom setting part to be used for updating parameter settings in the trim for a specific parameter.
        
            By default the custom map containing these custom setting parts is null.
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getCustomSettingPart`
        
        
        """
        ...
    def addFunction(self, parameter: cern.lsa.domain.settings.Parameter, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> 'TrimRequestBuilder':
        """
            Adds new (trim) function value for given parameter. The function is expected to have X coordinates within the
            :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.getContext`.
        
            Given function is cut into segments corresponding to intersected beam process.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter to be trimmed
                function (cern.accsoft.commons.value.ImmutableDiscreteFunction): new parameter value
        
            Returns:
                this instance for chaining
        
            Raises:
                : if either parameter or function is :code:`null` or if the function can't be mapped to any beam process from the given
                    context e.g. if the cycle is from 0 to 1000 but the function starts at X=2000
        
        
        """
        ...
    def addFunctionsArray(self, parameter: cern.lsa.domain.settings.Parameter, immutableDiscreteFunctionsArray: cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray) -> 'TrimRequestBuilder':
        """
            Adds new (trim) functionsArray value for given parameter. The functions within the functions array are expected to have
            X coordinates within the :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.getContext`.
        
            Given functionsArray is cut into segments corresponding to intersected beam process.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter to be trimmed
                functionsArray (cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray): new parameter value
        
            Returns:
                this instance for chaining
        
            Raises:
                : if either parameter or functionsArray is :code:`null` or if the functionsArray can't be mapped to any beam process from
                    the given context e.g. if the cycle is from 0 to 1000 but the function starts at X=2000
        
        
        """
        ...
    @typing.overload
    def addScalar(self, parameter: cern.lsa.domain.settings.Parameter, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> 'TrimRequestBuilder':
        """
            Adds scalar value for the given parameter to the current context.
        
            Note that this method can be used in case of :class:`~cern.lsa.domain.settings.StandAloneBeamProcess` and
            :class:`~cern.lsa.domain.settings.StandAloneCycle`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the trimmed parameter
                scalar (cern.accsoft.commons.value.ImmutableScalar): new parameter value (or delta)
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addScalar`
        
            Adds new (trim) scalar value for given parameter and context.
        
            The method searches for all compatible beam processes with given parameter that intersect with specified drivable
            context. If there is more than one beam process matching, the method adds scalar to the first matching beam process with
            preference for beam-in (and discrete) i.e. if the first beam process is beam-out and then there are few beam-in beam
            processes - the method will add value to the first beam-in. If there are only beam-out beam processes, the method will
            add the value to the first beam-out.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the trimmed parameter
                ctx (:class:`~cern.lsa.domain.settings.DrivableContext`): drivable context for which the scalar should be used: cycle or beam process
                scalar (cern.accsoft.commons.value.ImmutableScalar): new parameter value (or delta)
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addScalar`
        
        
        """
        ...
    @typing.overload
    def addScalar(self, parameter: cern.lsa.domain.settings.Parameter, drivableContext: cern.lsa.domain.settings.DrivableContext, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> 'TrimRequestBuilder': ...
    def addSetting(self, setting: cern.lsa.domain.settings.Setting) -> 'TrimRequestBuilder':
        """
            Adds new (trim) setting.
        
            Parameters:
                setting (:class:`~cern.lsa.domain.settings.Setting`): the setting to add to the trim request
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def addValue(self, parameter: cern.lsa.domain.settings.Parameter, beamProcess: cern.lsa.domain.settings.BeamProcess, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> 'TrimRequestBuilder':
        """
            Adds new (trim) value for given parameter and beam process. The value is expected to be "appropriate" for the given beam
            process e.g. if it is a function it is expected to have length corresponding to the length of beam process. If the beam
            process is :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getCategory` then the value is expected to be a scalar
            (or array of scalars).
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): trimmed parameter
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): trimmed beam process
                value (cern.accsoft.commons.value.ImmutableValue): the new setting value
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def build(self) -> cern.lsa.domain.settings.TrimRequest:
        """
            An alias method for :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.newTrimRequest`.
        
            Returns:
                a new instance of :code:`TrimRequest`
        
        
        """
        ...
    def newTrimRequest(self) -> cern.lsa.domain.settings.TrimRequest:
        """
            Creates a new instance of :code:`TrimRequest`.
        
            Returns:
                a new instance of :code:`TrimRequest`
        
        
        """
        ...
    def setAttribute(self, string: str, object: typing.Any) -> 'TrimRequestBuilder':
        """
            Sets custom attribute for the request.
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the attribute
                attrValue (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): attribute value (can be :code:`null`)
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getAttribute`
        
        
        """
        ...
    def setChildSettingPart(self, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'TrimRequestBuilder':
        """
            Sets a setting part to be used for updating child parameter settings in the trim.
        
            By default this property is set to :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET`.
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getChildSettingPart`
        
        
        """
        ...
    def setCommit(self, boolean: bool) -> 'TrimRequestBuilder':
        """
            Default value of this property is :code:`true`.
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isCommit`
        
        
        """
        ...
    def setContext(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> 'TrimRequestBuilder':
        """
            Defines the :code:`StandAloneContext` that should be used for the trim.
        
            If the builder was already initialized with another context or context settings - the corresponding context settings and
            context will be re-initialized with specified context.
        
            Parameters:
                context (:class:`~cern.lsa.domain.settings.StandAloneContext`): new context
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.getContext`
        
        
        """
        ...
    def setContextSettings(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> 'TrimRequestBuilder':
        """
            Sets :code:`ContextSettings` containing trim values.
        
            Parameters:
                contextSettings (:class:`~cern.lsa.domain.settings.ContextSettings`): a non-null contextSettings to set
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setCustomSettingPartMap(self, map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.SettingPartEnum], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.SettingPartEnum]]) -> 'TrimRequestBuilder': ...
    def setDescription(self, string: str) -> 'TrimRequestBuilder':
        """
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getDescription`
        
        
        """
        ...
    def setDrive(self, boolean: bool) -> 'TrimRequestBuilder':
        """
            Default value of this property is :code:`true`.
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isDrive`
        
        
        """
        ...
    def setForceDrive(self, boolean: bool) -> 'TrimRequestBuilder':
        """
            Default value of this property is :code:`false`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isForceDrive`
        
        
        """
        ...
    def setForceProcessing(self, boolean: bool) -> 'TrimRequestBuilder':
        """
            Default value of this property is :code:`false`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isForceProcessing`
        
        
        """
        ...
    def setIgnoreErrors(self, boolean: bool) -> 'TrimRequestBuilder':
        """
            Default value of this property is :code:`false`.
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isIgnoreErrors`
        
        
        """
        ...
    def setLenientDrive(self, boolean: bool) -> 'TrimRequestBuilder':
        """
            Default value of this property is :code:`false`.
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isLenientDrive`
        
        
        """
        ...
    def setParameters(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> 'TrimRequestBuilder': ...
    def setPersistSettings(self, boolean: bool) -> 'TrimRequestBuilder':
        """
            Default value of this property is :code:`true`.
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isPersistSettings`
        
        
        """
        ...
    def setPropagateToChildren(self, boolean: bool) -> 'TrimRequestBuilder':
        """
            Default value of this property is :code:`true`.
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isPropagateToChildren`
        
        
        """
        ...
    def setRelative(self, boolean: bool) -> 'TrimRequestBuilder':
        """
            Default value of this property is :code:`false`.
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isRelative`
        
        
        """
        ...
    def setReturnSettings(self, boolean: bool) -> 'TrimRequestBuilder':
        """
            Default value of this property is :code:`true`.
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isReturnSettings`
        
        
        """
        ...
    def setSettingPart(self, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'TrimRequestBuilder':
        """
            Sets a setting part to be used for the trim.
        
            By default this property is set to :meth:`~cern.lsa.domain.settings.SettingPartEnum.VALUE`.
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getSettingPart`
        
        
        """
        ...
    def setSkipProcessing(self, boolean: bool) -> 'TrimRequestBuilder':
        """
            Default value of this property is :code:`false`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isSkipProcessing`
        
        
        """
        ...
    def setTransactionId(self, int: int) -> 'TrimRequestBuilder':
        """
            Sets a custom transaction ID to drive the settings. If :code:`null` (default value), one is generated internally if
            required.
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getTransactionId`
        
        
        """
        ...

class CopySettingsRequestBuilder(TrimRequestBuilder):
    """
    public class CopySettingsRequestBuilder extends :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
    
        Builder for instances of the :class:`~cern.lsa.domain.settings.CopySettingsRequest` interface. It extends
        :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder` to provide some additional fields. The typical usage of
        the builder is following:
    
        .. code-block: java
        
         CopySettingsRequestBuilder<StandAloneCycle> builder = CopySettingsRequestBuilder.newInstance();
         builder.setContext(standAloneContext);
         builder.setParameters(parameters);
         builder.setDescription("A test copy"); // Trim comment
         builder.setSettingsSource(mySettingsSource);
         builder.setSourceContexts(mySourceContexts);
         builder.setDestinationContexts(myDestinationContexts);
         CopySettingsRequest<StandAloneCycle> request = builder.build();
         // Call the revert trim API
         trimService.copySettings(request);
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, copySettingsRequest: cern.lsa.domain.settings.CopySettingsRequest): ...
    @typing.overload
    def __init__(self, trimRequest: cern.lsa.domain.settings.TrimRequest): ...
    def addCustomSettingPart(self, parameter: cern.lsa.domain.settings.Parameter, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addCustomSettingPart`
            Adds a custom setting part to be used for updating parameter settings in the trim for a specific parameter.
        
            By default the custom map containing these custom setting parts is null.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addCustomSettingPart`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getCustomSettingPart`
        
        
        """
        ...
    def addFunction(self, parameter: cern.lsa.domain.settings.Parameter, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addFunction`
            Adds new (trim) function value for given parameter. The function is expected to have X coordinates within the
            :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.getContext`.
        
            Given function is cut into segments corresponding to intersected beam process.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addFunction`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter to be trimmed
                function (cern.accsoft.commons.value.ImmutableDiscreteFunction): new parameter value
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def addFunctionsArray(self, parameter: cern.lsa.domain.settings.Parameter, immutableDiscreteFunctionsArray: cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addFunctionsArray`
            Adds new (trim) functionsArray value for given parameter. The functions within the functions array are expected to have
            X coordinates within the :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.getContext`.
        
            Given functionsArray is cut into segments corresponding to intersected beam process.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addFunctionsArray`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter to be trimmed
                functionsArray (cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray): new parameter value
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    @typing.overload
    def addScalar(self, parameter: cern.lsa.domain.settings.Parameter, drivableContext: cern.lsa.domain.settings.DrivableContext, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addScalar`
            Adds new (trim) scalar value for given parameter and context.
        
            The method searches for all compatible beam processes with given parameter that intersect with specified drivable
            context. If there is more than one beam process matching, the method adds scalar to the first matching beam process with
            preference for beam-in (and discrete) i.e. if the first beam process is beam-out and then there are few beam-in beam
            processes - the method will add value to the first beam-in. If there are only beam-out beam processes, the method will
            add the value to the first beam-out.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addScalar`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the trimmed parameter
                ctx (:class:`~cern.lsa.domain.settings.DrivableContext`): drivable context for which the scalar should be used: cycle or beam process
                scalar (cern.accsoft.commons.value.ImmutableScalar): new parameter value (or delta)
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addScalar`
        
        
        """
        ...
    @typing.overload
    def addScalar(self, parameter: cern.lsa.domain.settings.Parameter, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> TrimRequestBuilder: ...
    def addSetting(self, setting: cern.lsa.domain.settings.Setting) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addSetting`
            Adds new (trim) setting.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addSetting`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                setting (:class:`~cern.lsa.domain.settings.Setting`): the setting to add to the trim request
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def addValue(self, parameter: cern.lsa.domain.settings.Parameter, beamProcess: cern.lsa.domain.settings.BeamProcess, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addValue`
            Adds new (trim) value for given parameter and beam process. The value is expected to be "appropriate" for the given beam
            process e.g. if it is a function it is expected to have length corresponding to the length of beam process. If the beam
            process is :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getCategory` then the value is expected to be a scalar
            (or array of scalars).
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): trimmed parameter
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): trimmed beam process
                value (cern.accsoft.commons.value.ImmutableValue): the new setting value
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def build(self) -> cern.lsa.domain.settings.CopySettingsRequest:
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.build`
            An alias method for :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.newTrimRequest`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.build`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                a new instance of :code:`TrimRequest`
        
        
        """
        ...
    def setAttribute(self, string: str, object: typing.Any) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setAttribute`
            Sets custom attribute for the request.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setAttribute`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the attribute
                attrValue (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): attribute value (can be :code:`null`)
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getAttribute`
        
        
        """
        ...
    def setChildSettingPart(self, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setChildSettingPart`
            Sets a setting part to be used for updating child parameter settings in the trim.
        
            By default this property is set to :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setChildSettingPart`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getChildSettingPart`
        
        
        """
        ...
    def setContext(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContext`
            Defines the :code:`StandAloneContext` that should be used for the trim.
        
            If the builder was already initialized with another context or context settings - the corresponding context settings and
            context will be re-initialized with specified context.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContext`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                context (:class:`~cern.lsa.domain.settings.StandAloneContext`): new context
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.getContext`
        
        
        """
        ...
    def setContextSettings(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContextSettings`
            Sets :code:`ContextSettings` containing trim values.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContextSettings`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                contextSettings (:class:`~cern.lsa.domain.settings.ContextSettings`): a non-null contextSettings to set
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setCustomSettingPartMap(self, map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.SettingPartEnum], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.SettingPartEnum]]) -> 'CopySettingsRequestBuilder': ...
    def setDescription(self, string: str) -> 'CopySettingsRequestBuilder':
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDescription`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getDescription`
        
        
        """
        ...
    def setDestinationContexts(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Context], typing.Sequence[cern.lsa.domain.settings.Context]]) -> 'CopySettingsRequestBuilder': ...
    def setDestinationParameters(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> 'CopySettingsRequestBuilder': ...
    def setDrive(self, boolean: bool) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDrive`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDrive`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isDrive`
        
        
        """
        ...
    def setForceDrive(self, boolean: bool) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setForceDrive`
            Default value of this property is :code:`false`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setForceDrive`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isForceDrive`
        
        
        """
        ...
    def setForceProcessing(self, boolean: bool) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setForceProcessing`
            Default value of this property is :code:`false`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setForceProcessing`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isForceProcessing`
        
        
        """
        ...
    def setIgnoreErrors(self, boolean: bool) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setIgnoreErrors`
            Default value of this property is :code:`false`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setIgnoreErrors`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isIgnoreErrors`
        
        
        """
        ...
    def setLenientDrive(self, boolean: bool) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setLenientDrive`
            Default value of this property is :code:`false`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setLenientDrive`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isLenientDrive`
        
        
        """
        ...
    def setParameters(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> 'CopySettingsRequestBuilder': ...
    def setPersistSettings(self, boolean: bool) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPersistSettings`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPersistSettings`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isPersistSettings`
        
        
        """
        ...
    def setPropagateToChildren(self, boolean: bool) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPropagateToChildren`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPropagateToChildren`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isPropagateToChildren`
        
        
        """
        ...
    def setRelative(self, boolean: bool) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setRelative`
            Default value of this property is :code:`false`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setRelative`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isRelative`
        
        
        """
        ...
    def setReturnSettings(self, boolean: bool) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setReturnSettings`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setReturnSettings`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isReturnSettings`
        
        
        """
        ...
    def setSettingPart(self, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setSettingPart`
            Sets a setting part to be used for the trim.
        
            By default this property is set to :meth:`~cern.lsa.domain.settings.SettingPartEnum.VALUE`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setSettingPart`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getSettingPart`
        
        
        """
        ...
    def setSettingsSource(self, settingsSource: cern.lsa.domain.settings.SettingsSource) -> 'CopySettingsRequestBuilder':
        """
        
            Parameters:
                settingsSource (:class:`~cern.lsa.domain.settings.SettingsSource`): 
            Returns:
                this builder for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.CopySettingsRequest.getSettingsSource`
        
        
        """
        ...
    def setSkipProcessing(self, boolean: bool) -> 'CopySettingsRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setSkipProcessing`
            Default value of this property is :code:`false`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setSkipProcessing`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isSkipProcessing`
        
        
        """
        ...
    def setSourceContexts(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Context], typing.Sequence[cern.lsa.domain.settings.Context]]) -> 'CopySettingsRequestBuilder': ...

class IncorporationRequestBuilder(TrimRequestBuilder):
    """
    public class IncorporationRequestBuilder extends :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
    
        Builder for instances of the :class:`~cern.lsa.domain.settings.IncorporationRequest` interface. It extends
        :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder` to provide some additional fields. The typical usage of
        the builder is following:
    
        .. code-block: java
        
         IncorporationRequestBuilder builder = IncorporationRequestBuilder.newInstance();
         builder.setContext(destBeamProcess);
         builder.setDescription("Incorporated from " + sourceBeamProcess.getName());
         builder.addIncorporationSetting(incorporationSetting);
         IncorporationRequest request = builder.build();
         // Call the incorporate API
         trimService.incorporate(request);
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, incorporationRequest: cern.lsa.domain.settings.IncorporationRequest): ...
    def addCustomSettingPart(self, parameter: cern.lsa.domain.settings.Parameter, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addCustomSettingPart`
            Adds a custom setting part to be used for updating parameter settings in the trim for a specific parameter.
        
            By default the custom map containing these custom setting parts is null.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addCustomSettingPart`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getCustomSettingPart`
        
        
        """
        ...
    def addFunction(self, parameter: cern.lsa.domain.settings.Parameter, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addFunction`
            Adds new (trim) function value for given parameter. The function is expected to have X coordinates within the
            :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.getContext`.
        
            Given function is cut into segments corresponding to intersected beam process.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addFunction`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter to be trimmed
                function (cern.accsoft.commons.value.ImmutableDiscreteFunction): new parameter value
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def addFunctionsArray(self, parameter: cern.lsa.domain.settings.Parameter, immutableDiscreteFunctionsArray: cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addFunctionsArray`
            Adds new (trim) functionsArray value for given parameter. The functions within the functions array are expected to have
            X coordinates within the :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.getContext`.
        
            Given functionsArray is cut into segments corresponding to intersected beam process.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addFunctionsArray`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter to be trimmed
                functionsArray (cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray): new parameter value
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def addIncorporationSetting(self, incorporationSetting: cern.lsa.domain.settings.IncorporationSetting) -> 'IncorporationRequestBuilder':
        """
        
            Parameters:
                newIncorporationSetting (:class:`~cern.lsa.domain.settings.IncorporationSetting`): the incorporation setting that will be added
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    @typing.overload
    def addScalar(self, parameter: cern.lsa.domain.settings.Parameter, drivableContext: cern.lsa.domain.settings.DrivableContext, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addScalar`
            Adds new (trim) scalar value for given parameter and context.
        
            The method searches for all compatible beam processes with given parameter that intersect with specified drivable
            context. If there is more than one beam process matching, the method adds scalar to the first matching beam process with
            preference for beam-in (and discrete) i.e. if the first beam process is beam-out and then there are few beam-in beam
            processes - the method will add value to the first beam-in. If there are only beam-out beam processes, the method will
            add the value to the first beam-out.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addScalar`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the trimmed parameter
                ctx (:class:`~cern.lsa.domain.settings.DrivableContext`): drivable context for which the scalar should be used: cycle or beam process
                scalar (cern.accsoft.commons.value.ImmutableScalar): new parameter value (or delta)
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addScalar`
        
        
        """
        ...
    @typing.overload
    def addScalar(self, parameter: cern.lsa.domain.settings.Parameter, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> TrimRequestBuilder: ...
    def addSetting(self, setting: cern.lsa.domain.settings.Setting) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addSetting`
            Adds new (trim) setting.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addSetting`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                setting (:class:`~cern.lsa.domain.settings.Setting`): the setting to add to the trim request
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def addValue(self, parameter: cern.lsa.domain.settings.Parameter, beamProcess: cern.lsa.domain.settings.BeamProcess, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addValue`
            Adds new (trim) value for given parameter and beam process. The value is expected to be "appropriate" for the given beam
            process e.g. if it is a function it is expected to have length corresponding to the length of beam process. If the beam
            process is :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getCategory` then the value is expected to be a scalar
            (or array of scalars).
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): trimmed parameter
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): trimmed beam process
                value (cern.accsoft.commons.value.ImmutableValue): the new setting value
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def build(self) -> cern.lsa.domain.settings.IncorporationRequest:
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.build`
            An alias method for :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.newTrimRequest`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.build`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                a new instance of :code:`TrimRequest`
        
        
        """
        ...
    def setAttribute(self, string: str, object: typing.Any) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setAttribute`
            Sets custom attribute for the request.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setAttribute`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the attribute
                attrValue (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): attribute value (can be :code:`null`)
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getAttribute`
        
        
        """
        ...
    def setChildSettingPart(self, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setChildSettingPart`
            Sets a setting part to be used for updating child parameter settings in the trim.
        
            By default this property is set to :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setChildSettingPart`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getChildSettingPart`
        
        
        """
        ...
    def setContext(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContext`
            Defines the :code:`StandAloneContext` that should be used for the trim.
        
            If the builder was already initialized with another context or context settings - the corresponding context settings and
            context will be re-initialized with specified context.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContext`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                context (:class:`~cern.lsa.domain.settings.StandAloneContext`): new context
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.getContext`
        
        
        """
        ...
    def setContextSettings(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContextSettings`
            Sets :code:`ContextSettings` containing trim values.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContextSettings`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                contextSettings (:class:`~cern.lsa.domain.settings.ContextSettings`): a non-null contextSettings to set
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setCustomSettingPartMap(self, map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.SettingPartEnum], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.SettingPartEnum]]) -> 'IncorporationRequestBuilder': ...
    def setDescription(self, string: str) -> 'IncorporationRequestBuilder':
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDescription`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getDescription`
        
        
        """
        ...
    def setDrive(self, boolean: bool) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDrive`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDrive`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isDrive`
        
        
        """
        ...
    def setForceDrive(self, boolean: bool) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setForceDrive`
            Default value of this property is :code:`false`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setForceDrive`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isForceDrive`
        
        
        """
        ...
    def setForceProcessing(self, boolean: bool) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setForceProcessing`
            Default value of this property is :code:`false`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setForceProcessing`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isForceProcessing`
        
        
        """
        ...
    def setIgnoreErrors(self, boolean: bool) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setIgnoreErrors`
            Default value of this property is :code:`false`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setIgnoreErrors`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isIgnoreErrors`
        
        
        """
        ...
    def setIncorporationSettings(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.IncorporationSetting], typing.Sequence[cern.lsa.domain.settings.IncorporationSetting]]) -> 'IncorporationRequestBuilder': ...
    def setLenientDrive(self, boolean: bool) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setLenientDrive`
            Default value of this property is :code:`false`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setLenientDrive`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isLenientDrive`
        
        
        """
        ...
    def setParameters(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> 'IncorporationRequestBuilder': ...
    def setPersistSettings(self, boolean: bool) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPersistSettings`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPersistSettings`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isPersistSettings`
        
        
        """
        ...
    def setPropagateToChildren(self, boolean: bool) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPropagateToChildren`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPropagateToChildren`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isPropagateToChildren`
        
        
        """
        ...
    def setRelative(self, boolean: bool) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setRelative`
            Default value of this property is :code:`false`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setRelative`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isRelative`
        
        
        """
        ...
    def setReturnSettings(self, boolean: bool) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setReturnSettings`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setReturnSettings`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isReturnSettings`
        
        
        """
        ...
    def setSettingPart(self, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setSettingPart`
            Sets a setting part to be used for the trim.
        
            By default this property is set to :meth:`~cern.lsa.domain.settings.SettingPartEnum.VALUE`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setSettingPart`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getSettingPart`
        
        
        """
        ...
    def setSkipProcessing(self, boolean: bool) -> 'IncorporationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setSkipProcessing`
            Default value of this property is :code:`false`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setSkipProcessing`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isSkipProcessing`
        
        
        """
        ...

class KnobCreationBuilder(AbstractKnobBuilder['KnobCreationBuilder']):
    """
    public class KnobCreationBuilder extends :class:`~cern.lsa.domain.settings.factory.AbstractKnobBuilder`<:class:`~cern.lsa.domain.settings.factory.KnobCreationBuilder`>
    
        Builder for new :class:`~cern.lsa.domain.settings.Knob`s.
    
        It can be used for to create a new :class:`~cern.lsa.domain.settings.Knob` from scratch or basing on an existing one.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, knob: cern.lsa.domain.settings.Knob): ...
    def setKnobParameterName(self, string: str) -> 'KnobCreationBuilder': ...
    def setKnobParameterType(self, parameterType: cern.lsa.domain.settings.ParameterType) -> 'KnobCreationBuilder': ...
    def setMultiplexed(self, boolean: bool) -> 'KnobCreationBuilder': ...
    def setValueType(self, type: cern.accsoft.commons.value.Type) -> 'KnobCreationBuilder': ...

class KnobModificationBuilder(AbstractKnobBuilder['KnobModificationBuilder']):
    """
    public class KnobModificationBuilder extends :class:`~cern.lsa.domain.settings.factory.AbstractKnobBuilder`<:class:`~cern.lsa.domain.settings.factory.KnobModificationBuilder`>
    
        Builder used to modify existing :class:`~cern.lsa.domain.settings.Knob`.
    """
    def __init__(self, knob: cern.lsa.domain.settings.Knob): ...

class RevertTrimRequestBuilder(TrimRequestBuilder):
    """
    public class RevertTrimRequestBuilder extends :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
    
        Builder for instances of the :class:`~cern.lsa.domain.settings.RevertTrimRequest` interface. It extends
        :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder` to provide some additional fields. The typical usage of
        the builder is following:
    
        .. code-block: java
        
         RevertTrimRequestBuilder<StandAloneCycle> builder = RevertTrimRequestBuilder.newInstance();
         builder.setContext(standAloneContext);
         builder.setParameters(parameters);
         builder.setDescription("A test trim"); // Trim comment
         builder.setTrimHeader(myTrimHeader);
         builder.setBeamProcesses(myBeamProcesses);
         RevertTrimRequest<StandAloneCycle> request = builder.build();
         // Call the revert trim API
         trimService.revertTrim(request);
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, revertTrimRequest: cern.lsa.domain.settings.RevertTrimRequest): ...
    @typing.overload
    def __init__(self, trimRequest: cern.lsa.domain.settings.TrimRequest): ...
    def addCustomSettingPart(self, parameter: cern.lsa.domain.settings.Parameter, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addCustomSettingPart`
            Adds a custom setting part to be used for updating parameter settings in the trim for a specific parameter.
        
            By default the custom map containing these custom setting parts is null.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addCustomSettingPart`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getCustomSettingPart`
        
        
        """
        ...
    def addFunction(self, parameter: cern.lsa.domain.settings.Parameter, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addFunction`
            Adds new (trim) function value for given parameter. The function is expected to have X coordinates within the
            :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.getContext`.
        
            Given function is cut into segments corresponding to intersected beam process.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addFunction`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter to be trimmed
                function (cern.accsoft.commons.value.ImmutableDiscreteFunction): new parameter value
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def addFunctionsArray(self, parameter: cern.lsa.domain.settings.Parameter, immutableDiscreteFunctionsArray: cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addFunctionsArray`
            Adds new (trim) functionsArray value for given parameter. The functions within the functions array are expected to have
            X coordinates within the :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.getContext`.
        
            Given functionsArray is cut into segments corresponding to intersected beam process.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addFunctionsArray`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter to be trimmed
                functionsArray (cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray): new parameter value
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    @typing.overload
    def addScalar(self, parameter: cern.lsa.domain.settings.Parameter, drivableContext: cern.lsa.domain.settings.DrivableContext, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addScalar`
            Adds new (trim) scalar value for given parameter and context.
        
            The method searches for all compatible beam processes with given parameter that intersect with specified drivable
            context. If there is more than one beam process matching, the method adds scalar to the first matching beam process with
            preference for beam-in (and discrete) i.e. if the first beam process is beam-out and then there are few beam-in beam
            processes - the method will add value to the first beam-in. If there are only beam-out beam processes, the method will
            add the value to the first beam-out.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addScalar`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the trimmed parameter
                ctx (:class:`~cern.lsa.domain.settings.DrivableContext`): drivable context for which the scalar should be used: cycle or beam process
                scalar (cern.accsoft.commons.value.ImmutableScalar): new parameter value (or delta)
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addScalar`
        
        
        """
        ...
    @typing.overload
    def addScalar(self, parameter: cern.lsa.domain.settings.Parameter, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> TrimRequestBuilder: ...
    def addSetting(self, setting: cern.lsa.domain.settings.Setting) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addSetting`
            Adds new (trim) setting.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addSetting`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                setting (:class:`~cern.lsa.domain.settings.Setting`): the setting to add to the trim request
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def addValue(self, parameter: cern.lsa.domain.settings.Parameter, beamProcess: cern.lsa.domain.settings.BeamProcess, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addValue`
            Adds new (trim) value for given parameter and beam process. The value is expected to be "appropriate" for the given beam
            process e.g. if it is a function it is expected to have length corresponding to the length of beam process. If the beam
            process is :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getCategory` then the value is expected to be a scalar
            (or array of scalars).
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.addValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): trimmed parameter
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): trimmed beam process
                value (cern.accsoft.commons.value.ImmutableValue): the new setting value
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def build(self) -> cern.lsa.domain.settings.RevertTrimRequest:
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.build`
            An alias method for :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.newTrimRequest`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.build`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                a new instance of :code:`TrimRequest`
        
        
        """
        ...
    def setAttribute(self, string: str, object: typing.Any) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setAttribute`
            Sets custom attribute for the request.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setAttribute`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the attribute
                attrValue (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): attribute value (can be :code:`null`)
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getAttribute`
        
        
        """
        ...
    def setBeamProcesses(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.BeamProcess], typing.Sequence[cern.lsa.domain.settings.BeamProcess]]) -> 'RevertTrimRequestBuilder': ...
    def setChildSettingPart(self, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setChildSettingPart`
            Sets a setting part to be used for updating child parameter settings in the trim.
        
            By default this property is set to :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setChildSettingPart`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getChildSettingPart`
        
        
        """
        ...
    def setContext(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContext`
            Defines the :code:`StandAloneContext` that should be used for the trim.
        
            If the builder was already initialized with another context or context settings - the corresponding context settings and
            context will be re-initialized with specified context.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContext`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                context (:class:`~cern.lsa.domain.settings.StandAloneContext`): new context
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.getContext`
        
        
        """
        ...
    def setContextSettings(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContextSettings`
            Sets :code:`ContextSettings` containing trim values.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContextSettings`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                contextSettings (:class:`~cern.lsa.domain.settings.ContextSettings`): a non-null contextSettings to set
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setCustomSettingPartMap(self, map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.SettingPartEnum], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.SettingPartEnum]]) -> 'RevertTrimRequestBuilder': ...
    def setDescription(self, string: str) -> 'RevertTrimRequestBuilder':
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDescription`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getDescription`
        
        
        """
        ...
    def setDrive(self, boolean: bool) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDrive`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDrive`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isDrive`
        
        
        """
        ...
    def setForceDrive(self, boolean: bool) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setForceDrive`
            Default value of this property is :code:`false`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setForceDrive`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isForceDrive`
        
        
        """
        ...
    def setForceProcessing(self, boolean: bool) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setForceProcessing`
            Default value of this property is :code:`false`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setForceProcessing`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isForceProcessing`
        
        
        """
        ...
    def setIgnoreErrors(self, boolean: bool) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setIgnoreErrors`
            Default value of this property is :code:`false`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setIgnoreErrors`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isIgnoreErrors`
        
        
        """
        ...
    def setLenientDrive(self, boolean: bool) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setLenientDrive`
            Default value of this property is :code:`false`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setLenientDrive`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isLenientDrive`
        
        
        """
        ...
    def setParameters(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> 'RevertTrimRequestBuilder': ...
    def setPersistSettings(self, boolean: bool) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPersistSettings`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPersistSettings`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isPersistSettings`
        
        
        """
        ...
    def setPropagateToChildren(self, boolean: bool) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPropagateToChildren`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPropagateToChildren`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isPropagateToChildren`
        
        
        """
        ...
    def setRelative(self, boolean: bool) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setRelative`
            Default value of this property is :code:`false`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setRelative`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isRelative`
        
        
        """
        ...
    def setReturnSettings(self, boolean: bool) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setReturnSettings`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setReturnSettings`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isReturnSettings`
        
        
        """
        ...
    def setSettingPart(self, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setSettingPart`
            Sets a setting part to be used for the trim.
        
            By default this property is set to :meth:`~cern.lsa.domain.settings.SettingPartEnum.VALUE`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setSettingPart`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getSettingPart`
        
        
        """
        ...
    def setSkipProcessing(self, boolean: bool) -> 'RevertTrimRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setSkipProcessing`
            Default value of this property is :code:`false`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setSkipProcessing`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isSkipProcessing`
        
        
        """
        ...
    def setTrimHeader(self, trimHeader: cern.lsa.domain.settings.TrimHeader) -> 'RevertTrimRequestBuilder':
        """
        
            Parameters:
                trimHeader (:class:`~cern.lsa.domain.settings.TrimHeader`): the trim herder that should be used
        
            Returns:
                this builder for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.RevertTrimRequest.getTrimHeader`
        
        
        """
        ...

class SettingsGenerationRequestBuilder(TrimRequestBuilder):
    """
    public class SettingsGenerationRequestBuilder extends :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
    
        Builder for instances of the :class:`~cern.lsa.domain.settings.SettingsGenerationRequest` interface. The typical usage
        of the builder is following:
    
        .. code-block: java
        
         SettingsGenerationRequestBuilder builder = SettingsGenerationRequestBuilder.newInstance();
         builder.setContext(myCycle);
         builder.setParameters(parametersToGenerate)
         
         // Call the generation API
         generationService.generateSettings(builder.build());
         
        With the :code:`SettingsGenerationRequest` one can also control whether settings should be sent to hardware (in case the
        context is resident), what setting part or hierarchy should be while trimming parameter settings, and many other
        features. For instance in order to generate ZERO settings and not propagate the trim to dependent parameters the
        following two properties should be set:
    
        .. code-block: java
        
         builder.setPropagateToChildren(false);
         builder.setGenerateZeroSettings(true);
         
        Note that by default the builder initializes the following properties with values different than the
        :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`:
    
          - :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setSettingPart` -
            :meth:`~cern.lsa.domain.settings.SettingPartEnum.UPDATE_TARGET_NO_CORRECTION`
          - :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDrive` - :code:`false`
          - :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDescription` - "(Re)Generated"
    
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.settings.SettingsGenerationRequest:
        """
            Builds the request.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.build`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                a new instance of :code:`TrimRequest`
        
        
        """
        ...
    def setAttribute(self, string: str, object: typing.Any) -> 'SettingsGenerationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setAttribute`
            Sets custom attribute for the request.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setAttribute`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the attribute
                attrValue (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): attribute value (can be :code:`null`)
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getAttribute`
        
        
        """
        ...
    def setContext(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> 'SettingsGenerationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContext`
            Defines the :code:`StandAloneContext` that should be used for the trim.
        
            If the builder was already initialized with another context or context settings - the corresponding context settings and
            context will be re-initialized with specified context.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setContext`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Parameters:
                context (:class:`~cern.lsa.domain.settings.StandAloneContext`): new context
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.getContext`
        
        
        """
        ...
    def setDescription(self, string: str) -> 'SettingsGenerationRequestBuilder':
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDescription`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getDescription`
        
        
        """
        ...
    def setDrive(self, boolean: bool) -> 'SettingsGenerationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDrive`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setDrive`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isDrive`
        
        
        """
        ...
    def setGenerateZeroSettings(self, boolean: bool) -> 'SettingsGenerationRequestBuilder':
        """
            Determines whether generation shall generate zeros for the given parameters.
        
            Parameters:
                generateZeroSettings (boolean): flag that indicates whether to generate zero settings
        
            Returns:
                this builder for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingsGenerationRequest.isGenerateZeroSettings`
        
        
        """
        ...
    def setParameters(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> 'SettingsGenerationRequestBuilder': ...
    def setPersistSettings(self, boolean: bool) -> 'SettingsGenerationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPersistSettings`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPersistSettings`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isPersistSettings`
        
        
        """
        ...
    def setPropagateToChildren(self, boolean: bool) -> 'SettingsGenerationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPropagateToChildren`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setPropagateToChildren`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isPropagateToChildren`
        
        
        """
        ...
    def setReturnSettings(self, boolean: bool) -> 'SettingsGenerationRequestBuilder':
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setReturnSettings`
            Default value of this property is :code:`true`.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.factory.TrimRequestBuilder.setReturnSettings`Â in
                classÂ :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isReturnSettings`
        
        
        """
        ...
    def setSubContexts(self, set: java.util.Set[cern.lsa.domain.settings.SubContext]) -> 'SettingsGenerationRequestBuilder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.settings.factory")``.

    AbstractKnobBuilder: typing.Type[AbstractKnobBuilder]
    BeamProcessIncorporationRequestBuilder: typing.Type[BeamProcessIncorporationRequestBuilder]
    ContextSettingsBuilder: typing.Type[ContextSettingsBuilder]
    CopySettingsRequestBuilder: typing.Type[CopySettingsRequestBuilder]
    IncorporationRequestBuilder: typing.Type[IncorporationRequestBuilder]
    KnobCreationBuilder: typing.Type[KnobCreationBuilder]
    KnobModificationBuilder: typing.Type[KnobModificationBuilder]
    ParameterTreesRequestBuilder: typing.Type[ParameterTreesRequestBuilder]
    ParameterTypesRequestBuilder: typing.Type[ParameterTypesRequestBuilder]
    ParametersRequestBuilder: typing.Type[ParametersRequestBuilder]
    RevertTrimRequestBuilder: typing.Type[RevertTrimRequestBuilder]
    SettingComparisonRequestBuilder: typing.Type[SettingComparisonRequestBuilder]
    SettingsGenerationRequestBuilder: typing.Type[SettingsGenerationRequestBuilder]
    StandAloneContextCloneRequestBuilder: typing.Type[StandAloneContextCloneRequestBuilder]
    StandAloneContextCreationRequestBuilder: typing.Type[StandAloneContextCreationRequestBuilder]
    TrimRequestBuilder: typing.Type[TrimRequestBuilder]
