import typing



class InitAware:
    """
    public interface InitAware
    
        Adds init awareness to the implementing classes. It's used to initialize the instance after all necessary setters have
        been called.
    """
    def init(self) -> None:
        """
            Do all necessary work to initialize the instance (called usually after setters).
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.marker")``.

    InitAware: typing.Type[InitAware]
