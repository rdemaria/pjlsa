import cern.accsoft.commons.domain
import java.util.function
import typing



class CernAccelerators:
    """
    Java class 'cern.lsa.domain.cern.commons.CernAccelerators'
    
        Extends:
            java.lang.Object
    
    """
    class AD(java.util.function.Supplier[cern.accsoft.commons.domain.Accelerator]):
        """
        Java class 'cern.lsa.domain.cern.commons.CernAccelerators$AD'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.function.Supplier
        
          Constructors:
            * AD()
        
        """
        def __init__(self): ...
        def get(self) -> cern.accsoft.commons.domain.Accelerator: ...
    class AWAKE(java.util.function.Supplier[cern.accsoft.commons.domain.Accelerator]):
        """
        Java class 'cern.lsa.domain.cern.commons.CernAccelerators$AWAKE'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.function.Supplier
        
          Constructors:
            * AWAKE()
        
        """
        def __init__(self): ...
        def get(self) -> cern.accsoft.commons.domain.Accelerator: ...
    class CTF(java.util.function.Supplier[cern.accsoft.commons.domain.Accelerator]):
        """
        Java class 'cern.lsa.domain.cern.commons.CernAccelerators$CTF'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.function.Supplier
        
          Constructors:
            * CTF()
        
        """
        def __init__(self): ...
        def get(self) -> cern.accsoft.commons.domain.Accelerator: ...
    class ELENA(java.util.function.Supplier[cern.accsoft.commons.domain.Accelerator]):
        """
        Java class 'cern.lsa.domain.cern.commons.CernAccelerators$ELENA'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.function.Supplier
        
          Constructors:
            * ELENA()
        
        """
        def __init__(self): ...
        def get(self) -> cern.accsoft.commons.domain.Accelerator: ...
    class ISOLDE(java.util.function.Supplier[cern.accsoft.commons.domain.Accelerator]):
        """
        Java class 'cern.lsa.domain.cern.commons.CernAccelerators$ISOLDE'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.function.Supplier
        
          Constructors:
            * ISOLDE()
        
        """
        def __init__(self): ...
        def get(self) -> cern.accsoft.commons.domain.Accelerator: ...
    class LEIR(java.util.function.Supplier[cern.accsoft.commons.domain.Accelerator]):
        """
        Java class 'cern.lsa.domain.cern.commons.CernAccelerators$LEIR'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.function.Supplier
        
          Constructors:
            * LEIR()
        
        """
        def __init__(self): ...
        def get(self) -> cern.accsoft.commons.domain.Accelerator: ...
    class LHC(java.util.function.Supplier[cern.accsoft.commons.domain.Accelerator]):
        """
        Java class 'cern.lsa.domain.cern.commons.CernAccelerators$LHC'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.function.Supplier
        
          Constructors:
            * LHC()
        
        """
        def __init__(self): ...
        def get(self) -> cern.accsoft.commons.domain.Accelerator: ...
    class LINAC4(java.util.function.Supplier[cern.accsoft.commons.domain.Accelerator]):
        """
        Java class 'cern.lsa.domain.cern.commons.CernAccelerators$LINAC4'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.function.Supplier
        
          Constructors:
            * LINAC4()
        
        """
        def __init__(self): ...
        def get(self) -> cern.accsoft.commons.domain.Accelerator: ...
    class NORTH(java.util.function.Supplier[cern.accsoft.commons.domain.Accelerator]):
        """
        Java class 'cern.lsa.domain.cern.commons.CernAccelerators$NORTH'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.function.Supplier
        
          Constructors:
            * NORTH()
        
        """
        def __init__(self): ...
        def get(self) -> cern.accsoft.commons.domain.Accelerator: ...
    class PS(java.util.function.Supplier[cern.accsoft.commons.domain.Accelerator]):
        """
        Java class 'cern.lsa.domain.cern.commons.CernAccelerators$PS'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.function.Supplier
        
          Constructors:
            * PS()
        
        """
        def __init__(self): ...
        def get(self) -> cern.accsoft.commons.domain.Accelerator: ...
    class PSB(java.util.function.Supplier[cern.accsoft.commons.domain.Accelerator]):
        """
        Java class 'cern.lsa.domain.cern.commons.CernAccelerators$PSB'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.function.Supplier
        
          Constructors:
            * PSB()
        
        """
        def __init__(self): ...
        def get(self) -> cern.accsoft.commons.domain.Accelerator: ...
    class SPS(java.util.function.Supplier[cern.accsoft.commons.domain.Accelerator]):
        """
        Java class 'cern.lsa.domain.cern.commons.CernAccelerators$SPS'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.util.function.Supplier
        
          Constructors:
            * SPS()
        
        """
        def __init__(self): ...
        def get(self) -> cern.accsoft.commons.domain.Accelerator: ...

class LsaCernConstants:
    """
    Java class 'cern.lsa.domain.cern.commons.LsaCernConstants'
    
        Extends:
            java.lang.Object
    
    """
    class DriveConstants:
        """
        Java class 'cern.lsa.domain.cern.commons.LsaCernConstants$DriveConstants'
        
            Extends:
                java.lang.Object
        
          Attributes:
            ATTR_FUNCTIONS_TO_REACH_NEW_VALUES (java.lang.String): final static field
            ATTR_TIME_TO_REACH_NEW_VALUES (java.lang.String): final static field
            ATTR_TRANSACTION_ID (java.lang.String): final static field
        
        """
        ATTR_FUNCTIONS_TO_REACH_NEW_VALUES: typing.ClassVar[str] = ...
        ATTR_TIME_TO_REACH_NEW_VALUES: typing.ClassVar[str] = ...
        ATTR_TRANSACTION_ID: typing.ClassVar[str] = ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.commons")``.

    CernAccelerators: typing.Type[CernAccelerators]
    LsaCernConstants: typing.Type[LsaCernConstants]
