import cern.accsoft.commons.ccs
import cern.accsoft.commons.diag
import cern.accsoft.commons.domain
import cern.accsoft.commons.remoting
import cern.accsoft.commons.timing
import cern.accsoft.commons.util
import cern.accsoft.commons.value
import typing


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons")``.

    ccs: cern.accsoft.commons.ccs.__module_protocol__
    diag: cern.accsoft.commons.diag.__module_protocol__
    domain: cern.accsoft.commons.domain.__module_protocol__
    remoting: cern.accsoft.commons.remoting.__module_protocol__
    timing: cern.accsoft.commons.timing.__module_protocol__
    util: cern.accsoft.commons.util.__module_protocol__
    value: cern.accsoft.commons.value.__module_protocol__
