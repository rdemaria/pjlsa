import cmmnbuild_dep_manager
import re
from typing import Set, List, Tuple, Mapping

# ------ JPype SETUP ------
mgr = cmmnbuild_dep_manager.Manager('pjlsa')
jpype = mgr.start_jpype_jvm()


# Monkey-Patcher for LSA Java Domain Objects
class LsaCustomizer(jpype._jclass.JClassCustomizer):
    _PATCHES = {
        '__repr__': lambda self: self.__str__()
    }

    def canCustomize(self, name, jc):
        return name.startswith('cern.lsa.domain.') or name.startswith('cern.accsoft.commons.domain.')

    def customize(self, name, jc, bases, members, fields):
        members.update(LsaCustomizer._PATCHES)
        # delete accessors to fields
        for k in [k for k in members.keys() if type(members[k]) is property]:
            del members[k]
        # inline enum constants (also for pseudo-enum pojos)
        if 'values' in members and 'valueOf' in members:
            members.update({f: v for f, v in fields.items() if f not in ['$VALUES', 'mro', 'class_']})
        # expose getters and setters in a more pythonic way
        getters = {re.sub('^(get|is)(.)(.*)', lambda g: g.group(2).lower() + g.group(3), k): k
                   for k in members.keys() if k.startswith('get') or k.startswith('is')}
        setters = {re.sub('^(set)(.)(.*)', lambda g: g.group(2).lower() + g.group(3), k): k
                   for k in members.keys() if k.startswith('set')}
        for m, getter in getters.items():
            if '=> EXACT' not in members[getter].matchReport(jc):
                continue
            setter = setters[m] if m in setters else None
            wrapped_getter = LsaCustomizer._from_java(members[getter])
            wrapped_setter = LsaCustomizer._to_java(members[setter]) if setter is not None else None
            members[m] = property(wrapped_getter, wrapped_setter)
            del members[getter]
            if setter is not None:
                del members[setter]
        for methodName in members.keys():
            if isinstance(members[methodName], jpype._jclass._jpype._JavaMethod):
                members[methodName] = LsaCustomizer._from_to_java(members[methodName])

    @classmethod
    def _from_to_java(cls, accessor):
        return lambda *args: _javaToPython(accessor(*[_pythonToJava(a) for a in args]))

    @classmethod
    def _from_java(cls, accessor):
        return lambda *args: _javaToPython(accessor(*args))

    @classmethod
    def _to_java(cls, accessor):
        return lambda *args: accessor(*[_pythonToJava(a) for a in args])


def _javaToPython(value):
    if isinstance(value, java.util.Set):
        return set(value)
    if isinstance(value, java.util.List):
        return list(value)
    if isinstance(value, java.util.Map):
        return {i.getKey(): i.getValue() for i in value.entrySet()}
    if isinstance(value, java.util.Optional):
        return value.orElse(None)
    return value


def _pythonToJava(value):
    if isinstance(value, Set):
        hs = java.util.HashSet()
        for v in value:
            hs.put(_pythonToJava(v))
        return hs
    if isinstance(value, List):
        hs = java.util.ArrayList()
        for v in value:
            hs.add(_pythonToJava(v))
        return hs
    if isinstance(value, Mapping):
        hs = java.util.HashMap()
        for k, v in value.items():
            hs.put(_pythonToJava(k), _pythonToJava(v))
        return hs
    return value


# possible future - even more opportunistic - conversion
# overloads = [m for m in jpype.java.lang.Class.forName(jc.getName()).getMethods() if m.getName()==accessor.getName()]
# params = overloads[0].getParameterTypes()
# params[0].isAssignableFrom(java.lang.String)

jpype._jclass.registerClassCustomizer(LsaCustomizer())

# ------ IMPORTS ------
cern = jpype.JPackage('cern')
org = jpype.JPackage('org')
java = jpype.JPackage('java')

# General Java
System = java.lang.System

# LSA Services
ServiceLocator = cern.lsa.client.ServiceLocator

AcceleratorService = cern.lsa.client.AcceleratorService
AdService = cern.lsa.client.AdService
ArchiveReferenceService = cern.lsa.client.ArchiveReferenceService
CacheService = cern.lsa.client.CacheService
ContextService = cern.lsa.client.ContextService
DeviceService = cern.lsa.client.DeviceService
ElenaService = cern.lsa.client.ElenaService
ExploitationService = cern.lsa.client.ExploitationService
FidelService = cern.lsa.client.FidelService
GenerationService = cern.lsa.client.GenerationService
HyperCycleService = cern.lsa.client.HyperCycleService
JapcService = cern.lsa.client.JapcService
KnobService = cern.lsa.client.KnobService
LhcService = cern.lsa.client.LhcService
LktimService = cern.lsa.client.LktimService
OpticService = cern.lsa.client.OpticService
ParameterService = cern.lsa.client.ParameterService
SettingService = cern.lsa.client.SettingService
SpsService = cern.lsa.client.SpsService
TestService = cern.lsa.client.TestService
TimingService = cern.lsa.client.TimingService
TransactionService = cern.lsa.client.TransactionService
TrimService = cern.lsa.client.TrimService
WorkingSetService = cern.lsa.client.WorkingSetService

# Contexts
ContextFamily = cern.lsa.domain.settings.ContextFamily
Context = cern.lsa.domain.settings.Context
StandAloneBeamProcess = cern.lsa.domain.settings.StandAloneBeamProcess
StandAloneContext = cern.lsa.domain.settings.StandAloneContext
StandAloneCycle = cern.lsa.domain.settings.StandAloneCycle
BeamProcess = cern.lsa.domain.settings.BeamProcess
BeamProcessType = cern.lsa.domain.settings.type.BeamProcessType
BeamProcessPurpose = cern.lsa.domain.settings.type.BeamProcessPurpose
ActualBeamProcessInfo = cern.lsa.domain.settings.ActualBeamProcessInfo
UserContextMapping = cern.lsa.domain.settings.UserContextMapping
AcceleratorUser = cern.lsa.domain.settings.AcceleratorUser
AcceleratorUserGroup = cern.lsa.domain.settings.AcceleratorUserGroup
