__version__ = "0.1.0"

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
    from .lsa_client import LsaClient
    from .lsa_domain import *
except (ImportError, TypeError) as ex:
    import logging
    logging.basicConfig()
    log = logging.getLogger(__name__)
    log.warning("required dependencies are not yet installed: {0}".format(ex))
