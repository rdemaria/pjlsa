from datetime import datetime
from typing import Iterable, Union

from .. import _jpype as _jp
from ..domain import *

__all__ = ['LsaTrimService']


class LsaTrimService(object):
    def __init__(self, lsa_client):
        self._lsa = lsa_client

    def trimSettings(self):
        pass

    def revertTrim(self):
        pass

    def copySettings(self):
        pass

    def incorporate(self):
        pass

    def updateTrimDescription(self):
        pass

    def deleteTrim(self):
        pass

    def findTrimHeaders(self, contexts: Union[str, Iterable[str], Context, Iterable[Context]],
                        parameters: Union[str, Iterable[str], Parameter, Iterable[Parameter]], *,
                        since: Union[None, datetime, int, str] = None):
        resolved_contexts = self._lsa.contextService._resolve_contexts(contexts)
        beamprocesses = [bp for ctx in resolved_contexts for bp in ctx.beamProcesses]
        builder = _jp.cern.lsa.domain.settings.TrimHeadersRequest.builder()
        builder.beamProcesses(_jp.to_java_list(beamprocesses))
        builder.parameters(self._lsa.parameterService._resolve_params(parameters))
        if since is not None:
            builder.at(_jp.to_java_date(since))

        return self._lsa._trimService.findTrimHeaders(builder.build())

    def findTrimmedParameters(self):
        pass