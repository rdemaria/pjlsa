__version__ = "0.2.0"

__cmmnbuild_deps__ = [
    "log4j",
    "lsa-client",
]

from .pjlsa import LSAClient

__all__ = ["LSAClient"]
