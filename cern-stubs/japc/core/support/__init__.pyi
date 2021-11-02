import cern.japc.core
import cern.japc.core.factory
import cern.japc.value
import java.io
import java.util
import typing



class Descriptors:
    RDA: typing.ClassVar[str] = ...
    RDA3: typing.ClassVar[str] = ...
    DEFAULT_STRING: typing.ClassVar[str] = ...
    IS_VALID: typing.ClassVar[str] = ...
    ERROR_STRING: typing.ClassVar[str] = ...
    SERVER_NAME: typing.ClassVar[str] = ...
    DEVICE_ALIAS: typing.ClassVar[str] = ...
    RESPONSIBLE: typing.ClassVar[str] = ...
    CLASS_VERSION: typing.ClassVar[str] = ...
    IMPL_UNKNOWN: typing.ClassVar[str] = ...
    IMPL_VIRTUAL: typing.ClassVar[str] = ...
    IMPL_HARDWARE: typing.ClassVar[str] = ...
    IMPL_SLEQUIP: typing.ClassVar[str] = ...
    IMPL_GM: typing.ClassVar[str] = ...
    IMPL_FESA: typing.ClassVar[str] = ...
    IMPL_FGC: typing.ClassVar[str] = ...
    IMPL_BISCOTO: typing.ClassVar[str] = ...
    DATA_SOURCE: typing.ClassVar[str] = ...
    DATA_SOURCE_UNKNOWN: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def getAccelerator(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getClassVersion(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getClassVersion(string: str) -> str: ...
    @staticmethod
    def getColumnCount(parameter: cern.japc.core.Parameter) -> int: ...
    @staticmethod
    def getDataSource(string: str) -> str: ...
    @staticmethod
    def getDescription(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getDeviceAlias(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getDeviceAlias(string: str) -> str: ...
    @staticmethod
    def getDeviceClassName(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getDeviceResponsible(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getDeviceResponsible(string: str) -> str: ...
    @staticmethod
    def getEnumItemSymbols(string: str) -> java.util.Collection[str]: ...
    @staticmethod
    def getEnumType(string: str) -> cern.japc.value.EnumType: ...
    @typing.overload
    @staticmethod
    def getErrors(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getErrors(parameterDescriptor: cern.japc.core.ParameterDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getErrors(string: str) -> str: ...
    @staticmethod
    def getFormatPattern(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getHostName(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getHostName(string: str) -> str: ...
    @staticmethod
    def getImplementation(string: str) -> int: ...
    @staticmethod
    def getImplementationAsString(string: str) -> str: ...
    @staticmethod
    def getLength(string: str) -> int: ...
    @staticmethod
    def getMapPropertyFieldNames(string: str) -> typing.List[str]: ...
    @staticmethod
    def getMaxValue(string: str) -> float: ...
    @staticmethod
    def getMinValue(string: str) -> float: ...
    @staticmethod
    def getRowCount(parameter: cern.japc.core.Parameter) -> int: ...
    @typing.overload
    @staticmethod
    def getServerName(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getServerName(string: str) -> str: ...
    @staticmethod
    def getSettableEnumItemSymbols(string: str) -> java.util.Collection[str]: ...
    @typing.overload
    @staticmethod
    def getSimpleValueDescriptor(valueDescriptor: cern.japc.value.ValueDescriptor, string: str) -> cern.japc.value.SimpleDescriptor: ...
    @typing.overload
    @staticmethod
    def getSimpleValueDescriptor(string: str) -> cern.japc.value.SimpleDescriptor: ...
    @staticmethod
    def getTgmName(string: str) -> str: ...
    @staticmethod
    def getTitle(string: str) -> str: ...
    @staticmethod
    def getType(string: str) -> cern.japc.value.Type: ...
    @staticmethod
    def getUnit(string: str) -> str: ...
    @staticmethod
    def getValueDescriptor(string: str) -> cern.japc.value.MapDescriptor: ...
    @typing.overload
    @staticmethod
    def getValueType(simpleDescriptor: cern.japc.value.SimpleDescriptor) -> cern.japc.value.ValueType: ...
    @typing.overload
    @staticmethod
    def getValueType(string: str) -> cern.japc.value.ValueType: ...
    @staticmethod
    def isAcquisition(parameterDescriptor: cern.japc.core.ParameterDescriptor) -> bool: ...
    @typing.overload
    @staticmethod
    def isConstant(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isConstant(valueDescriptor: cern.japc.value.ValueDescriptor) -> bool: ...
    @staticmethod
    def isControl(parameterDescriptor: cern.japc.core.ParameterDescriptor) -> bool: ...
    @staticmethod
    def isCycleBound(string: str) -> bool: ...
    @staticmethod
    def isCycleDependent(string: str) -> bool: ...
    @staticmethod
    def isDefaultString(string: str) -> bool: ...
    @staticmethod
    def isDiscrete(string: str) -> bool: ...
    @staticmethod
    def isFilterable(string: str) -> bool: ...
    @staticmethod
    def isMonitorable(string: str) -> bool: ...
    @staticmethod
    def isMultiplexed(string: str) -> bool: ...
    @staticmethod
    def isNonCycleBoundAcquisition(parameterDescriptor: cern.japc.core.ParameterDescriptor) -> bool: ...
    @staticmethod
    def isReadable(string: str) -> bool: ...
    @staticmethod
    def isTransactional(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isValid(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> bool: ...
    @typing.overload
    @staticmethod
    def isValid(parameterDescriptor: cern.japc.core.ParameterDescriptor) -> bool: ...
    @typing.overload
    @staticmethod
    def isValid(valueDescriptor: cern.japc.value.ValueDescriptor) -> bool: ...
    @typing.overload
    @staticmethod
    def isValid(string: str) -> bool: ...
    @staticmethod
    def isWritable(string: str) -> bool: ...

class DiagTrace:
    """
    public class DiagTrace extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        The purpose of this class is to provide dynamic debugging facilities. According to the value set via the
        :meth:`~cern.japc.core.support.DiagTrace.setTraceLevel` method some printout are generated. The traceValue can be a
        bitwise OR of the folowing predefines values. For instance to have debugging trace on data coming from MW RDA you have
        to set the value to : DiagTrace.setTraceLevel(RDA_DATA_RECEPTION); IMPORTANT:
    
    
        DiagTrace.setTraceLevel(0) stop all the debugging trace.
    """
    RDA_SUBSCRIPTION: typing.ClassVar[int] = ...
    """
    public static final int RDA_SUBSCRIPTION
    
        Provide debugging trace each time un/subscription to the RDA is activated
    
        Also see:
            :meth:`~constant`
    
    
    """
    RDA_DATA_RECEPTION: typing.ClassVar[int] = ...
    """
    public static final int RDA_DATA_RECEPTION
    
        Provide debugging trace on each data reception from the RDA
    
        Also see:
            :meth:`~constant`
    
    
    """
    RDA_DATA_SET: typing.ClassVar[int] = ...
    """
    public static final int RDA_DATA_SET
    
        Provide debugging trace each time parameter' set is activated
    
        Also see:
            :meth:`~constant`
    
    
    """
    RDA_PARAMETER_CREATION: typing.ClassVar[int] = ...
    """
    public static final int RDA_PARAMETER_CREATION
    
        Provide debugging trace at the Parameter creation time
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    @staticmethod
    def displayTrace(int: int, string: str) -> None:
        """
            Send the given message to the current outputstream.
        
            Parameters:
                traceLevel (int): The trace level associated with the given message.
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the message to display.
        
        
        """
        ...
    @staticmethod
    def getTraceLevel() -> int:
        """
            The default current trace level. If 0 => stop all the trace.
        
            Returns:
                The default current trace level.
        
        
        """
        ...
    @staticmethod
    def println(string: str, string2: str) -> None:
        """
            Print on the standard output the given message prefixed by the time in the format: prefix HH:MM:SS:ms message.
        
            Parameters:
                prefix (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The String to be printed before everything else.(can be null)
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The message to be printed.
        
        
        """
        ...
    @staticmethod
    def setTraceLevel(int: int) -> None:
        """
            Set the trace level value. setTraceLevel(0) stop all the trace.
        
            Parameters:
                traceLevel (int): The Trace level.
        
        
        """
        ...
    @staticmethod
    def setTraceOutput(printStream: java.io.PrintStream) -> None:
        """
            Set the trace output stream.
        
            Parameters:
                outputStream (`PrintStream <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/PrintStream.html?is-external=true>`): The stream used to output messages via the :meth:`~cern.japc.core.support.DiagTrace.displayTrace` method.
        
        
        """
        ...
    @staticmethod
    def timeStamp() -> str:
        """
            Return the current data and time in the format HH:MM:SS:ms
        
            Returns:
                The current data and time in the format HH:MM:SS:ms
        
        
        """
        ...

class FirstUpdateDiscardingPVL(cern.japc.core.ParameterValueListener):
    """
    public class FirstUpdateDiscardingPVL extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.ParameterValueListener`
    
        A simple :class:`~cern.japc.core.ParameterValueListener` implementation which discards first update. This is important
        for the systems where first update should not be taken into account since has no meaning.
    """
    def __init__(self, parameterValueListener: cern.japc.core.ParameterValueListener): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`
            Notifies this listener that a problem occurred preventing the get/set to be done.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter on which the problem has occurred.
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a non null description of the problem that occurred
                exception (:class:`~cern.japc.core.ParameterException`): an exception possibly null representing the problem that occurred
        
        
        """
        ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.valueReceived`
            Notifies this listener that a new value has been received (get or monitor) or set to the parameter. In the case of the
            notification of the set the value can be null.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.valueReceived`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter for which the value has been received or set.
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the new value received from a get/set or monitor or null in case of set where the value is optional.
        
        
        """
        ...

class ParameterCatalog:
    """
    public class ParameterCatalog extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        This class provides a way to create a unique set of parameters that are used for all access. This class would be used to
        make sure that only one instance of any given parameter is created. The same parameter will be shared for all get and
        set operation and a different monitorable parameter will be created for each subscription request for each parameter.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, parameterFactory: cern.japc.core.factory.ParameterFactory): ...
    @typing.overload
    def __init__(self, parameterFactory: cern.japc.core.factory.ParameterFactory, boolean: bool): ...
    def destroy(self) -> None:
        """
            Destroys this catalog by stopping all subscription and removing all known parameters. After this call, the catalog does
            not contain any parameter and all subscriptions are stopped.
        
        """
        ...
    def destroyParameter(self, string: str) -> None:
        """
            Signal to this catalog that one user of the parameter parameterName is not using it anymore.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter not used by the client of this catalog
        
        
        """
        ...
    def getParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor: ...
    @typing.overload
    def getValue(self, string: str, selector: cern.japc.core.Selector) -> cern.japc.core.AcquiredParameterValue:
        """
            Reads asynchronously the value of the parameter identified by parameterName for the given selector. The provided
            listener is notified of the value read or if a problem occurs.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the parameter to get the value for
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null for cycle independent parameter
                listener (:class:`~cern.japc.core.ParameterValueListener`): the listener to notify when the value is read or when a problem occurs
        
        public :class:`~cern.japc.core.AcquiredParameterValue` getValue (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` parameterName, :class:`~cern.japc.core.Selector` selector) throws :class:`~cern.japc.core.ParameterException`
        
            Reads synchronously the value of the parameter identified by parameterName for the given selector.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the parameter to get the value for
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null for cycle independent parameter
        
            Returns:
                the value read
        
            Raises:
                :class:`~cern.japc.core.ParameterException`: if the value cannot be read.
        
        
        """
        ...
    @typing.overload
    def getValue(self, string: str, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def getValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor: ...
    def isMonitoring(self, string: str, selector: cern.japc.core.Selector) -> bool:
        """
            Returns true if the monitoring of the provided parameter for the given selector is activated.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the parameter to get the value for
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null for cycle independent parameter
        
            Returns:
                true if the monitoring of the provided parameter for the given selector is activated.
        
        
        """
        ...
    def newParameter(self, string: str) -> None: ...
    @typing.overload
    def setValue(self, string: str, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue) -> None:
        """
            Sets asynchronously the value of the parameter identified by parameterName for the given selector. The provided listener
            is notified when the value is set or if a problem occurs.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the parameter to set the value for
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null for cycle independent parameter
                value (cern.japc.value.ParameterValue): the new value to set to this parameter
                listener (:class:`~cern.japc.core.ParameterValueListener`): the listener to notify when the value is set or when a problem occurs
        
        public void setValue (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` parameterName, :class:`~cern.japc.core.Selector` selector, cern.japc.value.ParameterValue value) throws :class:`~cern.japc.core.ParameterException`
        
            Sets synchronously the value of the parameter identified by parameterName for the given selector.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the parameter to set the value for
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null for cycle independent parameter
                value (cern.japc.value.ParameterValue): the new value to set to this parameter
        
            Raises:
                :class:`~cern.japc.core.ParameterException`: if the value cannot be set.
        
        
        """
        ...
    @typing.overload
    def setValue(self, string: str, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def startMonitoring(self, string: str, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None:
        """
            Starts the monitoring of the provided parameter for the given selector.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the parameter to get the value for
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null for cycle independent parameter
                listener (:class:`~cern.japc.core.ParameterValueListener`): the listener notified of the values received from the subscription.
        
        
        """
        ...
    def stopMonitoring(self, string: str, selector: cern.japc.core.Selector) -> None:
        """
            Stops the monitoring of the provided parameter for the given selector.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the parameter to get the value for
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null for cycle independent parameter
        
        
        """
        ...

class ParameterGroupValues:
    """
    public class ParameterGroupValues extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Methods used in conjunction with :class:`~cern.japc.core.group.ParameterGroup`s to convert SimpleParameterValues into
        MapParameterValues and vice versa.
    
        This works only for SimpleParameterValues with extended parameterNames that also contain the field name, e.g.
        BTVI10/Acquisition#timeStamp. The corresponding MapParameterValue has a normal parameterName without field name, e.g.
        BTV10/Acquisition. It contains SimpleParameterValues and use as key names of the map the field names, e.g. "timeStamp".
    
        This is further explained in the following example, where two AcquiredParameterValues containing each a
        SimpleParameterValue are merged into one AcquiredParameterValue with a single MapParameterValue. This corresponds to the
        conversion done by method :meth:`~cern.japc.core.support.ParameterGroupValues.joinSimple2OneMap`.
    
        .. code-block: java
        
         
               AcquiredParameterValue { 
                    parameterName="BTVI10/Acquisition#gain", 
                    value = SimpleParameterValue { value=double 0.2 }
               }
               AcquiredParameterValue { 
                    parameterName="BTVI10/Acquisition#measurement", 
                value = SimpleParameterValue { value=double 23.0 }
               }
            
         
        are converted to
    
        .. code-block: java
        
         
                AcquiredParameterValue { 
                    parameterName="BTVI10/Acquisition", 
                    MapParameterValue {
                        value= { fieldName="gain" => SimpleParameterValue { double 0.2 } }
                        value= { fieldName="measurement" => SimpleParameterValue { double 23.0 } }
                    }
                }
            
         
        These conversions are typically used in a scenario where MapParameterValues coming from FESA equipment and need to be
        stored in some Database as SimpleParameterValues. As of this writing, LSA Settings and the LHC Measurement database (and
        the LHC logging database) can only handle simple ParameterValues. So to be able to store MapParameterValues in there,
        these need to be split up into SimpleParameterValues. On retrieval of data form the database, the inverse operation has
        to be done, i.e. several SimpleParameterValues needs to be joined into one MapParameterValue.
    
        Methods for combining SimpleParameterValues to MapParameterValues are prefixed with "join", whereas methods for doing
        the opposite, i.e. breaking up MapParameterValues into SimpleParameterValues are prefixed with "split".
    
        The methods are capable of splitting and joining the JAPC value classes :code:`MapParameterValue`and
        :code:`SimpleParameterValue`or the container classes :class:`~cern.japc.core.AcquiredParameterValue`and (or
        :class:`~cern.japc.core.FailSafeParameterValue`.
    
        The arguments used in these methods reflect those used in JAPC, where setValue() methods take :code:`ParameterValue`s as
        argument, whereas getValue() methods return :class:`~cern.japc.core.AcquiredParameterValue`s (or
        :class:`~cern.japc.core.FailSafeParameterValue`s in the case of JAPC :class:`~cern.japc.core.group.ParameterGroup`).
    
        Methods to join SimpleParameterValues inside AcquiredParameterValues and FailSafeParameterValues:
    
          - :meth:`~cern.japc.core.support.ParameterGroupValues.joinSimple2OneMap`converts an array of AcquiredParameterValues which
            each contain a SimpleParameterValue with a full parameterName (c.f. example above) into one AcquiredParameterValue that
            contains a MapParameterValue.
          - :meth:`~cern.japc.core.support.ParameterGroupValues.joinSimple2OneMapFailSafe`the same for FailSafeParameterValues
          - :meth:`~cern.japc.core.support.ParameterGroupValues.joinSimple2ManyMaps`converts many groups of SimpleParameterValues
            which each contain one Simple
          - :meth:`~cern.japc.core.support.ParameterGroupValues.joinSimple2ManyMapsFailSafe`the same for FailSafeParameterValues
    
    
        One method to split one or more MapParameterValues into its constituent SimpleParameterValues is supported:
    
          - :meth:`~cern.japc.core.support.ParameterGroupValues.splitOneMap2Simple`
    """
    @typing.overload
    @staticmethod
    def checkForException(failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> cern.japc.core.FailSafeParameterValue:
        """
            Same as :meth:`~cern.japc.core.support.ParameterGroupValues.checkForException` with checkSameParameterName = false
        
            Parameters:
                fs (:class:`~cern.japc.core.FailSafeParameterValue`[]): an array of FailSafeParameterValues
        
            Returns:
                a FailSafeParameterValue with the exception or null if no exception was found
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkForException(failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue], boolean: bool) -> cern.japc.core.FailSafeParameterValue:
        """
            Checks if one of the simple FailSafeParameterValues contains an exception. If yes, one FailSafeParameterValue with that
            exception is returned, corresponding to the map FailSafeParameterValue. If no, null is returned.
        
            Parameters:
                fs (:class:`~cern.japc.core.FailSafeParameterValue`[]): an array of FailSafeParameterValues
                checkSameMainParameterName (boolean):             if true, the method verifies that all fs[] have the same mainParameterName and throws an IllegalArgumentException if not
        
            Returns:
                a FailSafeParameterValue with the exception or null if no exception was found
        
        """
        ...
    @staticmethod
    def joinSimple2ManyMaps(acquiredParameterValueArray: typing.List[cern.japc.core.AcquiredParameterValue]) -> typing.List[cern.japc.core.AcquiredParameterValue]:
        """
            Converts AcquiredParameterValues with SimpleValues into AcquiredParameterValues with MapParameterValues. The
            AquiredParameterValues passed as arguments must have with full parameter names inside (e.g.
            :code:`"PowDf10/Setting#currentRef"`) and contain SimpleParameterValues. Each of the produced AcquiredParameterValues
            has the main parameterNames (e.g. :code:`"PowDf10/Setting"`) and contains one MapParameterValue with the values of the
            SimpleParameterValues.
        
            Used in getXxx() methods that retrieve an array SimpleParameterValues that belong together, and which has to be
            recombined to one single MapParameterValue.
        
            Parameters:
                simpleAcqParVals (:class:`~cern.japc.core.AcquiredParameterValue`[]): the array of AcquiredParameterValues with field names inside.
        
            Returns:
                an array of AcquiredParameterValues corresponding to the main parameterNames
        
        
        """
        ...
    @staticmethod
    def joinSimple2ManyMapsFailSafe(failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> typing.List[cern.japc.core.FailSafeParameterValue]:
        """
            Converts FailSafeParameterValues with SimpleValues into FailSafeParameterValues with MapParameterValues. The
            AquiredParameterValues passed as arguments must have with full parameter names inside (e.g.
            :code:`"PowDf10/Setting#currentRef"`) and contain SimpleParameterValues. Each of the produced FailSafeParameterValues
            has the main parameterNames (e.g. :code:`"PowDf10/Setting"`) and contains one MapParameterValue with the values of the
            SimpleParameterValues. If a FailSafeParameterValue containing an exception is passed to this method, the produced
            FailSafeParameterValue will also contain this exception.
        
            Parameters:
                fspv (:class:`~cern.japc.core.FailSafeParameterValue`[]): the array of FailSafeParameterValues with field names inside.
        
            Returns:
                an array of FailSafeParameterValues corresponding to the main parameterNames
        
            Also see:
                :meth:`~cern.japc.core.support.ParameterGroupValues.joinSimple2ManyMaps`
        
        
        """
        ...
    @staticmethod
    def joinSimple2OneMap(acquiredParameterValueArray: typing.List[cern.japc.core.AcquiredParameterValue]) -> cern.japc.core.AcquiredParameterValue:
        """
            Converts related AcquiredParameterValues with SimpleParameterValues into one AcquiredParameterValue that contains a
            MapParameterValue. The ValueHeader and Status are taken from the first parameterValue in the list.
        
        
            Parameters:
                acqParVals (:class:`~cern.japc.core.AcquiredParameterValue`[]): the array of simple AcquiredParameterValues corresponding to the main name
        
            Returns:
                the AcquiredParameterValue that contains a MapParameterValue
        
            Also see:
                :meth:`~cern.japc.core.support.ParameterGroupValues.joinSimple2ManyMapsFailSafe`
        
        
        """
        ...
    @staticmethod
    def joinSimple2OneMapFailSafe(failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> cern.japc.core.FailSafeParameterValue:
        """
            Converts related FailSafeParameterValues with SimpleParameterValues into one FailSafeParameterValue that contains a
            MapParameterValue. Same as :meth:`~cern.japc.core.support.ParameterGroupValues.joinSimple2OneMap` but for
            FailSafeParameterValues
        
            **Precondition: none of the FailSafeParamterValues contains an exception.**
        
            Parameters:
                fsParVals (:class:`~cern.japc.core.FailSafeParameterValue`[]): the array of simple FailSafeParameterValues corresponding to the main name
        
            Returns:
                the FailSafeParameterValue that contains a MapParameterValue
        
        
        """
        ...
    @staticmethod
    def splitOneMap2Simple(acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> typing.List[cern.japc.core.AcquiredParameterValue]:
        """
            Splits an AcquiredParameterValue containing a MapParameterValue into AcquiredParameterValues with the corresponding
            SimpleParameterValues.
        
            The produced AcquiredParameterValues have full parameterNames including the field names, e.g.
            "BTVI10/Acquisition#measurement".
        
        
            The returned array of SimpleParameterValues is ordered alphabetically by the field names
        
            Parameters:
                apv (:class:`~cern.japc.core.AcquiredParameterValue`): the AcquiredParameterValue with the MapParameterValue to split
        
            Returns:
                an array of AcquiredParameterValues with SimpleParameterValues
        
        
        """
        ...

class ParameterValues:
    @typing.overload
    @staticmethod
    def extractParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def extractParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, int: int) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def extractParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def extractParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str, int: int) -> typing.Any: ...
    @staticmethod
    def extractSimpleParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def getFieldStatus(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, int: int, string: str) -> cern.japc.value.ValueStatus: ...
    @typing.overload
    @staticmethod
    def getFieldStatus(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, int: int, string: str, int2: int) -> cern.japc.value.ValueStatus: ...
    @typing.overload
    @staticmethod
    def getFieldStatus(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> cern.japc.value.ValueStatus: ...
    @typing.overload
    @staticmethod
    def getFieldStatus(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str, int: int) -> cern.japc.value.ValueStatus: ...
    @typing.overload
    @staticmethod
    def getFieldValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, int: int, string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, int: int, string: str, int2: int) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(failSafeParameterValue: cern.japc.core.FailSafeParameterValue, int: int, string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(failSafeParameterValue: cern.japc.core.FailSafeParameterValue, int: int, string: str, int2: int) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(failSafeParameterValue: cern.japc.core.FailSafeParameterValue, string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(failSafeParameterValue: cern.japc.core.FailSafeParameterValue, string: str, int: int) -> str: ...
    @staticmethod
    def getMaxValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> float: ...
    @staticmethod
    def getMinValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> float: ...
    @staticmethod
    def getUnit(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> str: ...
    @staticmethod
    def getValueAsBoolean(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> bool: ...
    @staticmethod
    def getValueAsDouble(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> float: ...
    @staticmethod
    def getValueAsFloat(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> float: ...
    @staticmethod
    def getValueAsInt(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> int: ...
    @staticmethod
    def getValueAsLong(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> int: ...
    @staticmethod
    def getValueAsStrings(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> typing.List[str]: ...
    @staticmethod
    def printArray(parameterValueArray: typing.List[cern.japc.value.ParameterValue]) -> None: ...
    @typing.overload
    @staticmethod
    def replaceControlStatus(simpleParameterValue: cern.japc.value.SimpleParameterValue, simpleValueControlStatus: cern.japc.value.SimpleValueControlStatus) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def replaceControlStatus(simpleValueStatus: cern.japc.value.SimpleValueStatus, simpleValueControlStatus: cern.japc.value.SimpleValueControlStatus) -> cern.japc.value.SimpleValueStatus: ...

class SysoutParameterValueListener(cern.japc.core.ParameterValueListener):
    """
    public class SysoutParameterValueListener extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.ParameterValueListener`
    
        Implements a simple ParameterValueListener that ouput the values and exceptions received on the command line.
    """
    def __init__(self): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`
            Notifies this listener that a problem occurred preventing the get/set to be done.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter on which the problem has occurred.
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a non null description of the problem that occurred
                exception (:class:`~cern.japc.core.ParameterException`): an exception possibly null representing the problem that occurred
        
        
        """
        ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.valueReceived`
            Notifies this listener that a new value has been received (get or monitor) or set to the parameter. In the case of the
            notification of the set the value can be null.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.valueReceived`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter for which the value has been received or set.
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the new value received from a get/set or monitor or null in case of set where the value is optional.
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.support")``.

    Descriptors: typing.Type[Descriptors]
    DiagTrace: typing.Type[DiagTrace]
    FirstUpdateDiscardingPVL: typing.Type[FirstUpdateDiscardingPVL]
    ParameterCatalog: typing.Type[ParameterCatalog]
    ParameterGroupValues: typing.Type[ParameterGroupValues]
    ParameterValues: typing.Type[ParameterValues]
    SysoutParameterValueListener: typing.Type[SysoutParameterValueListener]
