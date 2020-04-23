import pjlsa
import jpype.imports
import stubgenj
import sys
import importlib

lsa = pjlsa.LSAClient()

jpype.imports.registerDomain("cern")
jpype_importer = sys.meta_path[-1]
del sys.meta_path[-1]
sys.meta_path.insert(0, jpype_importer)

classes = [c for c in lsa._mgr.class_search('cern.lsa.domain.settings.') if '$' not in c]

import cern.lsa.domain.settings
for cls in classes:
    importlib.import_module(cls)


stubgenj.generate_stub_for_java_module('cern.lsa.domain.settings', 'pyi/cern/lsa/domain/settings/__init__.pyi')

#from cern.lsa.domain.settings import StandAloneBeamProcess

#sabp = StandAloneBeamProcess()
#sabp.getCategory()

