from typing import ClassVar as _py_ClassVar
import java.util


class DefaultDateFormatter:
    FORMAT: _py_ClassVar[str] = ...
    @classmethod
    def format(cls, date: java.util.Date) -> str: ...
    @classmethod
    def parse(cls, string: str) -> java.util.Date: ...
