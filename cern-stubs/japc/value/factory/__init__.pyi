import cern.japc.value
import typing



class DomainValueFactory:
    """
    public class DomainValueFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        This factory is used to produce implementations of accelerator complex domain classes, like
        :class:`~cern.japc.value.DiscreteFunction` and :class:`~cern.japc.value.DiscreteFunctionList` implementations.
    """
    def __init__(self): ...
    @staticmethod
    def newDiscreteFunction(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> cern.japc.value.DiscreteFunction:
        """
            Creates a new :class:`~cern.japc.value.DiscreteFunction`.
        
            Parameters:
                xArray (double[]): an array of X coordinates
                yArray (double[]): an array of Y coordinates
        
            Returns:
                constructed :class:`~cern.japc.value.DiscreteFunction`
        
        
        """
        ...
    @staticmethod
    def newDiscreteFunctionList(discreteFunctionArray: typing.List[cern.japc.value.DiscreteFunction]) -> cern.japc.value.DiscreteFunctionList:
        """
            Creates a new :class:`~cern.japc.value.DiscreteFunctionList`.
        
            Parameters:
                functions (:class:`~cern.japc.value.DiscreteFunction`...): discrete function which should compose the list
        
            Returns:
                constructed :class:`~cern.japc.value.DiscreteFunctionList`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newEnumItemSet(enumItem: cern.japc.value.EnumItem, enumItemArray: typing.List[cern.japc.value.EnumItem]) -> cern.japc.value.EnumItemSet:
        """
            Creates a new :class:`~cern.japc.value.EnumItemSet`.
        
            Parameters:
                enumType (:class:`~cern.japc.value.EnumType`): the enumeration type to contain items of
                encodedEnumItems (long): bitmap encoded enumeration values (basically coming from HW)
        
            Creates a new :class:`~cern.japc.value.EnumItemSet`.
        
            Parameters:
                firstItem (:class:`~cern.japc.value.EnumItem`): an item in the set
                otherItems (:class:`~cern.japc.value.EnumItem`...): other items in the set
        
            Creates a new :class:`~cern.japc.value.EnumItemSet`.
        
            Parameters:
                enumType (:class:`~cern.japc.value.EnumType`): the enumeration type to contain items of
                enumItems (:class:`~cern.japc.value.EnumItem`...): initial list of items
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newEnumItemSet(enumType: cern.japc.value.EnumType, enumItemArray: typing.List[cern.japc.value.EnumItem]) -> cern.japc.value.EnumItemSet: ...
    @typing.overload
    @staticmethod
    def newEnumItemSet(enumType: cern.japc.value.EnumType, long: int) -> cern.japc.value.EnumItemSet: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.value.factory")``.

    DomainValueFactory: typing.Type[DomainValueFactory]
