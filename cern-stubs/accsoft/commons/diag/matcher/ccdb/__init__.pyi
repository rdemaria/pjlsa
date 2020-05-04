from typing import ClassVar as _py_ClassVar
import cern.accsoft.commons.diag.matcher


class CcdbThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    CCDB_PROBLEM_DOMAIN: _py_ClassVar[str] = ...
    def __init__(self): ...
