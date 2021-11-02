import typing



class RegexpUtils:
    def __init__(self): ...
    @staticmethod
    def escapeSpecialCharacters(string: str) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.regexp")``.

    RegexpUtils: typing.Type[RegexpUtils]
