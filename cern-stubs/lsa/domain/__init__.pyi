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
    public class LsaException extends `Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`
    
        A generic LSA exception.
    
    
        Although the exception has public constructors, it is mainly meant for inheritance by more concrete exception classes.
    
        Also see:
            :meth:`~serialized`
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
