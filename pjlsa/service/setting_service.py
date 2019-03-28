from typing import Iterable, Union, Optional, List, Set, Mapping
from .._util import *
from .. import _jpype as _jp
from ..domain import *
from datetime import datetime

__all__ = ['LsaSettingService']


class LsaSettingService(object):
    def __init__(self, lsa_client):
        self._lsa = lsa_client

    def findContextSettings(self, context: Union[str, StandAloneContext], *,
                            parameters: Union[str, Iterable[str], Parameter, Iterable[Parameter]] = None,
                            at: Union[datetime, int, str] = None) -> ContextSettings:
        builder = _jp.cern.lsa.domain.settings.ContextSettingsRequest.builder()
        builder.standAloneContext(self._lsa.contextService._resolve_context(context))
        if parameters is not None:
            builder.parameters(self._lsa.parameterService._resolve_params(parameters))
        if at is not None:
            builder.at(_jp.to_java_date(at))

        return self._lsa._settingService.findContextSettings(builder.build())

    def findNotIncorporatedParameters(self, *, sourceBp: Union[str, StandAloneBeamProcess], sourcePoint: int,
                                      destinationBp: Union[str, BeamProcess], destinationPoint: int = 0):
        return self._lsa._settingService.findNotIncorporatedParameters(
            self._lsa.contextService._resolve_context(sourceBp), sourcePoint,
            self._lsa.contextService._resolve_context(destinationBp), destinationPoint)
