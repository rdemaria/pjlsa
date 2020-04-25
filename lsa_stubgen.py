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


def imp(pack):
    classes = [c for c in lsa._mgr.class_search(pack + '.')]
    importlib.import_module(pack)
    for cls in classes:
        importlib.import_module(cls)


for pkg in ['cern.lsa.domain.settings',
            'cern.lsa.domain.settings.type',
            'cern.lsa.domain.settings.spi',
            'cern.lsa.domain.settings.factory']:
    imp(pkg)
    stubgenj.generate_stub_for_java_module(pkg, 'pyi/%s/__init__.pyi' % pkg.replace('.', '/'))
