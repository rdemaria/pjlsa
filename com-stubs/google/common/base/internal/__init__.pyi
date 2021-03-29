import java.lang
import java.lang.ref
import typing


class Finalizer(java.lang.Runnable):
    def run(self) -> None: ...
    @staticmethod
    def startFinalizer(class_: typing.Type[typing.Any], referenceQueue: java.lang.ref.ReferenceQueue[typing.Any], phantomReference: java.lang.ref.PhantomReference[typing.Any]) -> None: ...
