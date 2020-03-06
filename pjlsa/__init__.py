__version__ = "0.0.15"

__cmmnbuild_deps__ = [
    "lsa-client",
]

# When running setuptools without required dependencies installed
# we need to be able to access __version__, so print a warning but
# continue
try:
    from .pjlsa import *
except ImportError as e:
    import logging
    logging.basicConfig()
    log = logging.getLogger(__name__)
    log.warn(str(e))
    log.warn("required dependencies are not installed")
