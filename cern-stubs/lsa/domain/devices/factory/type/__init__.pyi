import cern.lsa.domain.devices
import cern.lsa.domain.devices.type
import java.util
import typing


class PropertyVersionsRequestBuilder:
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.devices.type.PropertyVersionsRequest: ...
    @staticmethod
    def byDeviceTypeName(string: str) -> cern.lsa.domain.devices.type.PropertyVersionsRequest: ...
    @staticmethod
    def byDeviceTypeNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.devices.type.PropertyVersionsRequest: ...
    @staticmethod
    def byDeviceTypeVersion(deviceTypeVersion: cern.lsa.domain.devices.DeviceTypeVersion) -> cern.lsa.domain.devices.type.PropertyVersionsRequest: ...
    @staticmethod
    def byDeviceTypeVersions(collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceTypeVersion], typing.Sequence[cern.lsa.domain.devices.DeviceTypeVersion]]) -> cern.lsa.domain.devices.type.PropertyVersionsRequest: ...
    @typing.overload
    @staticmethod
    def byDeviceTypes(deviceType: cern.lsa.domain.devices.DeviceType) -> cern.lsa.domain.devices.type.PropertyVersionsRequest: ...
    @typing.overload
    @staticmethod
    def byDeviceTypes(collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceType], typing.Sequence[cern.lsa.domain.devices.DeviceType]]) -> cern.lsa.domain.devices.type.PropertyVersionsRequest: ...
    def setDeviceTypeName(self, string: str) -> 'PropertyVersionsRequestBuilder': ...
    def setDeviceTypeNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'PropertyVersionsRequestBuilder': ...
    def setDeviceTypeVersion(self, deviceTypeVersion: cern.lsa.domain.devices.DeviceTypeVersion) -> 'PropertyVersionsRequestBuilder': ...
    def setDeviceTypeVersions(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceTypeVersion], typing.Sequence[cern.lsa.domain.devices.DeviceTypeVersion]]) -> 'PropertyVersionsRequestBuilder': ...
    def setPropertyName(self, string: str) -> 'PropertyVersionsRequestBuilder': ...
    def setPropertyNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'PropertyVersionsRequestBuilder': ...
