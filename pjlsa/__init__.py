__version__ = "0.0.12"

__cmmnbuild_deps__ = [
    "lsa-client",
    "slf4j-log4j12",
    "slf4j-api",
    "log4j"
]

# When running setuptools without required dependencies installed
# we need to be able to access __version__, so print a warning but
# continue
try:
    from .pjlsa import *
except ImportError:
    import logging
    logging.basicConfig()
    log = logging.getLogger(__name__)
    log.warn("required dependencies are not installed")
