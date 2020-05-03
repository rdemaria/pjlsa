import pjlsa
import stubgenj

lsa = pjlsa.LSAClient()
prefixes = ["java",
            "com.google.common.collect",
            "cern.lsa",
            "cern.accsoft.commons",
            "cern.rbac.common",
            "cern.japc.core", "cern.japc.value"]
#prefixes = ["java.util"]
stubgenj.generate_java_stubs(prefixes, use_stubs_suffix=True, output_dir='.')
