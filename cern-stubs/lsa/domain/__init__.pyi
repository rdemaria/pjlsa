from typing import overload
import java.lang


class LsaException(java.lang.Exception):
    @overload
    def __init__(self, exception: java.lang.Exception): ...
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, exception: java.lang.Exception): ...
