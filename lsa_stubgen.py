import pjlsa
import stubgenj

lsa = pjlsa.LSAClient()
prefixes = ["java",
            "com.google.common.collect",
            "com.google.common.base",
            "cern.lsa",
            "cern.accsoft.commons",
            "cern.rbac.common",
            "cern.japc.core", "cern.japc.value"]
#prefixes = ["cern.accsoft.commons.remoting"]
stubgenj.generateJavaStubs(prefixes, useStubsSuffix=True, outputDir='.')
