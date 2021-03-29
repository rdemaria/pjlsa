import java.lang
import java.util.concurrent
import typing


class DefaultThreadFactory(java.util.concurrent.ThreadFactory):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, boolean: bool): ...
    def newThread(self, runnable: typing.Union[java.lang.Runnable, typing.Callable]) -> java.lang.Thread: ...
