import cern.japc.value
import typing



class DomainValueFactory:
    """
    Java class 'cern.japc.value.factory.DomainValueFactory'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * DomainValueFactory()
    
    """
    def __init__(self): ...
    @staticmethod
    def newDiscreteFunction(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> cern.japc.value.DiscreteFunction: ...
    @staticmethod
    def newDiscreteFunctionList(discreteFunctionArray: typing.List[cern.japc.value.DiscreteFunction]) -> cern.japc.value.DiscreteFunctionList: ...
    @typing.overload
    @staticmethod
    def newEnumItemSet(enumItem: cern.japc.value.EnumItem, enumItemArray: typing.List[cern.japc.value.EnumItem]) -> cern.japc.value.EnumItemSet: ...
    @typing.overload
    @staticmethod
    def newEnumItemSet(enumType: cern.japc.value.EnumType, enumItemArray: typing.List[cern.japc.value.EnumItem]) -> cern.japc.value.EnumItemSet: ...
    @typing.overload
    @staticmethod
    def newEnumItemSet(enumType: cern.japc.value.EnumType, long: int) -> cern.japc.value.EnumItemSet: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.value.factory")``.

    DomainValueFactory: typing.Type[DomainValueFactory]
