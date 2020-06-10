from typing import Any as _py_Any
from typing import Type as _py_Type
import java.lang
import java.lang.ref


class Finalizer(java.lang.Runnable):
    def run(self) -> None: ...
    @classmethod
    def startFinalizer(cls, class_: _py_Type[_py_Any], referenceQueue: java.lang.ref.ReferenceQueue[_py_Any], phantomReference: java.lang.ref.PhantomReference[_py_Any]) -> None: ...
