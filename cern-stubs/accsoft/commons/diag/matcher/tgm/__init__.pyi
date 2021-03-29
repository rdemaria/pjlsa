import cern.accsoft.commons.diag.matcher
import typing


class TgmThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    TGM_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    def __init__(self): ...
