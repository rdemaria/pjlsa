import pjlsa
import jpype.imports
import stubgenj
import sys

lsa = pjlsa.LSAClient()

sigs=dict()
class_sigs=dict()

jpype.imports.registerDomain("cern")
jpype_importer = sys.meta_path[-1]
del sys.meta_path[-1]
sys.meta_path.insert(0, jpype_importer)

import cern.lsa.domain.settings
from cern.lsa.domain.settings import Setting
from cern.lsa.domain.settings import Settings

stubgenj.generate_stub_for_c_module('cern.lsa.domain.settings', 'pyi/cern/lsa/domain/settings.pyi', sigs, class_sigs)
