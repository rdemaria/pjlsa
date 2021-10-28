import cern.accsoft.commons.domain.particletransfers
import cern.lsa.domain.settings
import java.io
import typing



class ParameterRelation:
    """
    Java class 'cern.lsa.domain.settings.parameter.relation.ParameterRelation'
    
    """
    @staticmethod
    def builder() -> 'DefaultParameterRelation.Builder': ...
    def getDependentParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def getHierarchy(self) -> str: ...
    def getSourceParameter(self) -> cern.lsa.domain.settings.Parameter: ...

class ParameterRelationInfo:
    """
    Java class 'cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo'
    
    """
    @staticmethod
    def builder() -> 'DefaultParameterRelationInfo.Builder': ...
    def getParameterRelation(self) -> ParameterRelation: ...
    def getParameterSpecificMakeRuleName(self) -> str: ...

class ParameterRelationInfosRequest:
    """
    Java class 'cern.lsa.domain.settings.parameter.relation.ParameterRelationInfosRequest'
    
    """
    @staticmethod
    def builder() -> 'DefaultParameterRelationInfosRequest.Builder': ...
    @staticmethod
    def byParticleTransfer(particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'ParameterRelationInfosRequest': ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...

class DefaultParameterRelation(ParameterRelation, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.settings.parameter.relation.DefaultParameterRelation'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.settings.parameter.relation.ParameterRelation,
            java.io.Serializable
    
    """
    @staticmethod
    def builder() -> 'DefaultParameterRelation.Builder': ...
    @staticmethod
    def copyOf(parameterRelation: ParameterRelation) -> 'DefaultParameterRelation': ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDependentParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def getHierarchy(self) -> str: ...
    def getSourceParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def withDependentParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultParameterRelation': ...
    def withHierarchy(self, string: str) -> 'DefaultParameterRelation': ...
    def withSourceParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultParameterRelation': ...
    class Builder:
        """
        Java class 'cern.lsa.domain.settings.parameter.relation.DefaultParameterRelation$Builder'
        
            Extends:
                java.lang.Object
        
        """
        def build(self) -> 'DefaultParameterRelation': ...
        def dependentParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultParameterRelation.Builder': ...
        def hierarchy(self, string: str) -> 'DefaultParameterRelation.Builder': ...
        def sourceParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultParameterRelation.Builder': ...

class DefaultParameterRelationInfo(ParameterRelationInfo, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.settings.parameter.relation.DefaultParameterRelationInfo'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.settings.parameter.relation.ParameterRelationI
            nfo, java.io.Serializable
    
    """
    @staticmethod
    def builder() -> 'DefaultParameterRelationInfo.Builder': ...
    @staticmethod
    def copyOf(parameterRelationInfo: ParameterRelationInfo) -> 'DefaultParameterRelationInfo': ...
    def equals(self, object: typing.Any) -> bool: ...
    def getParameterRelation(self) -> ParameterRelation: ...
    def getParameterSpecificMakeRuleName(self) -> str: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def withParameterRelation(self, parameterRelation: ParameterRelation) -> 'DefaultParameterRelationInfo': ...
    def withParameterSpecificMakeRuleName(self, string: str) -> 'DefaultParameterRelationInfo': ...
    class Builder:
        """
        Java class 'cern.lsa.domain.settings.parameter.relation.DefaultParameterRelationInfo$Builder'
        
            Extends:
                java.lang.Object
        
        """
        def build(self) -> 'DefaultParameterRelationInfo': ...
        def parameterRelation(self, parameterRelation: ParameterRelation) -> 'DefaultParameterRelationInfo.Builder': ...
        def parameterSpecificMakeRuleName(self, string: str) -> 'DefaultParameterRelationInfo.Builder': ...

class DefaultParameterRelationInfosRequest(ParameterRelationInfosRequest, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.settings.parameter.relation.DefaultParameterRelationInfosRequest'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.settings.parameter.relation.ParameterRelationI
            nfosRequest, java.io.Serializable
    
    """
    @staticmethod
    def builder() -> 'DefaultParameterRelationInfosRequest.Builder': ...
    @staticmethod
    def copyOf(parameterRelationInfosRequest: ParameterRelationInfosRequest) -> 'DefaultParameterRelationInfosRequest': ...
    def equals(self, object: typing.Any) -> bool: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def withParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultParameterRelationInfosRequest': ...
    class Builder:
        """
        Java class 'cern.lsa.domain.settings.parameter.relation.DefaultParameterRelationInfosRequest$Builder'
        
            Extends:
                java.lang.Object
        
        """
        def build(self) -> 'DefaultParameterRelationInfosRequest': ...
        def particleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultParameterRelationInfosRequest.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.settings.parameter.relation")``.

    DefaultParameterRelation: typing.Type[DefaultParameterRelation]
    DefaultParameterRelationInfo: typing.Type[DefaultParameterRelationInfo]
    DefaultParameterRelationInfosRequest: typing.Type[DefaultParameterRelationInfosRequest]
    ParameterRelation: typing.Type[ParameterRelation]
    ParameterRelationInfo: typing.Type[ParameterRelationInfo]
    ParameterRelationInfosRequest: typing.Type[ParameterRelationInfosRequest]
