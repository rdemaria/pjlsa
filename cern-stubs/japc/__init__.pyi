import cern.japc.core
import cern.japc.value
import typing


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc")``.

    core: cern.japc.core.__module_protocol__
    value: cern.japc.value.__module_protocol__
