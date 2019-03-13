from . import jpype_lsa as _jp

# Contexts
ContextFamily = _jp._pyEnum(_jp.cern.lsa.domain.settings.ContextFamily)
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

# Accsoft Common
CernAccelerator = _jp._pyEnum(_jp.cern.accsoft.commons.domain.CernAccelerator)
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

