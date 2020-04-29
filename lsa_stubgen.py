import pjlsa
import stubgenj

lsa = pjlsa.LSAClient()

prefixes = ["java",
            "cern.lsa",
            "cern.accsoft.commons",
            "cern.rbac.common",
            "cern.japc.core", "cern.japc.value"]

#prefixes = ["java.util"]
stubgenj.generate_java_stubs(prefixes, 'pyi')
