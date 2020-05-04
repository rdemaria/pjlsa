from typing import List as _py_List
from typing import overload
import cern.japc.value


class DomainValueFactory:
    def __init__(self): ...
    @classmethod
    def newDiscreteFunction(cls, doubleArray: _py_List[float], doubleArray2: _py_List[float]) -> cern.japc.value.DiscreteFunction: ...
    @classmethod
    def newDiscreteFunctionList(cls, discreteFunctionArray: _py_List[cern.japc.value.DiscreteFunction]) -> cern.japc.value.DiscreteFunctionList: ...
    @classmethod
    @overload
    def newEnumItemSet(cls, enumItem: cern.japc.value.EnumItem, enumItemArray: _py_List[cern.japc.value.EnumItem]) -> cern.japc.value.EnumItemSet: ...
    @classmethod
    @overload
    def newEnumItemSet(cls, enumType: cern.japc.value.EnumType, enumItemArray: _py_List[cern.japc.value.EnumItem]) -> cern.japc.value.EnumItemSet: ...
    @classmethod
    @overload
    def newEnumItemSet(cls, enumType: cern.japc.value.EnumType, long: int) -> cern.japc.value.EnumItemSet: ...
