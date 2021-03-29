import cern.accsoft.commons.diag.matcher
import typing


class CcdbThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    CCDB_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    def __init__(self): ...
