import typing



class InitAware:
    """
    Java class 'cern.accsoft.commons.util.marker.InitAware'
    
    """
    def init(self) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.marker")``.

    InitAware: typing.Type[InitAware]
