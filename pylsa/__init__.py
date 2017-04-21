__version__ = "0.0.1"

cmmnbuild_deps = [
    "lsa-client"
]

# When running setuptools without required dependencies installed
# we need to be able to access __version__, so print a warning but
# continue
try:
    from .pylsa import *
except ImportError:
    import logging
    logging.basicConfig()
    log = logging.getLogger(__name__)
    log.warn("required dependencies are not installed")
