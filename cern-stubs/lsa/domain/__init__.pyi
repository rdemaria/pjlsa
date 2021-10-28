import cern.lsa.domain.cern
import cern.lsa.domain.commons
import cern.lsa.domain.devices
import cern.lsa.domain.exploitation
import cern.lsa.domain.generation
import cern.lsa.domain.optics
import cern.lsa.domain.settings
import cern.lsa.domain.trim
import java.lang
import typing



class LsaException(java.lang.Exception):
    """
    Java class 'cern.lsa.domain.LsaException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * LsaException(java.lang.String, java.lang.Exception)
        * LsaException(java.lang.String)
        * LsaException(java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain")``.

    LsaException: typing.Type[LsaException]
    cern: cern.lsa.domain.cern.__module_protocol__
    commons: cern.lsa.domain.commons.__module_protocol__
    devices: cern.lsa.domain.devices.__module_protocol__
    exploitation: cern.lsa.domain.exploitation.__module_protocol__
    generation: cern.lsa.domain.generation.__module_protocol__
    optics: cern.lsa.domain.optics.__module_protocol__
    settings: cern.lsa.domain.settings.__module_protocol__
    trim: cern.lsa.domain.trim.__module_protocol__
