from typing import Iterable, Union, Optional, List
from ..util import *
from .. import _jpype as _jp
from ..domain import *
from datetime import datetime

__all__ = ['LsaParameterService']


class LsaParameterService(object):
    def findParameters(self, names: Union[str, Iterable[str], None] = None, *,
                       accelerator: Union[str, CernAccelerator, None] = None,
                       acceleratorZones: Union[str, Iterable[str], None] = None,
                       ):
        pass

    def findParametersForEditing(self):
        pass

    def findParameterTypes(self):
        pass

    def findHierarchies(self):
        pass

    def saveParameters(self):
        pass

    def saveParameterRelations(self):
        pass

    def saveParameterTypes(self):
        pass

    def deleteParameterTypes(self):
        pass

    def deleteParameters(self):
        pass

    def saveCriticalProperty(self):
        pass

    def deleteCriticalProperty(self):
        pass

    def findParameterGroups(self):
        pass

    def saveParameterGroup(self):
        pass

    def deleteParameterGroup(self):
        pass

    def addParametersToParameterGroup(self):
        pass

    def removeParametersFromParameterGroup(self):
        pass

    def findMakeRuleForParameterRelation(self):
        pass

    def findParameterTrees(self):
        pass

    def getMaxDelta(self):
        pass
