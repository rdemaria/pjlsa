from . import _jpype as _jp
from .util import super_enum as _super_enum

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
ContextFamily = _jp.pyEnum(_jp.cern.lsa.domain.settings.ContextFamily)
SettingComparisonResultType = _jp.pyEnum(_jp.cern.lsa.domain.settings.SettingComparisonResultType)
LinkRuleAttribute = _jp.pyEnum(_jp.cern.lsa.domain.settings.LinkRuleAttribute)
ParameterTypeCategory = _jp.pyEnum(_jp.cern.lsa.domain.settings.ParameterTypeCategory)
PropertyAccessMode = _jp.pyEnum(_jp.cern.lsa.domain.settings.PropertyAccessMode)
SettingPartEnum = _jp.pyEnum(_jp.cern.lsa.domain.settings.SettingPartEnum)
BeamProcessTypeCategory = _jp.pyEnum(_jp.cern.lsa.domain.settings.type.BeamProcessTypeCategory)
CernContextCategory = _jp.pyEnum(_jp.cern.lsa.domain.cern.settings.CernContextCategory)
MakeRuleConfigStatus = _jp.pyEnum('cern.lsa.domain.settings.parameter.relation.MakeRuleForParameterRelation$MakeRuleConfigStatus')

# cern.lsa.domain.optics
CalibrationFunctionTypes = _jp.pyEnum(_jp.cern.lsa.domain.optics.CalibrationFunctionTypes)
ElementType = _jp.pyEnum(_jp.cern.lsa.domain.optics.ElementType)
BeamEnum = _jp.pyEnum(_jp.cern.lsa.domain.optics.BeamEnum)
ElementPlane = _jp.pyEnum(_jp.cern.lsa.domain.optics.ElementPlane)
OfbReadingSetType = _jp.pyEnum(_jp.cern.lsa.domain.cern.optics.ofb.OfbReadingSetType)

# cern.lsa.domain.devices
DeviceTypeImplementation = _jp.pyEnum(_jp.cern.lsa.domain.devices.DeviceTypeImplementation)
PropertyFieldAccess = _jp.pyEnum(_jp.cern.lsa.domain.devices.spi.PropertyFieldAccess)
DeviceMetaTypeEnum = _jp.pyEnum(_jp.cern.lsa.domain.devices.DeviceMetaTypeEnum)
DeviceGroupTypeEnum = _jp.pyEnum(_jp.cern.lsa.domain.cern.devices.DeviceGroupTypeEnum)
CollimatorRegion = _jp.pyEnum(_jp.cern.lsa.domain.cern.devices.CollimatorRegion)

# cern.lsa.domain.timing
TimingMasterStatus = _jp.pyEnum(_jp.cern.lsa.domain.cern.timing.enums.MASTER_STATUS)
TimingTableStatusSw = _jp.pyEnum(_jp.cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW)
TimingRngi = _jp.pyEnum(_jp.cern.lsa.domain.cern.timing.enums.RNGI)
TimingInjectionStatus = _jp.pyEnum(_jp.cern.lsa.domain.cern.timing.enums.INJECTION_STATUS)
TimingTableStatusHw = _jp.pyEnum(_jp.cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW)
TimingBeamType = _jp.pyEnum(_jp.cern.lsa.domain.cern.timing.enums.BEAM_TYPE)
TimingParticleType = _jp.pyEnum(_jp.cern.lsa.domain.cern.timing.enums.PARTICLE_TYPE)

# cern.accsoft.commons
CernAccelerator = _jp.pyEnum(_jp.cern.accsoft.commons.domain.CernAccelerator)
CernTimingDomain = _jp.pyEnum(_jp.cern.accsoft.commons.domain.CernTimingDomain)


ParticleTransfer = _super_enum('ParticleTransfer')
AdParticleTransfer = _jp.pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.AdParticleTransfer, ParticleTransfer)
CtfParticleTransfer = _jp.pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.CtfParticleTransfer, ParticleTransfer)
ElenaParticleTransfer = _jp.pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer, ParticleTransfer)
IsoldeParticleTransfer = _jp.pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.IsoldeParticleTransfer, ParticleTransfer)
LeirParticleTransfer = _jp.pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.LeirParticleTransfer, ParticleTransfer)
LhcParticleTransfer = _jp.pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.LhcParticleTransfer, ParticleTransfer)
Linac4ParticleTransfer = _jp.pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.Linac4ParticleTransfer, ParticleTransfer)
NorthParticleTransfer = _jp.pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer, ParticleTransfer)
ParticleTransferType = _jp.pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.ParticleTransferType, ParticleTransfer)
PsParticleTransfer = _jp.pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.PsParticleTransfer, ParticleTransfer)
PsbParticleTransfer = _jp.pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.PsbParticleTransfer, ParticleTransfer)
SpsParticleTransfer = _jp.pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer, ParticleTransfer)

AcceleratorZone = _super_enum('AcceleratorZone')
AdAcceleratorZone = _jp.pyEnum(_jp.cern.accsoft.commons.domain.zones.AdAcceleratorZone, AcceleratorZone)
CtfAcceleratorZone = _jp.pyEnum(_jp.cern.accsoft.commons.domain.zones.CtfAcceleratorZone, AcceleratorZone)
ElenaAcceleratorZone = _jp.pyEnum(_jp.cern.accsoft.commons.domain.zones.ElenaAcceleratorZone, AcceleratorZone)
IsoldeAcceleratorZone = _jp.pyEnum(_jp.cern.accsoft.commons.domain.zones.IsoldeAcceleratorZone, AcceleratorZone)
LeirAcceleratorZone = _jp.pyEnum(_jp.cern.accsoft.commons.domain.zones.LeirAcceleratorZone, AcceleratorZone)
LhcAcceleratorZone = _jp.pyEnum(_jp.cern.accsoft.commons.domain.zones.LhcAcceleratorZone, AcceleratorZone)
Linac4AcceleratorZone = _jp.pyEnum(_jp.cern.accsoft.commons.domain.zones.Linac4AcceleratorZone, AcceleratorZone)
NorthAcceleratorZone = _jp.pyEnum(_jp.cern.accsoft.commons.domain.zones.NorthAcceleratorZone, AcceleratorZone)
PsAcceleratorZone = _jp.pyEnum(_jp.cern.accsoft.commons.domain.zones.PsAcceleratorZone, AcceleratorZone)
PsbAcceleratorZone = _jp.pyEnum(_jp.cern.accsoft.commons.domain.zones.PsbAcceleratorZone, AcceleratorZone)
SpsAcceleratorZone = _jp.pyEnum(_jp.cern.accsoft.commons.domain.zones.SpsAcceleratorZone, AcceleratorZone)

ElenaBeam = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beams.ElenaBeam)
SpsBeam = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beams.SpsBeam)
LeirBeam = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beams.LeirBeam)
PsbBeam = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beams.PsbBeam)
PsBeam = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beams.PsBeam)
AdBeam = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beams.AdBeam)
LhcBeam = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beams.LhcBeam)
Linac4Beam = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beams.Linac4Beam)

AcceleratorMode = _super_enum('AcceleratorMode')
PsbAcceleratorMode = _jp.pyEnum(_jp.cern.accsoft.commons.domain.modes.PsbAcceleratorMode, AcceleratorMode)
LhcAcceleratorMode = _jp.pyEnum(_jp.cern.accsoft.commons.domain.modes.LhcAcceleratorMode, AcceleratorMode)
SpsAcceleratorMode = _jp.pyEnum(_jp.cern.accsoft.commons.domain.modes.SpsAcceleratorMode, AcceleratorMode)
PsAcceleratorMode = _jp.pyEnum(_jp.cern.accsoft.commons.domain.modes.PsAcceleratorMode, AcceleratorMode)
LeirAcceleratorMode = _jp.pyEnum(_jp.cern.accsoft.commons.domain.modes.LeirAcceleratorMode, AcceleratorMode)

LhcBeamMode = _jp.pyEnum(_jp.cern.accsoft.commons.domain.modes.LhcBeamMode)
ParticleType = _jp.pyEnum(_jp.cern.accsoft.commons.domain.ParticleType)

SpsLhcB2EndPoint = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beamdestinations.SpsLhcB2EndPoint)
SpsLhcB1EndPoint = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beamdestinations.SpsLhcB1EndPoint)
SpsAwakeEndPoint = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beamdestinations.SpsAwakeEndPoint)
SpsHiradmatEndPoint = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beamdestinations.SpsHiradmatEndPoint)
SpsFTargetEndPoint = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beamdestinations.SpsFTargetEndPoint)
SpsBeamDestination = _jp.pyEnum(_jp.cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination)

LhcInteractionPoint = _jp.pyEnum(_jp.cern.accsoft.commons.domain.lhc.LhcInteractionPoint)
LhcSector = _jp.pyEnum(_jp.cern.accsoft.commons.domain.lhc.LhcSector)
LhcExperiment = _jp.pyEnum(_jp.cern.accsoft.commons.domain.lhc.LhcExperiment)
