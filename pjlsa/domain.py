from . import _jpype as _jp

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

AdParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.AdParticleTransfer)
CtfParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.CtfParticleTransfer)
ElenaParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer)
IsoldeParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.IsoldeParticleTransfer)
LeirParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.LeirParticleTransfer)
LhcParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.LhcParticleTransfer)
Linac4ParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.Linac4ParticleTransfer)
NorthParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer)
ParticleTransferType = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.ParticleTransferType)
PsParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.PsParticleTransfer)
PsbParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.PsbParticleTransfer)
SpsParticleTransfer = _jp._pyEnum(_jp.cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer)

AdAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.AdAcceleratorZone)
CtfAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.CtfAcceleratorZone)
ElenaAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.ElenaAcceleratorZone)
IsoldeAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.IsoldeAcceleratorZone)
LeirAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.LeirAcceleratorZone)
LhcAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.LhcAcceleratorZone)
Linac4AcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.Linac4AcceleratorZone)
NorthAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.NorthAcceleratorZone)
PsAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.PsAcceleratorZone)
PsbAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.PsbAcceleratorZone)
SpsAcceleratorZone = _jp._pyEnum(_jp.cern.accsoft.commons.domain.zones.SpsAcceleratorZone)

ElenaBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.ElenaBeam)
SpsBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.SpsBeam)
LeirBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.LeirBeam)
PsbBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.PsbBeam)
PsBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.PsBeam)
AdBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.AdBeam)
LhcBeam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.LhcBeam)
Linac4Beam = _jp._pyEnum(_jp.cern.accsoft.commons.domain.beams.Linac4Beam)

PsbAcceleratorMode = _jp._pyEnum(_jp.cern.accsoft.commons.domain.modes.PsbAcceleratorMode)
LhcAcceleratorMode = _jp._pyEnum(_jp.cern.accsoft.commons.domain.modes.LhcAcceleratorMode)
SpsAcceleratorMode = _jp._pyEnum(_jp.cern.accsoft.commons.domain.modes.SpsAcceleratorMode)
PsAcceleratorMode = _jp._pyEnum(_jp.cern.accsoft.commons.domain.modes.PsAcceleratorMode)
LeirAcceleratorMode = _jp._pyEnum(_jp.cern.accsoft.commons.domain.modes.LeirAcceleratorMode)
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
