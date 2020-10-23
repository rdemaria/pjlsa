from typing import List as _py_List
from typing import ClassVar as _py_ClassVar
from typing import overload
import cern.japc.core
import cern.japc.core.factory
import cern.japc.core.spi
import cern.japc.core.transaction
import cern.japc.value
import java.io
import java.util


class InternalParameterCharacteristics(cern.japc.core.factory.ParameterCharacteristicsImpl, cern.japc.core.ParameterCharacteristics, java.io.Serializable):
    def __init__(self, parameterCharacteristics: cern.japc.core.ParameterCharacteristics): ...
    def decreaseCreatingCompositeParameter(self) -> None: ...
    def increaseCreatingCompositeParameter(self) -> None: ...
    def isCreatingCompositeParameter(self) -> bool: ...
    def toString(self) -> str: ...

class ParameterCreator:
    SERVICE_NAME_PROPERTY: _py_ClassVar[str] = ...
    PROTOCOL_PROPERTY: _py_ClassVar[str] = ...
    CREATOR_CLASS_PROPERTY: _py_ClassVar[str] = ...
    DEFAULT_PROPERTY: _py_ClassVar[str] = ...
    def createParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor, parameterFactory: cern.japc.core.factory.ParameterFactory) -> cern.japc.core.transaction.TransactionalParameter: ...

class ServiceConfigLookup:
    def getConfig(self, string: str) -> _py_List[java.util.Properties]: ...

class AdvancedParameterCreator(ParameterCreator):
    @overload
    def createParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor, parameterFactory: cern.japc.core.factory.ParameterFactory, internalParameterCharacteristics: InternalParameterCharacteristics) -> cern.japc.core.transaction.TransactionalParameter: ...
    @overload
    def createParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor, parameterFactory: cern.japc.core.factory.ParameterFactory) -> cern.japc.core.transaction.TransactionalParameter: ...

class CompositeParameterCreator(AdvancedParameterCreator):
    def isKnownCompositeParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl) -> bool: ...