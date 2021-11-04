import cern.accsoft
import cern.japc
import cern.lsa
import cern.rbac
import typing


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern")``.

    accsoft: cern.accsoft.__module_protocol__
    japc: cern.japc.__module_protocol__
    lsa: cern.lsa.__module_protocol__
    rbac: cern.rbac.__module_protocol__
