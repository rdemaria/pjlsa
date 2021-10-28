import cern.lsa.domain.cern.commons
import cern.lsa.domain.cern.devices
import cern.lsa.domain.cern.diag
import cern.lsa.domain.cern.exploitation
import cern.lsa.domain.cern.optics
import cern.lsa.domain.cern.settings
import cern.lsa.domain.cern.timing
import cern.lsa.domain.cern.workset
import typing


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern")``.

    commons: cern.lsa.domain.cern.commons.__module_protocol__
    devices: cern.lsa.domain.cern.devices.__module_protocol__
    diag: cern.lsa.domain.cern.diag.__module_protocol__
    exploitation: cern.lsa.domain.cern.exploitation.__module_protocol__
    optics: cern.lsa.domain.cern.optics.__module_protocol__
    settings: cern.lsa.domain.cern.settings.__module_protocol__
    timing: cern.lsa.domain.cern.timing.__module_protocol__
    workset: cern.lsa.domain.cern.workset.__module_protocol__
