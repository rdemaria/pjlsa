from typing import overload
import java.lang
import java.util.concurrent


class DefaultThreadFactory(java.util.concurrent.ThreadFactory):
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, boolean: bool): ...
    def newThread(self, runnable: java.lang.Runnable) -> java.lang.Thread: ...
