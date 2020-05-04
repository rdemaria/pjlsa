from typing import List as _py_List
import cern.japc.value


class DomainValueFactory:
    def __init__(self): ...
    @classmethod
    def newDiscreteFunction(cls, doubleArray: _py_List[float], doubleArray2: _py_List[float]) -> cern.japc.value.DiscreteFunction: ...
    @classmethod
    def newDiscreteFunctionList(cls, discreteFunctionArray: _py_List[cern.japc.value.DiscreteFunction]) -> cern.japc.value.DiscreteFunctionList: ...
