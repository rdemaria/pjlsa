import java.io
import java.lang
import java.lang.reflect
import java.nio
import java.util
import typing



class CallSite:
    """
    Java class 'java.lang.invoke.CallSite'
    
        Extends:
            java.lang.Object
    
    """
    def dynamicInvoker(self) -> 'MethodHandle': ...
    def getTarget(self) -> 'MethodHandle': ...
    def setTarget(self, methodHandle: 'MethodHandle') -> None: ...
    def type(self) -> 'MethodType': ...

class ConstantBootstraps:
    """
    Java class 'java.lang.invoke.ConstantBootstraps'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ConstantBootstraps()
    
    """
    def __init__(self): ...
    @staticmethod
    def arrayVarHandle(lookup: 'MethodHandles.Lookup', string: str, class_: typing.Type['VarHandle'], class2: typing.Type[typing.Any]) -> 'VarHandle': ...
    _enumConstant__E = typing.TypeVar('_enumConstant__E', bound=java.lang.Enum)  # <E>
    @staticmethod
    def enumConstant(lookup: 'MethodHandles.Lookup', string: str, class_: typing.Type[_enumConstant__E]) -> _enumConstant__E: ...
    @staticmethod
    def fieldVarHandle(lookup: 'MethodHandles.Lookup', string: str, class_: typing.Type['VarHandle'], class2: typing.Type[typing.Any], class3: typing.Type[typing.Any]) -> 'VarHandle': ...
    @typing.overload
    @staticmethod
    def getStaticFinal(lookup: 'MethodHandles.Lookup', string: str, class_: typing.Type[typing.Any]) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def getStaticFinal(lookup: 'MethodHandles.Lookup', string: str, class_: typing.Type[typing.Any], class2: typing.Type[typing.Any]) -> typing.Any: ...
    @staticmethod
    def invoke(lookup: 'MethodHandles.Lookup', string: str, class_: typing.Type[typing.Any], methodHandle: 'MethodHandle', objectArray: typing.List[typing.Any]) -> typing.Any: ...
    @staticmethod
    def nullConstant(lookup: 'MethodHandles.Lookup', string: str, class_: typing.Type[typing.Any]) -> typing.Any: ...
    @staticmethod
    def primitiveClass(lookup: 'MethodHandles.Lookup', string: str, class_: typing.Type[typing.Any]) -> typing.Type[typing.Any]: ...
    @staticmethod
    def staticFieldVarHandle(lookup: 'MethodHandles.Lookup', string: str, class_: typing.Type['VarHandle'], class2: typing.Type[typing.Any], class3: typing.Type[typing.Any]) -> 'VarHandle': ...

class LambdaConversionException(java.lang.Exception):
    """
    Java class 'java.lang.invoke.LambdaConversionException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * LambdaConversionException(java.lang.String, java.lang.Throwable, boolean, boolean)
        * LambdaConversionException(java.lang.Throwable)
        * LambdaConversionException(java.lang.String, java.lang.Throwable)
        * LambdaConversionException(java.lang.String)
        * LambdaConversionException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class LambdaMetafactory:
    """
    Java class 'java.lang.invoke.LambdaMetafactory'
    
        Extends:
            java.lang.Object
    
      Attributes:
        FLAG_SERIALIZABLE (int): final static field
        FLAG_MARKERS (int): final static field
        FLAG_BRIDGES (int): final static field
    
    """
    FLAG_SERIALIZABLE: typing.ClassVar[int] = ...
    FLAG_MARKERS: typing.ClassVar[int] = ...
    FLAG_BRIDGES: typing.ClassVar[int] = ...
    @staticmethod
    def altMetafactory(lookup: 'MethodHandles.Lookup', string: str, methodType: 'MethodType', objectArray: typing.List[typing.Any]) -> CallSite: ...
    @staticmethod
    def metafactory(lookup: 'MethodHandles.Lookup', string: str, methodType: 'MethodType', methodType2: 'MethodType', methodHandle: 'MethodHandle', methodType3: 'MethodType') -> CallSite: ...

class MethodHandle:
    """
    Java class 'java.lang.invoke.MethodHandle'
    
        Extends:
            java.lang.Object
    
    """
    @typing.overload
    def asCollector(self, int: int, class_: typing.Type[typing.Any], int2: int) -> 'MethodHandle': ...
    @typing.overload
    def asCollector(self, class_: typing.Type[typing.Any], int: int) -> 'MethodHandle': ...
    def asFixedArity(self) -> 'MethodHandle': ...
    @typing.overload
    def asSpreader(self, int: int, class_: typing.Type[typing.Any], int2: int) -> 'MethodHandle': ...
    @typing.overload
    def asSpreader(self, class_: typing.Type[typing.Any], int: int) -> 'MethodHandle': ...
    def asType(self, methodType: 'MethodType') -> 'MethodHandle': ...
    def asVarargsCollector(self, class_: typing.Type[typing.Any]) -> 'MethodHandle': ...
    def bindTo(self, object: typing.Any) -> 'MethodHandle': ...
    def invoke(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def invokeExact(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    @typing.overload
    def invokeWithArguments(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    @typing.overload
    def invokeWithArguments(self, list: java.util.List[typing.Any]) -> typing.Any: ...
    def isVarargsCollector(self) -> bool: ...
    def toString(self) -> str: ...
    def type(self) -> 'MethodType': ...
    def withVarargs(self, boolean: bool) -> 'MethodHandle': ...

class MethodHandleInfo:
    """
    Java class 'java.lang.invoke.MethodHandleInfo'
    
      Attributes:
        REF_getField (int): final static field
        REF_getStatic (int): final static field
        REF_putField (int): final static field
        REF_putStatic (int): final static field
        REF_invokeVirtual (int): final static field
        REF_invokeStatic (int): final static field
        REF_invokeSpecial (int): final static field
        REF_newInvokeSpecial (int): final static field
        REF_invokeInterface (int): final static field
    
    """
    REF_getField: typing.ClassVar[int] = ...
    REF_getStatic: typing.ClassVar[int] = ...
    REF_putField: typing.ClassVar[int] = ...
    REF_putStatic: typing.ClassVar[int] = ...
    REF_invokeVirtual: typing.ClassVar[int] = ...
    REF_invokeStatic: typing.ClassVar[int] = ...
    REF_invokeSpecial: typing.ClassVar[int] = ...
    REF_newInvokeSpecial: typing.ClassVar[int] = ...
    REF_invokeInterface: typing.ClassVar[int] = ...
    def getDeclaringClass(self) -> typing.Type[typing.Any]: ...
    def getMethodType(self) -> 'MethodType': ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getReferenceKind(self) -> int: ...
    def isVarArgs(self) -> bool: ...
    @staticmethod
    def referenceKindToString(int: int) -> str: ...
    _reflectAs__T = typing.TypeVar('_reflectAs__T', bound=java.lang.reflect.Member)  # <T>
    def reflectAs(self, class_: typing.Type[_reflectAs__T], lookup: 'MethodHandles.Lookup') -> _reflectAs__T: ...
    @staticmethod
    def toString(int: int, class_: typing.Type[typing.Any], string: str, methodType: 'MethodType') -> str: ...

class MethodHandleProxies:
    """
    Java class 'java.lang.invoke.MethodHandleProxies'
    
        Extends:
            java.lang.Object
    
    """
    _asInterfaceInstance__T = typing.TypeVar('_asInterfaceInstance__T')  # <T>
    @staticmethod
    def asInterfaceInstance(class_: typing.Type[_asInterfaceInstance__T], methodHandle: MethodHandle) -> _asInterfaceInstance__T: ...
    @staticmethod
    def isWrapperInstance(object: typing.Any) -> bool: ...
    @staticmethod
    def wrapperInstanceTarget(object: typing.Any) -> MethodHandle: ...
    @staticmethod
    def wrapperInstanceType(object: typing.Any) -> typing.Type[typing.Any]: ...

class MethodHandles:
    """
    Java class 'java.lang.invoke.MethodHandles'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def arrayConstructor(class_: typing.Type[typing.Any]) -> MethodHandle: ...
    @staticmethod
    def arrayElementGetter(class_: typing.Type[typing.Any]) -> MethodHandle: ...
    @staticmethod
    def arrayElementSetter(class_: typing.Type[typing.Any]) -> MethodHandle: ...
    @staticmethod
    def arrayElementVarHandle(class_: typing.Type[typing.Any]) -> 'VarHandle': ...
    @staticmethod
    def arrayLength(class_: typing.Type[typing.Any]) -> MethodHandle: ...
    @staticmethod
    def byteArrayViewVarHandle(class_: typing.Type[typing.Any], byteOrder: java.nio.ByteOrder) -> 'VarHandle': ...
    @staticmethod
    def byteBufferViewVarHandle(class_: typing.Type[typing.Any], byteOrder: java.nio.ByteOrder) -> 'VarHandle': ...
    @staticmethod
    def catchException(methodHandle: MethodHandle, class_: typing.Type[java.lang.Throwable], methodHandle2: MethodHandle) -> MethodHandle: ...
    @staticmethod
    def collectArguments(methodHandle: MethodHandle, int: int, methodHandle2: MethodHandle) -> MethodHandle: ...
    @staticmethod
    def constant(class_: typing.Type[typing.Any], object: typing.Any) -> MethodHandle: ...
    @typing.overload
    @staticmethod
    def countedLoop(methodHandle: MethodHandle, methodHandle2: MethodHandle, methodHandle3: MethodHandle) -> MethodHandle: ...
    @typing.overload
    @staticmethod
    def countedLoop(methodHandle: MethodHandle, methodHandle2: MethodHandle, methodHandle3: MethodHandle, methodHandle4: MethodHandle) -> MethodHandle: ...
    @staticmethod
    def doWhileLoop(methodHandle: MethodHandle, methodHandle2: MethodHandle, methodHandle3: MethodHandle) -> MethodHandle: ...
    @typing.overload
    @staticmethod
    def dropArguments(methodHandle: MethodHandle, int: int, classArray: typing.List[typing.Type[typing.Any]]) -> MethodHandle: ...
    @typing.overload
    @staticmethod
    def dropArguments(methodHandle: MethodHandle, int: int, list: java.util.List[typing.Type[typing.Any]]) -> MethodHandle: ...
    @staticmethod
    def dropArgumentsToMatch(methodHandle: MethodHandle, int: int, list: java.util.List[typing.Type[typing.Any]], int2: int) -> MethodHandle: ...
    @staticmethod
    def empty(methodType: 'MethodType') -> MethodHandle: ...
    @staticmethod
    def exactInvoker(methodType: 'MethodType') -> MethodHandle: ...
    @staticmethod
    def explicitCastArguments(methodHandle: MethodHandle, methodType: 'MethodType') -> MethodHandle: ...
    @staticmethod
    def filterArguments(methodHandle: MethodHandle, int: int, methodHandleArray: typing.List[MethodHandle]) -> MethodHandle: ...
    @staticmethod
    def filterReturnValue(methodHandle: MethodHandle, methodHandle2: MethodHandle) -> MethodHandle: ...
    @typing.overload
    @staticmethod
    def foldArguments(methodHandle: MethodHandle, int: int, methodHandle2: MethodHandle) -> MethodHandle: ...
    @typing.overload
    @staticmethod
    def foldArguments(methodHandle: MethodHandle, methodHandle2: MethodHandle) -> MethodHandle: ...
    @staticmethod
    def guardWithTest(methodHandle: MethodHandle, methodHandle2: MethodHandle, methodHandle3: MethodHandle) -> MethodHandle: ...
    @staticmethod
    def identity(class_: typing.Type[typing.Any]) -> MethodHandle: ...
    @staticmethod
    def insertArguments(methodHandle: MethodHandle, int: int, objectArray: typing.List[typing.Any]) -> MethodHandle: ...
    @staticmethod
    def invoker(methodType: 'MethodType') -> MethodHandle: ...
    @staticmethod
    def iteratedLoop(methodHandle: MethodHandle, methodHandle2: MethodHandle, methodHandle3: MethodHandle) -> MethodHandle: ...
    @staticmethod
    def lookup() -> 'MethodHandles.Lookup': ...
    @staticmethod
    def loop(methodHandleArray: typing.List[typing.List[MethodHandle]]) -> MethodHandle: ...
    @staticmethod
    def permuteArguments(methodHandle: MethodHandle, methodType: 'MethodType', intArray: typing.List[int]) -> MethodHandle: ...
    @staticmethod
    def privateLookupIn(class_: typing.Type[typing.Any], lookup: 'MethodHandles.Lookup') -> 'MethodHandles.Lookup': ...
    @staticmethod
    def publicLookup() -> 'MethodHandles.Lookup': ...
    _reflectAs__T = typing.TypeVar('_reflectAs__T', bound=java.lang.reflect.Member)  # <T>
    @staticmethod
    def reflectAs(class_: typing.Type[_reflectAs__T], methodHandle: MethodHandle) -> _reflectAs__T: ...
    @staticmethod
    def spreadInvoker(methodType: 'MethodType', int: int) -> MethodHandle: ...
    @staticmethod
    def throwException(class_: typing.Type[typing.Any], class2: typing.Type[java.lang.Throwable]) -> MethodHandle: ...
    @staticmethod
    def tryFinally(methodHandle: MethodHandle, methodHandle2: MethodHandle) -> MethodHandle: ...
    @staticmethod
    def varHandleExactInvoker(accessMode: 'VarHandle.AccessMode', methodType: 'MethodType') -> MethodHandle: ...
    @staticmethod
    def varHandleInvoker(accessMode: 'VarHandle.AccessMode', methodType: 'MethodType') -> MethodHandle: ...
    @staticmethod
    def whileLoop(methodHandle: MethodHandle, methodHandle2: MethodHandle, methodHandle3: MethodHandle) -> MethodHandle: ...
    @staticmethod
    def zero(class_: typing.Type[typing.Any]) -> MethodHandle: ...
    class Lookup:
        """
        Java class 'java.lang.invoke.MethodHandles$Lookup'
        
            Extends:
                java.lang.Object
        
          Attributes:
            PUBLIC (int): final static field
            PRIVATE (int): final static field
            PROTECTED (int): final static field
            PACKAGE (int): final static field
            MODULE (int): final static field
            UNCONDITIONAL (int): final static field
        
        """
        PUBLIC: typing.ClassVar[int] = ...
        PRIVATE: typing.ClassVar[int] = ...
        PROTECTED: typing.ClassVar[int] = ...
        PACKAGE: typing.ClassVar[int] = ...
        MODULE: typing.ClassVar[int] = ...
        UNCONDITIONAL: typing.ClassVar[int] = ...
        def accessClass(self, class_: typing.Type[typing.Any]) -> typing.Type[typing.Any]: ...
        def bind(self, object: typing.Any, string: str, methodType: 'MethodType') -> MethodHandle: ...
        def defineClass(self, byteArray: typing.List[int]) -> typing.Type[typing.Any]: ...
        def dropLookupMode(self, int: int) -> 'MethodHandles.Lookup': ...
        def findClass(self, string: str) -> typing.Type[typing.Any]: ...
        def findConstructor(self, class_: typing.Type[typing.Any], methodType: 'MethodType') -> MethodHandle: ...
        def findGetter(self, class_: typing.Type[typing.Any], string: str, class2: typing.Type[typing.Any]) -> MethodHandle: ...
        def findSetter(self, class_: typing.Type[typing.Any], string: str, class2: typing.Type[typing.Any]) -> MethodHandle: ...
        def findSpecial(self, class_: typing.Type[typing.Any], string: str, methodType: 'MethodType', class2: typing.Type[typing.Any]) -> MethodHandle: ...
        def findStatic(self, class_: typing.Type[typing.Any], string: str, methodType: 'MethodType') -> MethodHandle: ...
        def findStaticGetter(self, class_: typing.Type[typing.Any], string: str, class2: typing.Type[typing.Any]) -> MethodHandle: ...
        def findStaticSetter(self, class_: typing.Type[typing.Any], string: str, class2: typing.Type[typing.Any]) -> MethodHandle: ...
        def findStaticVarHandle(self, class_: typing.Type[typing.Any], string: str, class2: typing.Type[typing.Any]) -> 'VarHandle': ...
        def findVarHandle(self, class_: typing.Type[typing.Any], string: str, class2: typing.Type[typing.Any]) -> 'VarHandle': ...
        def findVirtual(self, class_: typing.Type[typing.Any], string: str, methodType: 'MethodType') -> MethodHandle: ...
        def hasPrivateAccess(self) -> bool: ...
        def lookupClass(self) -> typing.Type[typing.Any]: ...
        def lookupModes(self) -> int: ...
        def revealDirect(self, methodHandle: MethodHandle) -> MethodHandleInfo: ...
        def toString(self) -> str: ...
        def unreflect(self, method: java.lang.reflect.Method) -> MethodHandle: ...
        def unreflectConstructor(self, constructor: java.lang.reflect.Constructor[typing.Any]) -> MethodHandle: ...
        def unreflectGetter(self, field: java.lang.reflect.Field) -> MethodHandle: ...
        def unreflectSetter(self, field: java.lang.reflect.Field) -> MethodHandle: ...
        def unreflectSpecial(self, method: java.lang.reflect.Method, class_: typing.Type[typing.Any]) -> MethodHandle: ...
        def unreflectVarHandle(self, field: java.lang.reflect.Field) -> 'VarHandle': ...

class MethodType(java.io.Serializable):
    """
    Java class 'java.lang.invoke.MethodType'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
    """
    @typing.overload
    def appendParameterTypes(self, classArray: typing.List[typing.Type[typing.Any]]) -> 'MethodType': ...
    @typing.overload
    def appendParameterTypes(self, list: java.util.List[typing.Type[typing.Any]]) -> 'MethodType': ...
    def changeParameterType(self, int: int, class_: typing.Type[typing.Any]) -> 'MethodType': ...
    def changeReturnType(self, class_: typing.Type[typing.Any]) -> 'MethodType': ...
    def dropParameterTypes(self, int: int, int2: int) -> 'MethodType': ...
    def equals(self, object: typing.Any) -> bool: ...
    def erase(self) -> 'MethodType': ...
    @staticmethod
    def fromMethodDescriptorString(string: str, classLoader: java.lang.ClassLoader) -> 'MethodType': ...
    def generic(self) -> 'MethodType': ...
    @typing.overload
    @staticmethod
    def genericMethodType(int: int) -> 'MethodType': ...
    @typing.overload
    @staticmethod
    def genericMethodType(int: int, boolean: bool) -> 'MethodType': ...
    def hasPrimitives(self) -> bool: ...
    def hasWrappers(self) -> bool: ...
    def hashCode(self) -> int: ...
    @typing.overload
    def insertParameterTypes(self, int: int, classArray: typing.List[typing.Type[typing.Any]]) -> 'MethodType': ...
    @typing.overload
    def insertParameterTypes(self, int: int, list: java.util.List[typing.Type[typing.Any]]) -> 'MethodType': ...
    def lastParameterType(self) -> typing.Type[typing.Any]: ...
    @typing.overload
    @staticmethod
    def methodType(class_: typing.Type[typing.Any]) -> 'MethodType': ...
    @typing.overload
    @staticmethod
    def methodType(class_: typing.Type[typing.Any], class2: typing.Type[typing.Any]) -> 'MethodType': ...
    @typing.overload
    @staticmethod
    def methodType(class_: typing.Type[typing.Any], class2: typing.Type[typing.Any], classArray: typing.List[typing.Type[typing.Any]]) -> 'MethodType': ...
    @typing.overload
    @staticmethod
    def methodType(class_: typing.Type[typing.Any], classArray: typing.List[typing.Type[typing.Any]]) -> 'MethodType': ...
    @typing.overload
    @staticmethod
    def methodType(class_: typing.Type[typing.Any], methodType: 'MethodType') -> 'MethodType': ...
    @typing.overload
    @staticmethod
    def methodType(class_: typing.Type[typing.Any], list: java.util.List[typing.Type[typing.Any]]) -> 'MethodType': ...
    def parameterArray(self) -> typing.List[typing.Type[typing.Any]]: ...
    def parameterCount(self) -> int: ...
    def parameterList(self) -> java.util.List[typing.Type[typing.Any]]: ...
    def parameterType(self, int: int) -> typing.Type[typing.Any]: ...
    def returnType(self) -> typing.Type[typing.Any]: ...
    def toMethodDescriptorString(self) -> str: ...
    def toString(self) -> str: ...
    def unwrap(self) -> 'MethodType': ...
    def wrap(self) -> 'MethodType': ...

class SerializedLambda(java.io.Serializable):
    """
    Java class 'java.lang.invoke.SerializedLambda'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * SerializedLambda(java.lang.Class, java.lang.String, java.lang.String, java.lang.String, int, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.Object[])
    
    """
    def __init__(self, class_: typing.Type[typing.Any], string: str, string2: str, string3: str, int: int, string4: str, string5: str, string6: str, string7: str, objectArray: typing.List[typing.Any]): ...
    def getCapturedArg(self, int: int) -> typing.Any: ...
    def getCapturedArgCount(self) -> int: ...
    def getCapturingClass(self) -> str: ...
    def getFunctionalInterfaceClass(self) -> str: ...
    def getFunctionalInterfaceMethodName(self) -> str: ...
    def getFunctionalInterfaceMethodSignature(self) -> str: ...
    def getImplClass(self) -> str: ...
    def getImplMethodKind(self) -> int: ...
    def getImplMethodName(self) -> str: ...
    def getImplMethodSignature(self) -> str: ...
    def getInstantiatedMethodType(self) -> str: ...
    def toString(self) -> str: ...

class StringConcatException(java.lang.Exception):
    """
    Java class 'java.lang.invoke.StringConcatException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * StringConcatException(java.lang.String)
        * StringConcatException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...

class StringConcatFactory:
    """
    Java class 'java.lang.invoke.StringConcatFactory'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def makeConcat(lookup: MethodHandles.Lookup, string: str, methodType: MethodType) -> CallSite: ...
    @staticmethod
    def makeConcatWithConstants(lookup: MethodHandles.Lookup, string: str, methodType: MethodType, string2: str, objectArray: typing.List[typing.Any]) -> CallSite: ...

class SwitchPoint:
    """
    Java class 'java.lang.invoke.SwitchPoint'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SwitchPoint()
    
    """
    def __init__(self): ...
    def guardWithTest(self, methodHandle: MethodHandle, methodHandle2: MethodHandle) -> MethodHandle: ...
    def hasBeenInvalidated(self) -> bool: ...
    @staticmethod
    def invalidateAll(switchPointArray: typing.List['SwitchPoint']) -> None: ...

class VarHandle:
    """
    Java class 'java.lang.invoke.VarHandle'
    
        Extends:
            java.lang.Object
    
    """
    def accessModeType(self, accessMode: 'VarHandle.AccessMode') -> MethodType: ...
    @staticmethod
    def acquireFence() -> None: ...
    def compareAndExchange(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def compareAndExchangeAcquire(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def compareAndExchangeRelease(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def compareAndSet(self, objectArray: typing.List[typing.Any]) -> bool: ...
    def coordinateTypes(self) -> java.util.List[typing.Type[typing.Any]]: ...
    @staticmethod
    def fullFence() -> None: ...
    def get(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAcquire(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndAdd(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndAddAcquire(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndAddRelease(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndBitwiseAnd(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndBitwiseAndAcquire(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndBitwiseAndRelease(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndBitwiseOr(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndBitwiseOrAcquire(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndBitwiseOrRelease(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndBitwiseXor(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndBitwiseXorAcquire(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndBitwiseXorRelease(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndSet(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndSetAcquire(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getAndSetRelease(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getOpaque(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def getVolatile(self, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def isAccessModeSupported(self, accessMode: 'VarHandle.AccessMode') -> bool: ...
    @staticmethod
    def loadLoadFence() -> None: ...
    @staticmethod
    def releaseFence() -> None: ...
    def set(self, objectArray: typing.List[typing.Any]) -> None: ...
    def setOpaque(self, objectArray: typing.List[typing.Any]) -> None: ...
    def setRelease(self, objectArray: typing.List[typing.Any]) -> None: ...
    def setVolatile(self, objectArray: typing.List[typing.Any]) -> None: ...
    @staticmethod
    def storeStoreFence() -> None: ...
    def toMethodHandle(self, accessMode: 'VarHandle.AccessMode') -> MethodHandle: ...
    def varType(self) -> typing.Type[typing.Any]: ...
    def weakCompareAndSet(self, objectArray: typing.List[typing.Any]) -> bool: ...
    def weakCompareAndSetAcquire(self, objectArray: typing.List[typing.Any]) -> bool: ...
    def weakCompareAndSetPlain(self, objectArray: typing.List[typing.Any]) -> bool: ...
    def weakCompareAndSetRelease(self, objectArray: typing.List[typing.Any]) -> bool: ...
    class AccessMode(java.lang.Enum['VarHandle.AccessMode']):
        """
        Java class 'java.lang.invoke.VarHandle$AccessMode'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            GET (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            SET (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_VOLATILE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            SET_VOLATILE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_ACQUIRE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            SET_RELEASE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_OPAQUE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            SET_OPAQUE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            COMPARE_AND_SET (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            COMPARE_AND_EXCHANGE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            COMPARE_AND_EXCHANGE_ACQUIRE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            COMPARE_AND_EXCHANGE_RELEASE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            WEAK_COMPARE_AND_SET_PLAIN (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            WEAK_COMPARE_AND_SET (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            WEAK_COMPARE_AND_SET_ACQUIRE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            WEAK_COMPARE_AND_SET_RELEASE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_SET (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_SET_ACQUIRE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_SET_RELEASE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_ADD (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_ADD_ACQUIRE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_ADD_RELEASE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_BITWISE_OR (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_BITWISE_OR_RELEASE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_BITWISE_OR_ACQUIRE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_BITWISE_AND (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_BITWISE_AND_RELEASE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_BITWISE_AND_ACQUIRE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_BITWISE_XOR (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_BITWISE_XOR_RELEASE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
            GET_AND_BITWISE_XOR_ACQUIRE (java.lang.invoke.VarHandle$AccessMode): final static enum constant
        
        """
        GET: typing.ClassVar['VarHandle.AccessMode'] = ...
        SET: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_VOLATILE: typing.ClassVar['VarHandle.AccessMode'] = ...
        SET_VOLATILE: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_ACQUIRE: typing.ClassVar['VarHandle.AccessMode'] = ...
        SET_RELEASE: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_OPAQUE: typing.ClassVar['VarHandle.AccessMode'] = ...
        SET_OPAQUE: typing.ClassVar['VarHandle.AccessMode'] = ...
        COMPARE_AND_SET: typing.ClassVar['VarHandle.AccessMode'] = ...
        COMPARE_AND_EXCHANGE: typing.ClassVar['VarHandle.AccessMode'] = ...
        COMPARE_AND_EXCHANGE_ACQUIRE: typing.ClassVar['VarHandle.AccessMode'] = ...
        COMPARE_AND_EXCHANGE_RELEASE: typing.ClassVar['VarHandle.AccessMode'] = ...
        WEAK_COMPARE_AND_SET_PLAIN: typing.ClassVar['VarHandle.AccessMode'] = ...
        WEAK_COMPARE_AND_SET: typing.ClassVar['VarHandle.AccessMode'] = ...
        WEAK_COMPARE_AND_SET_ACQUIRE: typing.ClassVar['VarHandle.AccessMode'] = ...
        WEAK_COMPARE_AND_SET_RELEASE: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_SET: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_SET_ACQUIRE: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_SET_RELEASE: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_ADD: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_ADD_ACQUIRE: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_ADD_RELEASE: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_BITWISE_OR: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_BITWISE_OR_RELEASE: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_BITWISE_OR_ACQUIRE: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_BITWISE_AND: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_BITWISE_AND_RELEASE: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_BITWISE_AND_ACQUIRE: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_BITWISE_XOR: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_BITWISE_XOR_RELEASE: typing.ClassVar['VarHandle.AccessMode'] = ...
        GET_AND_BITWISE_XOR_ACQUIRE: typing.ClassVar['VarHandle.AccessMode'] = ...
        def methodName(self) -> str: ...
        @staticmethod
        def valueFromMethodName(string: str) -> 'VarHandle.AccessMode': ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'VarHandle.AccessMode': ...
        @staticmethod
        def values() -> typing.List['VarHandle.AccessMode']: ...

class WrongMethodTypeException(java.lang.RuntimeException):
    """
    Java class 'java.lang.invoke.WrongMethodTypeException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * WrongMethodTypeException(java.lang.String)
        * WrongMethodTypeException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class ConstantCallSite(CallSite):
    """
    Java class 'java.lang.invoke.ConstantCallSite'
    
        Extends:
            java.lang.invoke.CallSite
    
      Constructors:
        * ConstantCallSite(java.lang.invoke.MethodHandle)
    
    """
    def __init__(self, methodHandle: MethodHandle): ...
    def dynamicInvoker(self) -> MethodHandle: ...
    def getTarget(self) -> MethodHandle: ...
    def setTarget(self, methodHandle: MethodHandle) -> None: ...

class MutableCallSite(CallSite):
    """
    Java class 'java.lang.invoke.MutableCallSite'
    
        Extends:
            java.lang.invoke.CallSite
    
      Constructors:
        * MutableCallSite(java.lang.invoke.MethodType)
        * MutableCallSite(java.lang.invoke.MethodHandle)
    
    """
    @typing.overload
    def __init__(self, methodHandle: MethodHandle): ...
    @typing.overload
    def __init__(self, methodType: MethodType): ...
    def dynamicInvoker(self) -> MethodHandle: ...
    def getTarget(self) -> MethodHandle: ...
    def setTarget(self, methodHandle: MethodHandle) -> None: ...
    @staticmethod
    def syncAll(mutableCallSiteArray: typing.List['MutableCallSite']) -> None: ...

class VolatileCallSite(CallSite):
    """
    Java class 'java.lang.invoke.VolatileCallSite'
    
        Extends:
            java.lang.invoke.CallSite
    
      Constructors:
        * VolatileCallSite(java.lang.invoke.MethodType)
        * VolatileCallSite(java.lang.invoke.MethodHandle)
    
    """
    @typing.overload
    def __init__(self, methodHandle: MethodHandle): ...
    @typing.overload
    def __init__(self, methodType: MethodType): ...
    def dynamicInvoker(self) -> MethodHandle: ...
    def getTarget(self) -> MethodHandle: ...
    def setTarget(self, methodHandle: MethodHandle) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.lang.invoke")``.

    CallSite: typing.Type[CallSite]
    ConstantBootstraps: typing.Type[ConstantBootstraps]
    ConstantCallSite: typing.Type[ConstantCallSite]
    LambdaConversionException: typing.Type[LambdaConversionException]
    LambdaMetafactory: typing.Type[LambdaMetafactory]
    MethodHandle: typing.Type[MethodHandle]
    MethodHandleInfo: typing.Type[MethodHandleInfo]
    MethodHandleProxies: typing.Type[MethodHandleProxies]
    MethodHandles: typing.Type[MethodHandles]
    MethodType: typing.Type[MethodType]
    MutableCallSite: typing.Type[MutableCallSite]
    SerializedLambda: typing.Type[SerializedLambda]
    StringConcatException: typing.Type[StringConcatException]
    StringConcatFactory: typing.Type[StringConcatFactory]
    SwitchPoint: typing.Type[SwitchPoint]
    VarHandle: typing.Type[VarHandle]
    VolatileCallSite: typing.Type[VolatileCallSite]
    WrongMethodTypeException: typing.Type[WrongMethodTypeException]
