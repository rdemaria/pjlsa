__version__ = "0.2.11"

__cmmnbuild_deps__ = [
    {"product": "log4j", "groupId": "log4j"},
    {"product": "lsa-client", "groupId": "cern.lsa"}
]

__stubgen_packages__ = [
    "java",
    "com.google.common.collect",
    "com.google.common.base",
    "cern.lsa",
    "cern.accsoft.commons",
    "cern.rbac.common",
    "cern.japc.core",
    "cern.japc.value"
]

from ._pjlsa import LSAClient

__all__ = ["LSAClient"]
