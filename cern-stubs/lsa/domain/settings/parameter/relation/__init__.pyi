from typing import Any as _py_Any
import cern.accsoft.commons.domain.particletransfers
import cern.lsa.domain.settings
import java.io


class ParameterRelation:
    @classmethod
    def builder(cls) -> 'DefaultParameterRelation.Builder': ...
    def getDependentParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def getHierarchy(self) -> str: ...
    def getSourceParameter(self) -> cern.lsa.domain.settings.Parameter: ...

class ParameterRelationInfo:
    @classmethod
    def builder(cls) -> 'DefaultParameterRelationInfo.Builder': ...
    def getParameterRelation(self) -> ParameterRelation: ...
    def getParameterSpecificMakeRuleName(self) -> str: ...

class ParameterRelationInfosRequest:
    @classmethod
    def builder(cls) -> 'DefaultParameterRelationInfosRequest.Builder': ...
    @classmethod
    def byParticleTransfer(cls, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'ParameterRelationInfosRequest': ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...

class DefaultParameterRelation(ParameterRelation, java.io.Serializable):
    @classmethod
    def builder(cls) -> 'DefaultParameterRelation.Builder': ...
    @classmethod
    def copyOf(cls, parameterRelation: ParameterRelation) -> 'DefaultParameterRelation': ...
    def equals(self, object: _py_Any) -> bool: ...
    def getDependentParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def getHierarchy(self) -> str: ...
    def getSourceParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def withDependentParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultParameterRelation': ...
    def withHierarchy(self, string: str) -> 'DefaultParameterRelation': ...
    def withSourceParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultParameterRelation': ...
    class Builder:
        def build(self) -> 'DefaultParameterRelation': ...
        def dependentParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultParameterRelation.Builder': ...
        def hierarchy(self, string: str) -> 'DefaultParameterRelation.Builder': ...
        def sourceParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultParameterRelation.Builder': ...

class DefaultParameterRelationInfo(ParameterRelationInfo, java.io.Serializable):
    @classmethod
    def builder(cls) -> 'DefaultParameterRelationInfo.Builder': ...
    @classmethod
    def copyOf(cls, parameterRelationInfo: ParameterRelationInfo) -> 'DefaultParameterRelationInfo': ...
    def equals(self, object: _py_Any) -> bool: ...
    def getParameterRelation(self) -> ParameterRelation: ...
    def getParameterSpecificMakeRuleName(self) -> str: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def withParameterRelation(self, parameterRelation: ParameterRelation) -> 'DefaultParameterRelationInfo': ...
    def withParameterSpecificMakeRuleName(self, string: str) -> 'DefaultParameterRelationInfo': ...
    class Builder:
        def build(self) -> 'DefaultParameterRelationInfo': ...
        def parameterRelation(self, parameterRelation: ParameterRelation) -> 'DefaultParameterRelationInfo.Builder': ...
        def parameterSpecificMakeRuleName(self, string: str) -> 'DefaultParameterRelationInfo.Builder': ...

class DefaultParameterRelationInfosRequest(ParameterRelationInfosRequest, java.io.Serializable):
    @classmethod
    def builder(cls) -> 'DefaultParameterRelationInfosRequest.Builder': ...
    @classmethod
    def copyOf(cls, parameterRelationInfosRequest: ParameterRelationInfosRequest) -> 'DefaultParameterRelationInfosRequest': ...
    def equals(self, object: _py_Any) -> bool: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def withParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultParameterRelationInfosRequest': ...
    class Builder:
        def build(self) -> 'DefaultParameterRelationInfosRequest': ...
        def particleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultParameterRelationInfosRequest.Builder': ...