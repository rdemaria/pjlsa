import cern.lsa.client
import cern.lsa.domain
import typing


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa")``.

    client: cern.lsa.client.__module_protocol__
    domain: cern.lsa.domain.__module_protocol__
