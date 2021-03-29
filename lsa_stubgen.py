import cmmnbuild_dep_manager
import logging

logging.basicConfig(level='INFO')

manager = cmmnbuild_dep_manager.Manager()

manager.stubgen(output_dir='.')
