import java.util
import typing


class DefaultDateFormatter:
    FORMAT: typing.ClassVar[str] = ...
    @staticmethod
    def format(date: java.util.Date) -> str: ...
    @staticmethod
    def parse(string: str) -> java.util.Date: ...
