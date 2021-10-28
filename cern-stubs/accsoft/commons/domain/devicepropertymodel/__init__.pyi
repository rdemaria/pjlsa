import typing



class ClassDesignNames:
    """
    Java class 'cern.accsoft.commons.domain.devicepropertymodel.ClassDesignNames'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def assertDeviceName(string: str) -> None: ...
    @staticmethod
    def assertFieldName(string: str) -> None: ...
    @staticmethod
    def assertPropertyName(string: str) -> None: ...
    @staticmethod
    def isDeviceName(string: str) -> bool: ...
    @staticmethod
    def isFieldName(string: str) -> bool: ...
    @staticmethod
    def isPropertyName(string: str) -> bool: ...

class ParameterNames:
    """
    Java class 'cern.accsoft.commons.domain.devicepropertymodel.ParameterNames'
    
        Extends:
            java.lang.Object
    
      Attributes:
        PROTOCOL_SERVICE_SEPARATOR (java.lang.String): final static field
        SERVICE_DEVICE_SEPARATOR (java.lang.String): final static field
        DEVICE_PROPERTY_SEPARATOR (java.lang.String): final static field
        PROPERTY_FIELD_SEPARATOR (java.lang.String): final static field
    
    """
    PROTOCOL_SERVICE_SEPARATOR: typing.ClassVar[str] = ...
    SERVICE_DEVICE_SEPARATOR: typing.ClassVar[str] = ...
    DEVICE_PROPERTY_SEPARATOR: typing.ClassVar[str] = ...
    PROPERTY_FIELD_SEPARATOR: typing.ClassVar[str] = ...
    @typing.overload
    @staticmethod
    def assertParameterName(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def assertParameterName(string: str, boolean: bool) -> None: ...
    @typing.overload
    @staticmethod
    def isParameterName(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isParameterName(string: str, boolean: bool) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.devicepropertymodel")``.

    ClassDesignNames: typing.Type[ClassDesignNames]
    ParameterNames: typing.Type[ParameterNames]
