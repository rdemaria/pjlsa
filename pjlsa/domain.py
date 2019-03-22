from . import _jpype as _jp
from .util import enum_super as _enum_super

# Contexts
Context = _jp.cern.lsa.domain.settings.Context
StandAloneBeamProcess = _jp.cern.lsa.domain.settings.StandAloneBeamProcess
StandAloneContext = _jp.cern.lsa.domain.settings.StandAloneContext
StandAloneCycle = _jp.cern.lsa.domain.settings.StandAloneCycle
BeamProcess = _jp.cern.lsa.domain.settings.BeamProcess
BeamProcessType = _jp.cern.lsa.domain.settings.type.BeamProcessType
BeamProcessPurpose = _jp.cern.lsa.domain.settings.type.BeamProcessPurpose
ActualBeamProcessInfo = _jp.cern.lsa.domain.settings.ActualBeamProcessInfo
UserContextMapping = _jp.cern.lsa.domain.settings.UserContextMapping
AcceleratorUser = _jp.cern.lsa.domain.settings.AcceleratorUser
AcceleratorUserGroup = _jp.cern.lsa.domain.settings.AcceleratorUserGroup

# Parameters
Parameter = _jp.cern.lsa.domain.settings.Parameter
ParameterAttributes = _jp.cern.lsa.domain.settings.ParameterAttributes
ParameterForEditing = _jp.cern.lsa.domain.settings.ParameterForEditing
ParameterGroup = _jp.cern.lsa.domain.settings.ParameterGroup
ParameterTreeNode = _jp.cern.lsa.domain.settings.ParameterTreeNode
ParameterType = _jp.cern.lsa.domain.settings.ParameterType
ParameterTypeGroup = _jp.cern.lsa.domain.settings.ParameterTypeGroup

# Make Rules
MakeRuleForParameterRelation = _jp.cern.lsa.domain.settings.parameter.relation.MakeRuleForParameterRelation
MakeRuleClassInfo = _jp.cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo
MakeRuleInfo = _jp.cern.lsa.domain.trim.rules.makerule.MakeRuleInfo

# ============== Enums ==============
# cern.lsa.domain.settings
ContextFamily = _jp._pyEnum(_jp.cern.lsa.domain.settings.ContextFamily)
SettingComparisonResultType = _jp._pyEnum(_jp.cern.lsa.domain.settings.SettingComparisonResultType)
LinkRuleAttribute = _jp._pyEnum(_jp.cern.lsa.domain.settings.LinkRuleAttribute)
ParameterTypeCategory = _jp._pyEnum(_jp.cern.lsa.domain.settings.ParameterTypeCategory)
PropertyAccessMode = _jp._pyEnum(_jp.cern.lsa.domain.settings.PropertyAccessMode)
SettingPartEnum = _jp._pyEnum(_jp.cern.lsa.domain.settings.SettingPartEnum)
BeamProcessTypeCategory = _jp._pyEnum(_jp.cern.lsa.domain.settings.type.BeamProcessTypeCategory)
CernContextCategory = _jp._pyEnum(_jp.cern.lsa.domain.cern.settings.CernContextCategory)
MakeRuleConfigStatus = _jp._pyEnum('cern.lsa.domain.settings.parameter.relation.MakeRuleForParameterRelation$MakeRuleConfigStatus')

# cern.lsa.domain.optics
CalibrationFunctionTypes = _jp._pyEnum(_jp.cern.lsa.domain.optics.CalibrationFunctionTypes)
ElementType = _jp._pyEnum(_jp.cern.lsa.domain.optics.ElementType)
BeamEnum = _jp._pyEnum(_jp.cern.lsa.domain.optics.BeamEnum)
ElementPlane = _jp._pyEnum(_jp.cern.lsa.domain.optics.ElementPlane)
OfbReadingSetType = _jp._pyEnum(_jp.cern.lsa.domain.cern.optics.ofb.OfbReadingSetType)

# cern.lsa.domain.devices
DeviceTypeImplementation = _jp._pyEnum(_jp.cern.lsa.domain.devices.DeviceTypeImplementation)
PropertyFieldAccess = _jp._pyEnum(_jp.cern.lsa.domain.devices.spi.PropertyFieldAccess)
DeviceMetaTypeEnum = _jp._pyEnum(_jp.cern.lsa.domain.devices.DeviceMetaTypeEnum)
DeviceGroupTypeEnum = _jp._pyEnum(_jp.cern.lsa.domain.cern.devices.DeviceGroupTypeEnum)
CollimatorRegion = _jp._pyEnum(_jp.cern.lsa.domain.cern.devices.CollimatorRegion)

# cern.lsa.domain.timing
TimingMasterStatus = _jp._pyEnum(_jp.cern.lsa.domain.cern.timing.enums.MASTER_STATUS)
TimingTableStatusSw = _jp._pyEnum(_jp.cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW)
TimingRngi = _jp._pyEnum(_jp.cern.lsa.domain.cern.timing.enums.RNGI)
TimingInjectionStatus = _jp._pyEnum(_jp.cern.lsa.domain.cern.timing.enums.INJECTION_STATUS)
TimingTableStatusHw = _jp._pyEnum(_jp.cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW)
TimingBeamType = _jp._pyEnum(_jp.cern.lsa.domain.cern.timing.enums.BEAM_TYPE)
TimingParticleType = _jp._pyEnum(_jp.cern.lsa.domain.cern.timing.enums.PARTICLE_TYPE)

# cern.accsoft.commons
CernAccelerator = _jp._pyEnum(_jp.cern.accsoft.commons.domain.CernAccelerator)
CernTimingDomain = _jp._pyEnum(_jp.cern.accsoft.commons.domain.CernTimingDomain)


ParticleTransfer = _enum_super('ParticleTransfer')
AdParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.AdParticleTransfer, ParticleTransfer)
CtfParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.CtfParticleTransfer, ParticleTransfer)
ElenaParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer, ParticleTransfer)
IsoldeParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.IsoldeParticleTransfer, ParticleTransfer)
LeirParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.LeirParticleTransfer, ParticleTransfer)
LhcParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.LhcParticleTransfer, ParticleTransfer)
Linac4ParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.Linac4ParticleTransfer, ParticleTransfer)
NorthParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer, ParticleTransfer)
ParticleTransferType = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.ParticleTransferType, ParticleTransfer)
PsParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.PsParticleTransfer, ParticleTransfer)
PsbParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.PsbParticleTransfer, ParticleTransfer)
SpsParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer, ParticleTransfer)

AcceleratorZone = _enum_super('AcceleratorZone')
AdAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.AdAcceleratorZone, AcceleratorZone)
CtfAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.CtfAcceleratorZone, AcceleratorZone)
ElenaAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.ElenaAcceleratorZone, AcceleratorZone)
IsoldeAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.IsoldeAcceleratorZone, AcceleratorZone)
LeirAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.LeirAcceleratorZone, AcceleratorZone)
LhcAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.LhcAcceleratorZone, AcceleratorZone)
Linac4AcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.Linac4AcceleratorZone, AcceleratorZone)
NorthAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.NorthAcceleratorZone, AcceleratorZone)
PsAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.PsAcceleratorZone, AcceleratorZone)
PsbAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.PsbAcceleratorZone, AcceleratorZone)
SpsAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.SpsAcceleratorZone, AcceleratorZone)

ElenaBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.ElenaBeam)
SpsBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.SpsBeam)
LeirBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.LeirBeam)
PsbBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.PsbBeam)
PsBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.PsBeam)
AdBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.AdBeam)
LhcBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.LhcBeam)
Linac4Beam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.Linac4Beam)

AcceleratorMode = _enum_super('AcceleratorMode')
PsbAcceleratorMode = _jp._pyEnum(_jp.cern.accsoft.commons.domain.modes.PsbAcceleratorMode, AcceleratorMode)
LhcAcceleratorMode = _jp._pyEnum(_jp.cern.accsoft.commons.domain.modes.LhcAcceleratorMode, AcceleratorMode)
SpsAcceleratorMode = _jp._pyEnum(_jp.cern.accsoft.commons.domain.modes.SpsAcceleratorMode, AcceleratorMode)
PsAcceleratorMode = _jp._pyEnum(_jp.cern.accsoft.commons.domain.modes.PsAcceleratorMode, AcceleratorMode)
LeirAcceleratorMode = _jp._pyEnum(_jp.cern.accsoft.commons.domain.modes.LeirAcceleratorMode, AcceleratorMode)

LhcBeamMode = _jp._pyEnum(_jp.cern.accsoft.commons.domain.modes.LhcBeamMode)
ParticleType = _jp._pyEnum(_jp.cern.accsoft.commons.domain.ParticleType)

SpsLhcB2EndPoint = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beamdestinations.SpsLhcB2EndPoint)
SpsLhcB1EndPoint = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beamdestinations.SpsLhcB1EndPoint)
SpsAwakeEndPoint = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beamdestinations.SpsAwakeEndPoint)
SpsHiradmatEndPoint = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beamdestinations.SpsHiradmatEndPoint)
SpsFTargetEndPoint = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beamdestinations.SpsFTargetEndPoint)
SpsBeamDestination = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination)

LhcInteractionPoint = _jp._pyEnum(_jp.cern.accsoft.commons.domain.lhc.LhcInteractionPoint)
LhcSector = _jp._pyEnum(_jp.cern.accsoft.commons.domain.lhc.LhcSector)
LhcExperiment = _jp._pyEnum(_jp.cern.accsoft.commons.domain.lhc.LhcExperiment)
