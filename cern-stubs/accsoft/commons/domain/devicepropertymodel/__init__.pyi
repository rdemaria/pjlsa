import typing



class ClassDesignNames:
    """
    public final class ClassDesignNames extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    MAX_SUFFIX_LC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MAX_SUFFIX_LC
    
        Standard field name suffix for the maximum value
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAX_SUFFIX_UC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MAX_SUFFIX_UC
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    MIN_SUFFIX_LC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MIN_SUFFIX_LC
    
        Standard field name suffix for the minimum value
    
        Also see:
            :meth:`~constant`
    
    
    """
    MIN_SUFFIX_UC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MIN_SUFFIX_UC
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNITS_SUFFIX_LC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` UNITS_SUFFIX_LC
    
        Standard field name suffix for the units
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNITS_SUFFIX_UC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` UNITS_SUFFIX_UC
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAX_X_SUFFIX_LC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MAX_X_SUFFIX_LC
    
        Standard field name suffix for the x maximum value
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAX_X_SUFFIX_UC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MAX_X_SUFFIX_UC
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    MIN_X_SUFFIX_LC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MIN_X_SUFFIX_LC
    
        Standard field name suffix for the x minimum value
    
        Also see:
            :meth:`~constant`
    
    
    """
    MIN_X_SUFFIX_UC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MIN_X_SUFFIX_UC
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNITS_X_SUFFIX_LC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` UNITS_X_SUFFIX_LC
    
        Standard field name suffix for the units of the x axis
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNITS_X_SUFFIX_UC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` UNITS_X_SUFFIX_UC
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    STATUS_SUFFIX_LC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` STATUS_SUFFIX_LC
    
        Standard field name suffix for the value status
    
        Also see:
            :meth:`~constant`
    
    
    """
    STATUS_SUFFIX_UC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` STATUS_SUFFIX_UC
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def assertDeviceName(string: str) -> None:
        """
            Asserts that the given String is a valid device name.
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): device name to check
        
            Raises:
                : if the given string is not a valid device name
        
        
        """
        ...
    @staticmethod
    def assertFieldName(string: str) -> None:
        """
            Asserts that the given String is a valid field name.
        
            Parameters:
                fieldName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): field name to check
        
            Raises:
                : if the given string is not a valid field name
        
        
        """
        ...
    @staticmethod
    def assertPropertyName(string: str) -> None:
        """
            Asserts that the given String is a valid property name.
        
            Parameters:
                propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): property name to check
        
            Raises:
                : if the given string is not a valid property name
        
        
        """
        ...
    @staticmethod
    def isDeviceName(string: str) -> bool:
        """
            Return :code:`true` if the given String is a valid device name and :code:`false` otherwise.
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): device name to check
        
            Returns:
                :code:`true` if the given String is a valid device name
        
        
        """
        ...
    @staticmethod
    def isFieldName(string: str) -> bool:
        """
            Return :code:`true` if the given String is a valid field name and :code:`false` otherwise.
        
            Parameters:
                fieldName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): field name to check
        
            Returns:
                :code:`true` if the given String is a valid field name
        
        
        """
        ...
    @staticmethod
    def isMetaInfoFieldName(string: str) -> bool:
        """
            Returns :code:`true` if the given field name is a meta-field name (ends with _min, _max, _units, _status).
        
            Parameters:
                fieldName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): field name to check
        
            Returns:
                :code:`true` if the given field name is a meta-field name
        
        
        """
        ...
    @staticmethod
    def isPropertyName(string: str) -> bool:
        """
            Return :code:`true` if the given String is a valid property name and :code:`false` otherwise.
        
            Parameters:
                propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): property name to check
        
            Returns:
                :code:`true` if the given String is a valid property name
        
        
        """
        ...

class ParameterNames:
    """
    public final class ParameterNames extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    PROTOCOL_SERVICE_SEPARATOR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROTOCOL_SERVICE_SEPARATOR
    
        The separator between protocol and service
    
        Also see:
            :meth:`~constant`
    
    
    """
    SERVICE_DEVICE_SEPARATOR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SERVICE_DEVICE_SEPARATOR
    
        The separator between service and device
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_PROPERTY_SEPARATOR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_PROPERTY_SEPARATOR
    
        The separator between device and property
    
        Also see:
            :meth:`~constant`
    
    
    """
    PROPERTY_FIELD_SEPARATOR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROPERTY_FIELD_SEPARATOR
    
        The separator between property and field
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    @staticmethod
    def assertParameterName(string: str) -> None:
        """
            Asserts that the given String is a valid parameter name.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name to check
        
            Raises:
                : if the given string is not a valid parameter name
        
        """
        ...
    @typing.overload
    @staticmethod
    def assertParameterName(string: str, boolean: bool) -> None:
        """
            Asserts that the given String is a valid parameter name.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name to check
                strictCheck (boolean): if true the method will check the parameterName for the presence of incorrect characters
        
            Raises:
                : if the given string is not a valid parameter name
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isParameterName(string: str) -> bool:
        """
            Return :code:`true` if the given String is a valid parameter name and :code:`false` otherwise.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name to check
        
            Returns:
                :code:`true` if the given String is a valid parameter name
        
        """
        ...
    @typing.overload
    @staticmethod
    def isParameterName(string: str, boolean: bool) -> bool:
        """
            Return :code:`true` if the given String is a valid parameter name and :code:`false` otherwise.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter
                strictCheck (boolean): if true the method will check the parameterName for the presence of incorrect characters
        
            Returns:
                :code:`true` if the given String is a valid parameter name
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.devicepropertymodel")``.

    ClassDesignNames: typing.Type[ClassDesignNames]
    ParameterNames: typing.Type[ParameterNames]
