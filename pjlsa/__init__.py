__version__ = "0.2.4"

__cmmnbuild_deps__ = [
    {"product": "log4j", "groupId": "log4j"},
    {"product": "lsa-client", "groupId": "cern.lsa"}
]

from .pjlsa import LSAClient

__all__ = ["LSAClient"]
