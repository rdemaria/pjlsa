#!/usr/bin/env python3
"""Stub generator for Java modules, originally based on mypy stubgenc
"""

import jpype
import jpype.imports
from jpype._pykeywords import pysafe
import importlib
import inspect
import os.path
import re
from typing import List, Optional, Mapping, Any, Set, NamedTuple, Dict
from types import ModuleType
import pathlib

__all__ = ["generateJavaStubs"]


class TypeStr:
    __slots__ = ('name', 'typeArgs')

    def __init__(self, name: str, typeArgs: Optional[List['TypeStr']] = None):
        self.name = name
        self.typeArgs = list(typeArgs or [])

    def __repr__(self) -> str:
        return "TypeStr(name={}, typeArgs={})".format(repr(self.name), repr(self.typeArgs))


TypeVarStr = NamedTuple('TypeVarStr', [
    ('javaName', str),
    ('pythonName', str),
    ('bound', Optional[TypeStr])
])

ArgSig = NamedTuple('ArgSig', [
    ('name', str),
    ('type', Optional[TypeStr])
])

JavaFunctionSig = NamedTuple('JavaFunctionSig', [
    ('name', str),
    ('static', bool),
    ('args', List[ArgSig]),
    ('retType', TypeStr),
    ('typeVars', List[TypeVarStr])
])


def generateJavaStubs(pkgPrefixes: List[str], useStubsSuffix: bool = True, outputDir: str = '.') -> None:
    packages = {}  # type: Dict[str, List[str]]

    allClasses = findAllClasses()

    for prefix in pkgPrefixes:
        for clsName in allClasses:
            if not clsName.startswith(prefix + '.'):
                continue
            pkg_name = clsName[:clsName.rfind('.')]
            packages.setdefault(pkg_name, []).append(clsName)

    for pkg, classes in packages.items():
        print('Generating stubs for %s (%d classes)' % (pkg, len(classes)))
        if '.' in pkg:
            pkgDomain = pkg[:pkg.find('.')]
            if pkgDomain not in jpype.imports._JDOMAINS.keys():
                jpype.imports.registerDomain(pkgDomain)
        importlib.import_module(pkg)
        for cls in classes:
            try:
                importlib.import_module(cls)
            except ImportError:
                print(">> skipping class %s" % cls)
                classes.remove(cls)
        pathParts = pkg.split(".")
        if useStubsSuffix:
            pathParts[0] += "-stubs"
        path = pathlib.Path(outputDir)
        for pathPart in pathParts:
            path = path / pysafe(pathPart)
            if not path.is_dir():
                os.makedirs(path)
            initFile = path / '__init__.pyi'
            if not initFile.exists():
                open(initFile, "w").close()

        generateStubsForJavaPackage(pkg, path / '__init__.pyi')


def findAllClasses() -> List[str]:
    from java.nio.file import Paths  # noqa
    from java.net import URI  # noqa
    from java.lang import ClassLoader  # noqa
    import zipfile
    classLoader = ClassLoader.getSystemClassLoader()
    jars = [str(Paths.get(u.toURI())) for u in classLoader.getURLs()]  # noqa
    jRuntime = str(classLoader.getResource("java/lang/String.class").toURI())
    if jRuntime:
        jRuntimeUri = URI.create(str(jRuntime[4:jRuntime.index("!")]))
        jars.append(str(Paths.get(jRuntimeUri)))
    classes = []
    for jar in jars:
        if not jar.endswith(".jar"):
            continue
        names = zipfile.ZipFile(jar).namelist()
        for name in names:
            if name.endswith('.class') and '$' not in name:
                classes.append(name[:-6].replace('/', '.'))
    return classes


def generateStubsForJavaPackage(packageName: str, outputFile: str) -> None:
    module = importlib.import_module(packageName)
    subdir = os.path.dirname(outputFile)
    if subdir and not os.path.isdir(subdir):
        os.makedirs(subdir)
    importOutput = []  # type: List[str]
    classOutput = []  # type: List[str]
    javaClasses = [cls for name, cls in module.__dict__.items() if
                   not isInternal(name) and isJavaClass(cls)]  # type: List[jpype.JClass]

    done = set()  # type: Set[str]
    while javaClasses:
        javaClassesToGenerate = [c for c in javaClasses if dependenciesSatisfied(module, c, done)]
        if not javaClassesToGenerate:
            javaClassesToGenerate = javaClasses  # some inner class cases - will generate them with full names
        for cls in sorted(javaClassesToGenerate, key=lambda c: c.__name__):
            generateJavaClassStub(module.__name__, cls, classesDone=done,
                                  output=classOutput, importsOutput=importOutput)
            javaClasses.remove(cls)

    output = []
    for line in sorted(set(importOutput)):
        output.append(line)

    output.append('')
    for line in classOutput:
        output.append(line)
    output = addTypingImports(output)
    with open(outputFile, 'w') as file:
        for line in output:
            file.write('%s\n' % line)


def isInternal(name: str) -> bool:
    if name.startswith('__') and name.endswith('__'):
        return True  # python internal
    if '$' in name:
        return True  # inner class: will be generated recursively
    if '-' in name:
        return True  # package-info et al
    return False


def isJavaClass(obj: type) -> bool:
    if not isinstance(obj, jpype.JClass) or not hasattr(obj, 'class_') or not inspect.isclass(obj):
        return False
    # noinspection
    if obj.class_.isAnonymousClass() or obj.class_.isLocalClass() or obj.class_.isSynthetic():  # noqa
        return False
    return True


def dependenciesSatisfied(module: ModuleType, jClass: jpype.JClass, done: Set[str]):
    superTypes = [pythonType(b) for b in javaSuperTypes(jClass.class_)]
    for superType in superTypes:
        superTypeName = superType.name
        superTypeModule = superTypeName[:superTypeName.rindex('.')]
        if superTypeModule == module.__name__:
            superTypeLocalName = superTypeName[len(superTypeModule) + 1:]
            if superTypeLocalName not in done:
                return False
    # check dependencies of nested classes
    objDict = getattr(jClass, '__dict__')  # type: Mapping[str, Any]  # noqa
    for member in objDict.values():
        if isJavaClass(member):
            if not dependenciesSatisfied(module, member, done):
                return False
    return True


def javaSuperTypes(jClass: Any) -> List[Any]:
    superTypes = [jClass.getGenericSuperclass()] + list(jClass.getGenericInterfaces())
    if superTypes[0] is None or superTypes[0].getTypeName() == 'java.lang.Object':
        del superTypes[0]
    return superTypes


def addTypingImports(output: List[str]) -> List[str]:
    names = []
    for name in ['Any', 'Union', 'List', 'TypeVar', 'Type', 'ClassVar', 'Generic', 'Set', 'Collection', 'Mapping']:
        if any(re.search(r'\b_py_%s\b' % name, line) for line in output):
            names.append(name)
    if names:
        return ['from typing import {ti} as _py_{ti}'.format(ti=ti_name) for ti_name in names] + output
    else:
        return output[:]


def convertStrings() -> bool:
    if convertStrings.jpypeConversionFlag is None:
        from java.lang import String  # noqa
        convertStrings.jpypeConversionFlag = isinstance(String().trim(), str)
    return convertStrings.jpypeConversionFlag


convertStrings.jpypeConversionFlag = None


def translateTypeName(typeName: str, typeArgs: Optional[List[TypeStr]] = None) -> TypeStr:
    if typeName == 'void':
        return TypeStr('None')
    if typeName in ('byte', 'short', 'int', 'long', 'java.lang.Byte', 'java.lang.Short',
                    'java.lang.Integer', 'java.lang.Long'):
        return TypeStr('int')
    if typeName in ('boolean', 'java.lang.Boolean'):
        return TypeStr('bool')
    if typeName in ('double', 'float', 'java.lang.Double', 'java.lang.Float'):
        return TypeStr('float')
    if typeName in ('char', 'java.lang.Character'):
        return TypeStr('str')  # 1-character string

    if typeName == 'java.lang.String' and convertStrings():
        return TypeStr('str')
    if typeName == 'java.lang.Class':
        return TypeStr('_py_Type', typeArgs)
    if typeName == 'java.lang.Object':
        return TypeStr('_py_Any')
    return TypeStr(typeName, typeArgs)


def pythonType(jType: Any, typeVars: Optional[List[TypeVarStr]] = None) -> TypeStr:
    from java.lang.reflect import GenericArrayType, ParameterizedType, TypeVariable, WildcardType  # noqa
    if jType is None:
        return TypeStr('None')
    if typeVars is None:
        typeVars = []
    if isinstance(jType, ParameterizedType):
        return translateTypeName(str(jType.getRawType().getTypeName()),
                                 typeArgs=[pythonType(arg, typeVars) for arg in jType.getActualTypeArguments()])
    elif isinstance(jType, TypeVariable):
        jVarName = jType.getName()
        matching_vars = [tv for tv in typeVars if tv.javaName == jVarName]
        if len(matching_vars) == 1:
            return TypeStr(matching_vars[0].pythonName)
        jBound = jType.getBounds()[0]
        if isinstance(jBound, ParameterizedType):
            jBound = jBound.getRawType()
        return pythonType(jBound, typeVars)
    elif isinstance(jType, WildcardType):
        jBound = jType.getUpperBounds()[0]
        if jBound.getTypeName() == 'java.lang.Object':
            jLowerBounds = jType.getLowerBounds()
            if jLowerBounds:
                jBound = jLowerBounds[0]
        return pythonType(jBound, typeVars)
    elif isinstance(jType, GenericArrayType):
        return TypeStr('_py_List', [pythonType(jType.getGenericComponentType(), typeVars)])
    elif jType.isArray():
        return TypeStr('_py_List', [pythonType(jType.getComponentType(), typeVars)])
    else:
        return translateTypeName(str(jType.getName()))


def pythonTypeVar(jType: Any, uniqScopeId: str) -> TypeVarStr:
    from java.lang.reflect import TypeVariable, ParameterizedType  # noqa
    if not isinstance(jType, TypeVariable):
        raise RuntimeError("Can not convert to type var %s (%s)" % (str(jType), repr(jType)))
    jBound = jType.getBounds()[0]
    if isinstance(jBound, ParameterizedType):
        jBound = jBound.getRawType()
    bound = pythonType(jBound)
    if bound.name == '_py_Any':
        bound = None  # unbounded
    javaName = jType.getName()
    return TypeVarStr(javaName=javaName, pythonName='_%s__%s' % (uniqScopeId, javaName), bound=bound)


def inferArgName(jType: Any, prevArgs: List[ArgSig]) -> str:
    if jType is None:
        return 'arg%d' % len(prevArgs)

    typename = str(jType.getTypeName())
    isArray = typename.endswith('[]')
    typename = typename.split('<')[0].split('$')[-1].split('.')[-1].replace('[]', '')
    typename = typename[:1].lower() + typename[1:]
    if isArray:
        typename += 'Array'
    prevArgsOfType = sum([bool(re.match(typename + '\\d*', prev.name)) for prev in prevArgs])
    if prevArgsOfType == 0:
        return typename
    else:
        return typename + str(prevArgsOfType + 1)


def isStatic(member: Any) -> bool:
    from java.lang.reflect import Modifier  # noqa
    return member.getModifiers() & Modifier.STATIC > 0


def isPublic(member: Any) -> bool:
    from java.lang.reflect import Modifier  # noqa
    return member.getModifiers() & Modifier.PUBLIC > 0


def generateJavaMethodStub(parentName: str,
                           name: str,
                           jOverloads: List[Any],
                           typesDone: Set[str],
                           classTypeVars: List[TypeVarStr],
                           output: List[str],
                           importsOutput: List[str]) -> None:
    isConstructor = name == '__init__'
    isOverloaded = len(jOverloads) > 1
    signatures = []  # type: List[JavaFunctionSig]
    for i, jOverload in enumerate(sorted(list(jOverloads), key=str)):
        jReturnType = None if isConstructor else jOverload.getGenericReturnType()
        jArgs = jOverload.getParameters()
        static = False if isConstructor else isStatic(jOverload)
        methodTypeVars = [pythonTypeVar(jType, uniqScopeId='%s_%d' % (name, i) if isOverloaded else name)
                          for jType in jOverload.getTypeParameters()]
        usableTypeVars = methodTypeVars + classTypeVars if not static else methodTypeVars
        args = [ArgSig(name='cls' if static else 'self', type=None)]
        for jArg in jArgs:
            jArgType = jArg.getParameterizedType()
            jArgName = str(jArg.getName()) if jArg.isNamePresent() else inferArgName(jArgType, args)
            args.append(ArgSig(name=jArgName, type=pythonType(jArgType, usableTypeVars)))

        signatures.append(JavaFunctionSig(name, args=args, retType=pythonType(jReturnType, usableTypeVars),
                                          static=static, typeVars=methodTypeVars))

    if isOverloaded:
        importsOutput.append('from typing import overload')
    for signature in signatures:
        for typeVar in signature.typeVars:
            output.append(toTypeVarDeclaration(typeVar, parentName, typesDone, importsOutput))
        if signature.static:
            output.append('@classmethod')
        sig = []
        for arg in signature.args:
            if arg.name in ('self', 'cls'):
                argDef = arg.name
            else:
                argDef = pysafe(arg.name)

                if arg.type:
                    argDef += ": " + toAnnotatedType(arg.type, parentName, typesDone, importsOutput)

            sig.append(argDef)

        if isOverloaded:
            output.append('@overload')
        if isConstructor:
            output.append('def __init__({args}): ...'.format(args=", ".join(sig)))
        else:
            output.append('def {function}({args}) -> {ret}: ...'.format(
                function=pysafe(signature.name),
                args=", ".join(sig),
                ret=toAnnotatedType(signature.retType, parentName, typesDone, importsOutput)
            ))


def generateJavaFieldStub(parentName: str,
                          jField: Any,
                          typesDone: Set[str],
                          classTypeVars: List[TypeVarStr],
                          output: List[str],
                          importsOutput: List[str]) -> None:
    if not isPublic(jField):
        return
    static = isStatic(jField)
    fieldName = jField.getName()
    fieldType = pythonType(jField.getType(), classTypeVars if not static else None)
    fieldTypeAnnotation = toAnnotatedType(fieldType, parentName, typesDone, importsOutput,
                                          canBeDeferred=True)
    if static:
        fieldTypeAnnotation = '_py_ClassVar[%s]' % fieldTypeAnnotation
    output.append('%s: %s = ...' % (pysafe(fieldName), fieldTypeAnnotation))


def toAnnotatedType(typeName: TypeStr, parentName: str, typesDone: Set[str], imports: List[str],
                    canBeDeferred: bool = True, forceShort: bool = False) -> str:
    aType = typeName.name
    isJavaType = '.' in aType
    if aType.startswith(parentName + '$'):
        aType = aType[len(parentName) + 1:]
    if '.' in aType:
        module = aType[:aType.rindex('.')]
        if module == 'builtins':
            aType = aType[len(module) + 1:]
        elif module == parentName:
            shortType = aType[len(module) + 1:]
            if shortType in typesDone or forceShort:
                aType = shortType
            elif canBeDeferred:
                aType = '\'%s\'' % shortType

        else:
            imports.append('import %s' % (module,))
    aType = aType.replace('$', '.')
    if isJavaType:
        aType = ".".join([pysafe(p) for p in aType.split(".")])
    if typeName.typeArgs:
        return aType + "[" + ", ".join(
            [toAnnotatedType(t, parentName, typesDone, imports) for t in typeName.typeArgs]) + "]"
    else:
        return aType


def toTypeVarDeclaration(typeVar: TypeVarStr, parentName: str, typesDone: Set[str], imports: List[str]) -> str:
    if typeVar.bound is not None:
        return '{pyname} = _py_TypeVar(\'{pyname}\', bound={bound})  # <{jname}>'.format(
            pyname=typeVar.pythonName,
            bound=toAnnotatedType(typeVar.bound, parentName, typesDone, imports),
            jname=typeVar.javaName
        )
    else:
        return '{pyname} = _py_TypeVar(\'{pyname}\')  # <{jname}>'.format(
            pyname=typeVar.pythonName,
            jname=typeVar.javaName
        )


def extraSuperTypes(className: str, classTypeVars: List[TypeVarStr]) -> List[str]:
    if className == 'java.util.Map':
        return ['_py_Mapping[%s, %s]' % (classTypeVars[0].pythonName, classTypeVars[1].pythonName)]
    elif className == 'java.util.Collection':
        return ['_py_Collection[%s]' % classTypeVars[0].pythonName]
    elif className == 'java.util.Set':
        return ['_py_Set[%s]' % classTypeVars[0].pythonName]
    elif className == 'java.util.List':
        return ['_py_List[%s]' % classTypeVars[0].pythonName]
    return []


def generateJavaClassStub(packageName: str,
                          jClass: jpype.JClass,
                          classesDone: Set[str],
                          output: List[str],
                          importsOutput: List[str],
                          typeVarOutput: List[str] = None,
                          parentClass: jpype.JClass = None,
                          parentClassTypeVars: List[TypeVarStr] = None) -> None:
    objDict = getattr(jClass, '__dict__')  # type: Mapping[str, Any]  # noqa
    items = sorted(objDict.items(), key=lambda x: x[0])

    writeTypeVarsToOutput = False
    if typeVarOutput is None:
        writeTypeVarsToOutput = True
        typeVarOutput = []  # type: List[str]

    classPrefix = str(jClass.class_.getName()).replace(packageName + '.', '').replace('.', '_').replace('$', '__')
    classTypeVars = [pythonTypeVar(t, uniqScopeId=classPrefix) for t in jClass.class_.getTypeParameters()]
    if parentClassTypeVars is None or isStatic(jClass.class_):
        usableTypeVars = classTypeVars
    else:
        usableTypeVars = parentClassTypeVars + classTypeVars
    jClass.class_.getTypeParameters()
    nestedClassesOutput = []  # type: List[str]
    for attr, value in items:
        if isJavaClass(value):
            generateJavaClassStub(packageName, value, classesDone, output=nestedClassesOutput,
                                  typeVarOutput=typeVarOutput, importsOutput=importsOutput,
                                  parentClass=jClass, parentClassTypeVars=usableTypeVars)

    constructorsOutput = []  # type: List[str]
    constructors = jClass.class_.getConstructors()
    generateJavaMethodStub(packageName, '__init__', constructors, typesDone=classesDone,
                           classTypeVars=usableTypeVars,
                           output=constructorsOutput, importsOutput=importsOutput)

    methodsOutput = []  # type: List[str]
    jOverloads = jClass.class_.getMethods()
    for attr, value in items:
        if isinstance(value, jpype.JMethod):
            matchingOverloads = [o for o in jOverloads if o.getName() == attr]
            generateJavaMethodStub(packageName, attr, matchingOverloads, typesDone=classesDone,
                                   classTypeVars=usableTypeVars,
                                   output=methodsOutput, importsOutput=importsOutput)

    fieldsOutput = []  # type: List[str]
    jFields = jClass.class_.getDeclaredFields()
    for jField in jFields:
        generateJavaFieldStub(packageName, jField, typesDone=classesDone,
                              classTypeVars=usableTypeVars, output=fieldsOutput, importsOutput=importsOutput)

    superTypes = []
    for superType in javaSuperTypes(jClass.class_):
        superTypes.append(toAnnotatedType(
            pythonType(superType, usableTypeVars),
            packageName,
            classesDone,
            importsOutput,
            canBeDeferred=False
        ))
    if classTypeVars:
        superTypes.append('_py_Generic[%s]' % ', '.join([tv.pythonName for tv in classTypeVars]))
    superTypes = superTypes + extraSuperTypes(jClass.class_.getName(), classTypeVars)
    for type_var in classTypeVars:
        typeVarOutput.append(toTypeVarDeclaration(type_var, packageName, classesDone, importsOutput))

    superTypeStr = '(%s)' % ', '.join(superTypes) if superTypes else ''

    className = toAnnotatedType(
        TypeStr(str(jClass.class_.getSimpleName())),  # do not use python_typename to avoid mangling classes
        str(parentClass.class_.getName()) if parentClass else packageName,
        classesDone,
        importsOutput,
        forceShort=True
    )

    if writeTypeVarsToOutput:
        output.append('')
        output += typeVarOutput

    if not constructorsOutput and not methodsOutput and not fieldsOutput and not nestedClassesOutput:
        output.append('class %s%s: ...' % (className, superTypeStr))
    else:
        output.append('class %s%s:' % (className, superTypeStr))
        for line in fieldsOutput:
            output.append('    %s' % line)
        for line in constructorsOutput:
            output.append('    %s' % line)
        for line in methodsOutput:
            output.append('    %s' % line)
        for line in nestedClassesOutput:
            output.append('    %s' % line)
    classesDone.add(className)


if __name__ == '__main__':
    import argparse
    from glob import glob

    parser = argparse.ArgumentParser(description='Generate Python Type Stubs for Java classes.')
    parser.add_argument('prefixes', type=str, nargs='+',
                        help='package prefixes to generate stubs for (e.g. org.myproject)')
    parser.add_argument('--jvmpath', type=str,
                        help='path to the JVM ("libjvm.so", "jvm.dll", ...) (default: use system default JVM)')
    parser.add_argument('--classpath', type=str,
                        help='java class path to use, separated by ":". '
                             'glob-like expressions (e.g. dir/*.jar) are supported (default: .)')
    parser.add_argument('--output-dir', type=str,
                        help='path to write stubs to (default: .)')
    parser.add_argument('--convert-strings', dest='convert_strings', action='store_true')
    parser.add_argument('--no-convert-strings', dest='convert_strings', action='store_false',
                        help='whether to convert java.lang.String to python str in return types. '
                             'consult the JPype documentation on the convertStrings flag for details (default: False)')
    parser.add_argument('--stubs-suffix', dest='stubs_suffix', action='store_true')
    parser.add_argument('--no-stubs-suffix', dest='stubs_suffix', action='store_false',
                        help='whether to use PEP-561 "-stubs" suffix for top-level packages (default: True)')

    parser.set_defaults(stubs_suffix=True, classpath='.', output_dir='.', convert_strings=False)

    args = parser.parse_args()
    classpath = [c for c_in in args.classpath.split(':') for c in glob(c_in)]
    print("Starting JPype JVM with classpath " + str(classpath))
    jpype.startJVM(jvmpath=args.jvmpath, classpath=classpath, convertStrings=args.convert_strings)

    generateJavaStubs(args.prefixes, useStubsSuffix=args.stubs_suffix, outputDir=args.output_dir)
    print("Generation done.")
