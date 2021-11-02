import cern.accsoft.commons.domain.beams
import cern.accsoft.commons.domain.lhc
import cern.accsoft.commons.util
import cern.lsa.domain.cern.devices
import cern.lsa.domain.commons.spi
import java.io
import java.util
import typing



class BlmCrateInfoImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.devices.BlmCrateInfo], cern.lsa.domain.cern.devices.BlmCrateInfo):
    """
    public class BlmCrateInfoImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`> implements :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
    
        Default implementation of the :code:`BlmCrateInfo` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str): ...
    @staticmethod
    def getBeanPropertyNameByFESAFieldName(string: str) -> str:
        """
            Returns name of :code:`BlmCrateInfo` property for given field name of BLECSFlash property.
        
            Parameters:
                fesaFieldName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the field of BLECSFlash property
        
        
        """
        ...
    def getBlecfPresent(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getBlecfPresent`
            Returns encoded information about presence of CF sub cards. On every BLM crate there might be up to 16 cards (TC), each
            with two sub cards (CF) which gives in total 32 CF sub cards. The most significant bit (MSB) in the returned value
            corresponds to the sub card A of the first card (nr 1). The least significant bit (LSB) in the returned value
            corresponds to the sub card B of the last card (nr 16).
        
            The verification whether the sub card is present or not is done based on BLM expert names i.e. whether the names start
            with 'BLMM.' prefix (spare BLMs). If all BLMs on a given sub card are spare - this means that the sub card is not
            present and the corresponding bit is set to 0. If there is at least one BLM which is not spare on a given sub card - the
            corresponding bit is set to 1.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getBlecfPresent`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                encoded BLECF presence flags which corresponds to the FESA field: BLMLHC:BLECSFlash:blecsFBLECFPRES
        
        
        """
        ...
    def getBlecsFirmwareVersion(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getBlecsFirmwareVersion`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
        
        
        """
        ...
    def getBlecsSerial(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getBlecsSerial`
            Serial number of the combiner board.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getBlecsSerial`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                the blecsSerial
        
        
        """
        ...
    def getBletcPresent(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getBletcPresent`
            Returns encoded information about presence of cards. On every BLM crate there might be up to 16 cards (TC). The most
            significant bit (MSB) in the returned value corresponds to the first card (nr 1). The bit with index MSB - 16 in the
            returned value corresponds to the last card (nr 16).
        
            The verification whether the card is present or not is done based on BLM expert names i.e. whether the names start with
            'BLMM.' prefix (spare BLMs). If all BLMs on a given card are spare - this means that the card is not present and the
            corresponding bit is set to 0. If there is at least one BLM which is not spare on a given card - the corresponding bit
            is set to 1.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getBletcPresent`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                encoded BLETC presence flags which corresponds to the FESA field: BLMLHC:BLECSFlash:blecsFBLETCPRES
        
        
        """
        ...
    def getChannelCableConnected(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getChannelCableConnected`
            Returns and array of 8 integers which contain information about whether each channel is
            :meth:`~cern.lsa.domain.cern.devices.BlmInfo.isCableConnected`. Since there are 256 channels on each crate and one
            integer has 32 bits - we need 8 integers to encode these 256 flags. The most significant bit (MSB) of the first element
            of this array corresponds to the first channel on the first card (number 1). The least significant bit (LSB) of the last
            element of this array corresponds to the last channel of the last card (number 16). If the bit is set to 1 - the channel
            is cable connected, if it's 0 - it's not connected.
        
            If channel is cable connected - it means that there is physically connected monitor on the channel. This status is used
            in the connectivity check.
        
            This property is populated from IS_CABLE_CONNECTED column.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getChannelCableConnected`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                encoded channel present flags which corresponds to FESA field: BLMLHC:BLECSFlash:blecsFCHPRES.
        
        
        """
        ...
    def getExpertNames(self) -> typing.List[typing.List[str]]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getExpertNames`
            Returns the 2 dimensional array [cardIndex-1][channelIndex-1] containing the expert names
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getExpertNames`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
        
        
        """
        ...
    def getHvcfcTestHv(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getHvcfcTestHv`
            Settings for High Voltage of monitors (per IP).
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getHvcfcTestHv`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getHvcfcTestHvPeak(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getHvcfcTestHvPeak`
            Settings for High Voltage of monitors (per IP).
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getHvcfcTestHvPeak`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getLastLSAModification(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getLastLSAModification`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                the lastLSAModification
        
        
        """
        ...
    def getLhcInteractionPoint(self) -> cern.accsoft.commons.domain.lhc.LhcInteractionPoint:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getLhcInteractionPoint`
            Returns the LHC Interaction Point that this crate belongs to.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getLhcInteractionPoint`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                the LHC Interaction Point of this BLM crate
        
        
        """
        ...
    def getMod1GainMax(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod1GainMax`
            Thresholds for the connectivity check test.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod1GainMax`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod1GainMin(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod1GainMin`
            Thresholds for the connectivity check test.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod1GainMin`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod1Period(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod1Period`
            Returns modulation period for first frequency.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod1Period`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                modulation period for first frequency
        
        
        """
        ...
    def getMod1PhaseMax(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod1PhaseMax`
            Thresholds for the connectivity check test.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod1PhaseMax`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod1PhaseMin(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod1PhaseMin`
            Thresholds for the connectivity check test.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod1PhaseMin`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod1Voltage(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod1Voltage`
            Returns modulation voltage for first frequency.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod1Voltage`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                modulation voltage for first frequency
        
        
        """
        ...
    def getMod2GainMax(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod2GainMax`
            Thresholds for the connectivity check test.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod2GainMax`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod2GainMin(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod2GainMin`
            Thresholds for the connectivity check test.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod2GainMin`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod2Period(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod2Period`
            Returns modulation period for second frequency.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod2Period`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                modulation period for second frequency
        
        
        """
        ...
    def getMod2PhaseMax(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod2PhaseMax`
            Thresholds for the connectivity check test.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod2PhaseMax`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod2PhaseMin(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod2PhaseMin`
            Thresholds for the connectivity check test.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod2PhaseMin`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod2Voltage(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod2Voltage`
            Returns modulation voltage for second frequency.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getMod2Voltage`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                modulation voltage for second frequency
        
        
        """
        ...
    def getModTestHv(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getModTestHv`
            Settings for High Voltage of monitors (per IP).
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getModTestHv`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getNormalOpHv(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getNormalOpHv`
            Settings for High Voltage of monitors (per IP).
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getNormalOpHv`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getNormalOpHv1Hv2Diff(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getNormalOpHv1Hv2Diff`
            Settings for High Voltage of monitors (per IP).
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getNormalOpHv1Hv2Diff`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getOfficialNames(self) -> typing.List[typing.List[str]]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getOfficialNames`
            Returns the 2 dimensional array [cardIndex-1][channelIndex-1] containing the official names
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getOfficialNames`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
        
        
        """
        ...
    def getRdacResetHv(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getRdacResetHv`
            Settings for High Voltage of monitors (per IP).
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getRdacResetHv`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getRdacResetHvPeak(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getRdacResetHvPeak`
            Settings for High Voltage of monitors (per IP).
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getRdacResetHvPeak`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getRgohResetHv(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getRgohResetHv`
            Settings for High Voltage of monitors (per IP).
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getRgohResetHv`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getRgohResetHvPeak(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getRgohResetHvPeak`
            Settings for High Voltage of monitors (per IP).
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmCrateInfo.getRgohResetHvPeak`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmCrateInfo`
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def setBlecfSerial(self, int: int, int2: int, int3: int) -> None:
        """
            Sets CF serial of indicated BLM within the crate.
        
            Parameters:
                cardIndex (int): : The card number of BLM in the crate (1 -> 16)
                channelIndex (int): : The channel index of BLM in the crate (1 -> 16)
                serial (int): the CF serial number
        
        
        """
        ...
    def setBlecsFirmwareVersion(self, int: int) -> None:
        """
        
            Parameters:
                blecsFirmV (int): the blecsFirmV to set
        
        
        """
        ...
    def setBlecsSerial(self, long: int) -> None:
        """
        
            Parameters:
                blecsSerial (long): the blecsSerial to set
        
        
        """
        ...
    def setBletcSerial(self, int: int, int2: int, long: int) -> None:
        """
            Sets TC serial of indicated BLM within the crate.
        
            Parameters:
                cardIndex (int): : The card number of BLM in the crate (1 -> 16)
                channelIndex (int): : The channel index of BLM in the crate (1 -> 16)
                serial (long): the TC serial number
        
        
        """
        ...
    def setChannelCableConnected(self, int: int, boolean: bool) -> None: ...
    def setExpertName(self, int: int, int2: int, string: str) -> None:
        """
            Sets expert name of indicated BLM within the crate.
        
            Parameters:
                expertName (int):         cardIndex (int): : The card number of BLM in the crate (1 -> 16)
                channelIndex (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): : The channel index of BLM in the crate (1 -> 16)
        
        
        """
        ...
    def setHvcfcTestHv(self, int: int) -> None:
        """
        
            Parameters:
                hvcfcTestHv (int): the hvcfcTestHv to set
        
        
        """
        ...
    def setHvcfcTestHvPeak(self, int: int) -> None:
        """
        
            Parameters:
                hvcfcTestHvPeak (int): the hvcfcTestHvPeak to set
        
        
        """
        ...
    def setLastLSAModification(self, long: int) -> None:
        """
        
            Parameters:
                lastLSAModification (long): the lastLSAModification to set
        
        
        """
        ...
    def setLhcInteractionPoint(self, lhcInteractionPoint: cern.accsoft.commons.domain.lhc.LhcInteractionPoint) -> None:
        """
        
            Parameters:
                lhcIp (cern.accsoft.commons.domain.lhc.LhcInteractionPoint): the lhcIp to set
        
        
        """
        ...
    def setMod1GainMax(self, int: int, short: int) -> None:
        """
        
            Parameters:
                mod1GainMax (int): the mod1GainMax to set
        
        
        """
        ...
    def setMod1GainMin(self, int: int, short: int) -> None:
        """
        
            Parameters:
                mod1GainMin (int): the mod1GainMin to set
        
        
        """
        ...
    def setMod1Period(self, int: int) -> None:
        """
        
            Parameters:
                mod1Period (int): the mod1Period to set
        
        
        """
        ...
    def setMod1PhaseMax(self, int: int, short: int) -> None:
        """
        
            Parameters:
                mod1PhaseMax (int): the mod1PhaseMax to set
        
        
        """
        ...
    def setMod1PhaseMin(self, int: int, short: int) -> None:
        """
        
            Parameters:
                mod1PhaseMin (int): the mod1PhaseMin to set
        
        
        """
        ...
    def setMod1Voltage(self, int: int) -> None:
        """
        
            Parameters:
                mod1Voltage (int): the mod1Voltage to set
        
        
        """
        ...
    def setMod2GainMax(self, int: int, short: int) -> None:
        """
        
            Parameters:
                mod2GainMax (int): the mod2GainMax to set
        
        
        """
        ...
    def setMod2GainMin(self, int: int, short: int) -> None:
        """
        
            Parameters:
                mod2GainMin (int): the mod2GainMin to set
        
        
        """
        ...
    def setMod2Period(self, int: int) -> None:
        """
        
            Parameters:
                mod2Period (int): the mod2Period to set
        
        
        """
        ...
    def setMod2PhaseMax(self, int: int, short: int) -> None:
        """
        
            Parameters:
                mod2PhaseMax (int): the mod2PhaseMax to set
        
        
        """
        ...
    def setMod2PhaseMin(self, int: int, short: int) -> None:
        """
        
            Parameters:
                mod2PhaseMin (int): the mod2PhaseMin to set
        
        
        """
        ...
    def setMod2Voltage(self, int: int) -> None:
        """
        
            Parameters:
                mod2Voltage (int): the mod2Voltage to set
        
        
        """
        ...
    def setModTestHv(self, int: int) -> None:
        """
        
            Parameters:
                modTestHv (int): the modTestHv to set
        
        
        """
        ...
    def setNormalOpHv(self, int: int) -> None:
        """
        
            Parameters:
                normalOpHv (int): the normalOpHv to set
        
        
        """
        ...
    def setNormalOpHv1Hv2Diff(self, int: int) -> None:
        """
        
            Parameters:
                normalOpHv1Hv2Diff (int): the normalOpHv1Hv2Diff to set
        
        
        """
        ...
    def setOfficialName(self, int: int, int2: int, string: str) -> None:
        """
            Sets official name of indicated BLM within the crate.
        
            Parameters:
                officialName (int):         cardIndex (int): : The card number of BLM in the crate (1 -> 16)
                channelIndex (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): : The channel index of BLM in the crate (1 -> 16)
        
        
        """
        ...
    def setRdacResetHv(self, int: int) -> None:
        """
        
            Parameters:
                rdacResetHv (int): the rdacResetHv to set
        
        
        """
        ...
    def setRdacResetHvPeak(self, int: int) -> None:
        """
        
            Parameters:
                rdacResetHvPeak (int): the rdacResetHvPeak to set
        
        
        """
        ...
    def setRgohResetHv(self, int: int) -> None:
        """
        
            Parameters:
                rgohResetHv (int): the rgohResetHv to set
        
        
        """
        ...
    def setRgohResetHvPeak(self, int: int) -> None:
        """
        
            Parameters:
                rgohResetHvPeak (int): the rgohResetHvPeak to set
        
        
        """
        ...

class BlmFamilyImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.devices.BlmFamily], cern.lsa.domain.cern.devices.BlmFamily):
    """
    public class BlmFamilyImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.cern.devices.BlmFamily`> implements :class:`~cern.lsa.domain.cern.devices.BlmFamily`
    
    
        Also see:
            :class:`~cern.lsa.domain.cern.devices.BlmFamily`, :meth:`~serialized`
    """
    def __init__(self, string: str, double: float, double2: float): ...
    def addThresholds(self, int: int, longArray: typing.List[int]) -> None:
        """
        
            Parameters:
                energyLevel (int):         thresholdsToAdd (long[]): 
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :code:`equals` in class :class:`~cern.lsa.domain.cern.devices.BlmFamily`
        
        
        """
        ...
    def getAmpsFactor(self) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmFamily.getAmpsFactor`
            Returns special conversion factor used to calculate Amps based on Greys. Defined per BLM Family.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmFamily.getAmpsFactor`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmFamily`
        
            Returns:
                the ampsFactor
        
        
        """
        ...
    def getGysFactor(self) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmFamily.getGysFactor`
            Returns special conversion factor used to calculate Greys based on Blm bits. Defined per BLM Family.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmFamily.getGysFactor`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmFamily`
        
            Returns:
                the gysFactor
        
        
        """
        ...
    def getThresholds(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmFamily.getThresholds`
            Returns the thresholds Master Table for the family.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmFamily.getThresholds`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmFamily`
        
            Returns:
                an array representing a row-major matrix, indexed by the energy levels (rows) and the running sums (columns).
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :code:`hashCode` in class :class:`~cern.lsa.domain.cern.devices.BlmFamily`
        
        
        """
        ...
    def setAmpsFactor(self, double: float) -> None: ...
    def setFamilyName(self, string: str) -> None: ...
    def setGysFactor(self, double: float) -> None:
        """
        
            Parameters:
                gysFactor (double): the gysFactor to set
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.cern.devices.BlmFamily`
        
        
        """
        ...

class BlmInfoImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.devices.BlmInfo], cern.lsa.domain.cern.devices.ThresholdsAwareBlmInfo, java.io.Serializable):
    """
    public class BlmInfoImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.cern.devices.BlmInfo`> implements :class:`~cern.lsa.domain.cern.devices.ThresholdsAwareBlmInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :class:`~cern.lsa.domain.cern.devices.BlmInfo`, :meth:`~serialized`
    """
    SPARE_BLM_NAME_PREFIX: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SPARE_BLM_NAME_PREFIX
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str): ...
    def addAppliedThresholds(self, int: int, longArray: typing.List[int]) -> None: ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :code:`equals` in class :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
        
        """
        ...
    def getAppliedThresholds(self) -> typing.List[typing.List[int]]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.ThresholdsAwareBlmInfo.getAppliedThresholds`
            Returns applied table for this BLM from BLM_APPLIED_THRESHOLDS if loaded or :code:`null`. The first dimension specifies
            beam energy and the second - running sum.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.ThresholdsAwareBlmInfo.getAppliedThresholds`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.ThresholdsAwareBlmInfo`
        
            Returns:
                applied thresholds table
        
        
        """
        ...
    def getBlecfSerial(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getBlecfSerial`
            Returns BLECF card serial number.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getBlecfSerial`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                BLECF card serial number.
        
        
        """
        ...
    def getBletcFirmwareVersion(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getBletcFirmwareVersion`
            Returns the bletc firmware version.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getBletcFirmwareVersion`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                the bletc firmware version
        
        
        """
        ...
    def getBletcSerial(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getBletcSerial`
            Returns BLETC card serial number.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getBletcSerial`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                BLETC card serial number.
        
        
        """
        ...
    def getBlmFamily(self) -> cern.lsa.domain.cern.devices.BlmFamily:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getBlmFamily`
            Returns BLM family that this BLM belongs to. The method can return :code:`null` in case the BLM doesn't belong to any
            family e.g. when this object represents a spare slot or a mobile BLM.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getBlmFamily` in interface :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                blmFamily or :code:`null`
        
        
        """
        ...
    def getCardIndex(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getCardIndex`
            Returns the crate card index.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getCardIndex` in interface :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                crate card index of this BLM.
        
        
        """
        ...
    def getChannelIndex(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getChannelIndex`
            Returns the crate card channel index.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getChannelIndex`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                crate card channel index of this BLM.
        
        
        """
        ...
    def getCrateName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getCrateName`
            Returns the name of the crate hosting the BLM.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getCrateName` in interface :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                crate name hosting the BLM.
        
        
        """
        ...
    def getDcum(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getDcum`
            Returns DCUM number for the BLM. It is a position of this BLM in the ring.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getDcum` in interface :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                dcum value for a BLM
        
        
        """
        ...
    def getFilterValueCapacitor(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getFilterValueCapacitor`
            Returns capacitor value of the filter in the input channel of the monitor.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getFilterValueCapacitor`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
        
        """
        ...
    def getFilterValueResistor(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getFilterValueResistor`
            Returns resistor value of the filter in the input channel of the monitor.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getFilterValueResistor`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
        
        """
        ...
    def getIncludedRunningSums(self) -> typing.List[bool]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getIncludedRunningSums`
            Returns an array of 12 boolean values denoting whether their corresponding acq/threshold values for a certain BLM are
            included in Logging process. Namely, n-th boolean value indicates whether n-th acquired/threshold BLM value is
            monitored.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getIncludedRunningSums`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                the includedThresholds
        
        
        """
        ...
    def getLastLSAModification(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getLastLSAModification`
            Returns the moment (number of milliseconds since January 1, 1970, 00:00:00 GMT) of last modification of LSA database.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getLastLSAModification`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
        
        
        """
        ...
    def getLhcInteractionPoint(self) -> cern.accsoft.commons.domain.lhc.LhcInteractionPoint:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getLhcInteractionPoint`
            Returns the LHC Interaction Point that this BLM is installed in.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getLhcInteractionPoint`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                the LHC Interaction Point of this BLM
        
        
        """
        ...
    def getMobileName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getMobileName`
            Returns name of a mobile monitor. If this :code:`BlmInfo` doesn't represent a mobile BLM - :code:`null` value is
            returned.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getMobileName` in interface :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                name of a mobile monitor or :code:`null` if it's not mobile
        
            Also see:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.isSpare`
        
        
        """
        ...
    def getOfficialName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getOfficialName`
            Return BLM official name.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getOfficialName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                the BLM official name.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :code:`hashCode` in class :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
        
        """
        ...
    def isCableConnected(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.isCableConnected`
            If channel is cable connected - it means that there is physically connected monitor on the channel. This status is used
            in the connectivity check.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.isCableConnected`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
        
        """
        ...
    def isConnectedToBis(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.isConnectedToBis`
            Returns :code:`true` if this BLM is connected to the Beam Interlock System, :code:`false` if it's not connected.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.isConnectedToBis`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                the isConnectedToBis
        
        
        """
        ...
    def isMasked(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.isMasked`
            Returns :code:`true` if this BLM is masked i.e. if this BLM sends signals to maskable BIS interface.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.isMasked` in interface :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                the masked
        
        
        """
        ...
    def isSpare(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.BlmInfo.isSpare`
            Specifies if this BlmInfo represents a spare slot in the crate (which can be used to install a mobile BLM). If the
            method returns :code:`true` - it doesn't mean that it represents a mobile BLM. To check this use
            :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getMobileName`
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.isSpare` in interface :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
            Returns:
                :code:`true` if this :code:`BlmInfo` represents a spare slot in the crate (which can be used to install a mobile BLM).
        
            Also see:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getMobileName`
        
        
        """
        ...
    def setBlecfSerial(self, int: int) -> None:
        """
            Sets the BLECF card serial number.
        
            Parameters:
                blecfSerial (int): BLECF card serial number
        
        
        """
        ...
    def setBletcFirmwareVersion(self, int: int) -> None: ...
    def setBletcSerial(self, long: int) -> None:
        """
            Sets bletcSerial property
        
            Parameters:
                bletcSerial (long): 
        
        """
        ...
    def setBlmFamily(self, blmFamily: cern.lsa.domain.cern.devices.BlmFamily) -> None:
        """
            Sets :code:`blmFamily` property.
        
            Parameters:
                blmFamily (:class:`~cern.lsa.domain.cern.devices.BlmFamily`): the :code:`blmFamily` to set
        
        
        """
        ...
    def setCableConnected(self, boolean: bool) -> None:
        """
        
            Parameters:
                isCableConnected (boolean): the is_cable_connected to set
        
        
        """
        ...
    def setCardIndex(self, int: int) -> None:
        """
            Sets :code:`cardIndex` property.
        
            Parameters:
                cardIndex (int): the :code:`cardIndex` to set
        
        
        """
        ...
    def setChannelIndex(self, int: int) -> None:
        """
            Sets :code:`channelIndex` property.
        
            Parameters:
                channelIndex (int): the :code:`channelIndex` to set
        
        
        """
        ...
    def setConnectedToBis(self, boolean: bool) -> None:
        """
        
            Parameters:
                isConnectedToBis (boolean): the isConnectedToBis to set
        
        
        """
        ...
    def setCrateName(self, string: str) -> None:
        """
            Sets :code:`crateName` property.
        
            Parameters:
                crateName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the :code:`crateName` to set
        
        
        """
        ...
    def setDcum(self, int: int) -> None:
        """
            Sets :code:`dcum` property.
        
            Parameters:
                dcum (int): the :code:`dcum` to set
        
        
        """
        ...
    def setFilterValueCapacitor(self, int: int) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.cern.devices.spi.BlmInfoImpl.getFilterValueCapacitor`
        
        
        """
        ...
    def setFilterValueResistor(self, int: int) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.cern.devices.spi.BlmInfoImpl.getFilterValueResistor`
        
        
        """
        ...
    def setIncludedRunningSums(self, booleanArray: typing.List[bool]) -> None:
        """
            Sets :code:`includedRunningSums` property.
        
            Parameters:
                includedRunningSums (boolean[]): the :code:`includedRunningSums` to set
        
        
        """
        ...
    def setLastLSAModification(self, long: int) -> None: ...
    def setLhcInteractionPoint(self, lhcInteractionPoint: cern.accsoft.commons.domain.lhc.LhcInteractionPoint) -> None:
        """
        
            Parameters:
                lhcIp (cern.accsoft.commons.domain.lhc.LhcInteractionPoint): the lhcIp to set
        
        
        """
        ...
    def setMasked(self, boolean: bool) -> None:
        """
        
            Parameters:
                masked (boolean): the masked to set
        
        
        """
        ...
    def setMobileName(self, string: str) -> None:
        """
            Sets :code:`mobileName` property.
        
            Parameters:
                mobileName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the :code:`mobileName` to set
        
        
        """
        ...
    def setOfficialName(self, string: str) -> None:
        """
            Sets :code:`officialName` property.
        
            Parameters:
                officialName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the :code:`officialName` to set
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.cern.devices.BlmInfo`
        
        
        """
        ...

class CollimatorAlignmentImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedEntity[cern.lsa.domain.cern.devices.CollimatorAlignment], cern.lsa.domain.cern.devices.CollimatorAlignment):
    """
    public class CollimatorAlignmentImpl extends cern.lsa.domain.commons.spi.AbstractIdentifiedEntity<:class:`~cern.lsa.domain.cern.devices.CollimatorAlignment`> implements :class:`~cern.lsa.domain.cern.devices.CollimatorAlignment`
    
    
        Also see:
            :class:`~cern.lsa.domain.cern.devices.CollimatorAlignment`, :meth:`~serialized`
    """
    def __init__(self): ...
    def getAlignmentTime(self) -> java.util.Date:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.CollimatorAlignment.getAlignmentTime`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.CollimatorAlignment`
        
            Returns:
                the time when the collimator was aligned
        
        
        """
        ...
    def getBeamModeCategory(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.CollimatorAlignment.getBeamModeCategory`
            Returns the name of the collimator-related beam mode category (e.g. FLATTOP, INJECTION, PHYSICS, SQUEEZED)
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.CollimatorAlignment.getBeamModeCategory`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.CollimatorAlignment`
        
            Returns:
                the name of the beam mode category
        
        
        """
        ...
    def getCollimatorName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.CollimatorAlignment.getCollimatorName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.CollimatorAlignment`
        
            Returns:
                the associated collimator name
        
        
        """
        ...
    def getLeftJawPos(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.CollimatorAlignment.getLeftJawPos`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.CollimatorAlignment`
        
        
        """
        ...
    def getOpticName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.CollimatorAlignment.getOpticName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.CollimatorAlignment`
        
        
        """
        ...
    def getRightJawPos(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.CollimatorAlignment.getRightJawPos`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.CollimatorAlignment`
        
        
        """
        ...
    def getTcp1LeftPos(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.CollimatorAlignment.getTcp1LeftPos`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.CollimatorAlignment`
        
        
        """
        ...
    def getTcp1RightPos(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.CollimatorAlignment.getTcp1RightPos`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.CollimatorAlignment`
        
        
        """
        ...
    def getTcp2LeftPos(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.CollimatorAlignment.getTcp2LeftPos`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.CollimatorAlignment`
        
        
        """
        ...
    def getTcp2RightPos(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.CollimatorAlignment.getTcp2RightPos`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.CollimatorAlignment`
        
        
        """
        ...
    def setAlignmentTime(self, date: java.util.Date) -> None: ...
    def setBeamModeCategory(self, string: str) -> None: ...
    def setCollimatorName(self, string: str) -> None: ...
    def setLeftJawPos(self, float: float) -> None: ...
    def setOpticName(self, string: str) -> None: ...
    def setRightJawPos(self, float: float) -> None: ...
    def setTcp1LeftPos(self, float: float) -> None: ...
    def setTcp1RightPos(self, float: float) -> None: ...
    def setTcp2LeftPos(self, float: float) -> None: ...
    def setTcp2RightPos(self, float: float) -> None: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class LhcBeamLossMapImpl(cern.lsa.domain.cern.devices.LhcBeamLossMap, java.io.Serializable):
    """
    public class LhcBeamLossMapImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.devices.LhcBeamLossMap`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.lsa.domain.cern.devices.LhcBeamLossMap` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, list: java.util.List[cern.lsa.domain.cern.devices.LhcBeamLossMap.LhcBeamLossMapEntry]): ...
    def getAllEntries(self) -> java.util.List[cern.lsa.domain.cern.devices.LhcBeamLossMap.LhcBeamLossMapEntry]: ...
    def getEntry(self, lhcBeam: cern.accsoft.commons.domain.beams.LhcBeam, string: str, string2: str) -> cern.lsa.domain.cern.devices.LhcBeamLossMap.LhcBeamLossMapEntry:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.LhcBeamLossMap.getEntry`
            Returns the beam loss map entry for the specified triplet.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcBeamLossMap.getEntry`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcBeamLossMap`
        
            Parameters:
                beam (cern.accsoft.commons.domain.beams.LhcBeam): the beam identifier
                configType (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): configuration type name
                beamModeCategory (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the beam mode category
        
            Returns:
                the beam loss map entry for the specified triplet or :code:`null` if such entry does not exist i.e. there is no validity
                period defined for given triplet.
        
        
        """
        ...
    class LhcBeamLossMapEntryImpl(cern.lsa.domain.cern.devices.LhcBeamLossMap.LhcBeamLossMapEntry):
        def __init__(self, lhcBeam: cern.accsoft.commons.domain.beams.LhcBeam, string: str, string2: str, long: int, long2: int): ...
        def getBeam(self) -> cern.accsoft.commons.domain.beams.LhcBeam: ...
        def getBeamModeCategory(self) -> str: ...
        def getConfigType(self) -> str: ...
        def getValidFrom(self) -> int: ...
        def getValidTo(self) -> int: ...

class LhcCollimatorInfoImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.devices.LhcCollimatorInfo], cern.lsa.domain.cern.devices.LhcCollimatorInfo):
    """
    public class LhcCollimatorInfoImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`> implements :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def getAngle(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getAngle`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the angle
        
        
        """
        ...
    def getAutoRetractionLeftDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getAutoRetractionLeftDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the autoRetractionLeftDown
        
        
        """
        ...
    def getAutoRetractionLeftUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getAutoRetractionLeftUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the autoRetractionLeftUp
        
        
        """
        ...
    def getAutoRetractionRightDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getAutoRetractionRightDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the autoRetractionRightDown
        
        
        """
        ...
    def getAutoRetractionRightUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getAutoRetractionRightUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the autoRetractionRightUp
        
        
        """
        ...
    def getAxisLeftDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getAxisLeftDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the axisLeftDown
        
        
        """
        ...
    def getAxisLeftUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getAxisLeftUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the axisLeftUp
        
        
        """
        ...
    def getAxisRightDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getAxisRightDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the axisRightDown
        
        
        """
        ...
    def getAxisRightUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getAxisRightUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the axisRightUp
        
        
        """
        ...
    def getAxisTank(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getAxisTank`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the axisTank
        
        
        """
        ...
    def getBeam(self) -> cern.accsoft.commons.domain.beams.LhcBeam:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBeam`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the beam
        
        
        """
        ...
    def getBlmi(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBlmi`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the blmi
        
        
        """
        ...
    def getBlmi2(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBlmi2`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the blmi2
        
        
        """
        ...
    def getBlms(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBlms`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the blms
        
        
        """
        ...
    def getBlms2(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBlms2`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the blms2
        
        
        """
        ...
    def getBpmBtnAttnCoeffLeftDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnAttnCoeffLeftDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnAttnCoeffLeftUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnAttnCoeffLeftUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnAttnCoeffRightDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnAttnCoeffRightDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnAttnCoeffRightUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnAttnCoeffRightUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnCapacitanceLeftDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnCapacitanceLeftDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnCapacitanceLeftUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnCapacitanceLeftUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnCapacitanceRightDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnCapacitanceRightDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnCapacitanceRightUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnCapacitanceRightUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnDiameterLeftDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnDiameterLeftDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnDiameterLeftUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnDiameterLeftUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnDiameterRightDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnDiameterRightDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnDiameterRightUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnDiameterRightUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnDistToJawLeftDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnDistToJawLeftDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnDistToJawLeftUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnDistToJawLeftUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnDistToJawRightDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnDistToJawRightDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnDistToJawRightUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnDistToJawRightUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnDistToSfcLeftDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnDistToSfcLeftDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnDistToSfcLeftUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnDistToSfcLeftUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnDistToSfcRightDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnDistToSfcRightDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmBtnDistToSfcRightUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmBtnDistToSfcRightUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmChannelIdLeftDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmChannelIdLeftDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmChannelIdLeftUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmChannelIdLeftUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmChannelIdRightDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmChannelIdRightDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmChannelIdRightUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmChannelIdRightUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmFrontEndIdDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmFrontEndIdDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmFrontEndIdUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmFrontEndIdUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmNameDown(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmNameDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmNameE(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmNameE`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getBpmNameUp(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getBpmNameUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getCercaName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getCercaName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the cercaName
        
        
        """
        ...
    def getDisplayName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getDisplayName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the displayName
        
        
        """
        ...
    def getFamily(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getFamily`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the family
        
        
        """
        ...
    def getJawLeftDown(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getJawLeftDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the jawLeftDown
        
        
        """
        ...
    def getJawLeftUp(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getJawLeftUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the jawLeftUp
        
        
        """
        ...
    def getJawRightDown(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getJawRightDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the jawRightDown
        
        
        """
        ...
    def getJawRightUp(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getJawRightUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the jawRightUp
        
        
        """
        ...
    def getLastUpdate(self) -> java.util.Date:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getLastUpdate`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the lastUpdate
        
        
        """
        ...
    def getLength(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the length
        
        
        """
        ...
    def getMaterial(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getMaterial`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the material
        
        
        """
        ...
    def getMaxFlatErrLeft(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getMaxFlatErrLeft`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the maxFlatErrLeft
        
        
        """
        ...
    def getMaxFlatErrRight(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getMaxFlatErrRight`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the maxFlatErrRight
        
        
        """
        ...
    def getMaxTiltLeftMinus(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getMaxTiltLeftMinus`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the maxTiltLeftMinus
        
        
        """
        ...
    def getMaxTiltLeftPlus(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getMaxTiltLeftPlus`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the maxTiltLeftPlus
        
        
        """
        ...
    def getMaxTiltRightMinus(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getMaxTiltRightMinus`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the maxTiltRightMinus
        
        
        """
        ...
    def getMaxTiltRightPlus(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getMaxTiltRightPlus`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the maxTiltRightPlus
        
        
        """
        ...
    def getMechPlayLeftDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getMechPlayLeftDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the mechPlayLeftDown
        
        
        """
        ...
    def getMechPlayLeftUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getMechPlayLeftUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the mechPlayLeftUp
        
        
        """
        ...
    def getMechPlayRightDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getMechPlayRightDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the mechPlayRightDown
        
        
        """
        ...
    def getMechPlayRightUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getMechPlayRightUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the mechPlayRightUp
        
        
        """
        ...
    def getMtfName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getMtfName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the mtfName
        
        
        """
        ...
    def getRegion(self) -> cern.lsa.domain.cern.devices.CollimatorRegion:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getRegion`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the collimator region
        
        
        """
        ...
    def getScrewSerialNumberLeftDown(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getScrewSerialNumberLeftDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getScrewSerialNumberLeftUp(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getScrewSerialNumberLeftUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getScrewSerialNumberRightDown(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getScrewSerialNumberRightDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getScrewSerialNumberRightUp(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getScrewSerialNumberRightUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def getStopAntiDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getStopAntiDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the stopAntiDown
        
        
        """
        ...
    def getStopAntiUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getStopAntiUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the stopAntiUp
        
        
        """
        ...
    def getStopLeftDownIn(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getStopLeftDownIn`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the stopLeftDownIn
        
        
        """
        ...
    def getStopLeftDownOut(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getStopLeftDownOut`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the stopLeftDownOut
        
        
        """
        ...
    def getStopLeftUpIn(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getStopLeftUpIn`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the stopLeftUpIn
        
        
        """
        ...
    def getStopLeftUpOut(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getStopLeftUpOut`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the stopLeftUpOut
        
        
        """
        ...
    def getStopRightDownIn(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getStopRightDownIn`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the stopRightDownIn
        
        
        """
        ...
    def getStopRightDownOut(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getStopRightDownOut`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the stopRightDownOut
        
        
        """
        ...
    def getStopRightUpIn(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getStopRightUpIn`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the stopRightUpIn
        
        
        """
        ...
    def getStopRightUpOut(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getStopRightUpOut`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the stopRightUpOut
        
        
        """
        ...
    def getSwitchAntiDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getSwitchAntiDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the switchAntiDown
        
        
        """
        ...
    def getSwitchAntiUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getSwitchAntiUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the switchAntiUp
        
        
        """
        ...
    def getSwitchLeftDownIn(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getSwitchLeftDownIn`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the switchLeftDownIn
        
        
        """
        ...
    def getSwitchLeftDownOut(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getSwitchLeftDownOut`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the switchLeftDownOut
        
        
        """
        ...
    def getSwitchLeftUpIn(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getSwitchLeftUpIn`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the switchLeftUpIn
        
        
        """
        ...
    def getSwitchLeftUpOut(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getSwitchLeftUpOut`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the switchLeftUpOut
        
        
        """
        ...
    def getSwitchRightDownIn(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getSwitchRightDownIn`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the switchRightDownIn
        
        
        """
        ...
    def getSwitchRightDownOut(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getSwitchRightDownOut`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the switchRightDownOut
        
        
        """
        ...
    def getSwitchRightUpIn(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getSwitchRightUpIn`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the switchRightUpIn
        
        
        """
        ...
    def getSwitchRightUpOut(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getSwitchRightUpOut`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the switchRightUpOut
        
        
        """
        ...
    def getTankCalibration(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getTankCalibration`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                tank calibration for fifth motor axis
        
        
        """
        ...
    def getTankPosSetPoint(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getTankPosSetPoint`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the tankPosSetPoint
        
        
        """
        ...
    def getTankPosStopDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getTankPosStopDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the tankPosStopDown
        
        
        """
        ...
    def getTankPosStopUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getTankPosStopUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the tankPosStopUp
        
        
        """
        ...
    def getTankPosSwitchDown(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getTankPosSwitchDown`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the tankPosSwitchDown
        
        
        """
        ...
    def getTankPosSwitchUp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.getTankPosSwitchUp`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
            Returns:
                the tankPosSwitchUp
        
        
        """
        ...
    def isBpmInstalled(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.isBpmInstalled`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def isTankBpmInstalled(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo.isTankBpmInstalled`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.LhcCollimatorInfo`
        
        
        """
        ...
    def setAngle(self, double: float) -> None:
        """
        
            Parameters:
                angle (double): the angle to set
        
        
        """
        ...
    def setAutoRetractionLeftDown(self, double: float) -> None:
        """
        
            Parameters:
                autoRetractionLeftDown (double): the autoRetractionLeftDown to set
        
        
        """
        ...
    def setAutoRetractionLeftUp(self, double: float) -> None:
        """
        
            Parameters:
                autoRetractionLeftUp (double): the autoRetractionLeftUp to set
        
        
        """
        ...
    def setAutoRetractionRightDown(self, double: float) -> None:
        """
        
            Parameters:
                autoRetractionRightDown (double): the autoRetractionRightDown to set
        
        
        """
        ...
    def setAutoRetractionRightUp(self, double: float) -> None:
        """
        
            Parameters:
                autoRetractionRightUp (double): the autoRetractionRightUp to set
        
        
        """
        ...
    def setAxisLeftDown(self, double: float) -> None:
        """
        
            Parameters:
                axisLeftDown (double): the axisLeftDown to set
        
        
        """
        ...
    def setAxisLeftUp(self, double: float) -> None:
        """
        
            Parameters:
                axisLeftUp (double): the axisLeftUp to set
        
        
        """
        ...
    def setAxisRightDown(self, double: float) -> None:
        """
        
            Parameters:
                axisRightDown (double): the axisRightDown to set
        
        
        """
        ...
    def setAxisRightUp(self, double: float) -> None:
        """
        
            Parameters:
                axisRightUp (double): the axisRightUp to set
        
        
        """
        ...
    def setAxisTank(self, double: float) -> None:
        """
        
            Parameters:
                axisTank (double): the axisTank to set
        
        
        """
        ...
    def setBeam(self, lhcBeam: cern.accsoft.commons.domain.beams.LhcBeam) -> None:
        """
        
            Parameters:
                beam (cern.accsoft.commons.domain.beams.LhcBeam): the beam to set
        
        
        """
        ...
    def setBlmi(self, string: str) -> None:
        """
        
            Parameters:
                blmi (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the blmi to set
        
        
        """
        ...
    def setBlmi2(self, string: str) -> None:
        """
        
            Parameters:
                blmi2 (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the blmi2 to set
        
        
        """
        ...
    def setBlms(self, string: str) -> None:
        """
        
            Parameters:
                blms (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the blms to set
        
        
        """
        ...
    def setBlms2(self, string: str) -> None:
        """
        
            Parameters:
                blms2 (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the blms2 to set
        
        
        """
        ...
    def setBpmBtnAttnCoeffLeftDown(self, double: float) -> None: ...
    def setBpmBtnAttnCoeffLeftUp(self, double: float) -> None: ...
    def setBpmBtnAttnCoeffRightDown(self, double: float) -> None: ...
    def setBpmBtnAttnCoeffRightUp(self, double: float) -> None: ...
    def setBpmBtnCapacitanceLeftDown(self, double: float) -> None: ...
    def setBpmBtnCapacitanceLeftUp(self, double: float) -> None: ...
    def setBpmBtnCapacitanceRightDown(self, double: float) -> None: ...
    def setBpmBtnCapacitanceRightUp(self, double: float) -> None: ...
    def setBpmBtnDiameterLeftDown(self, double: float) -> None: ...
    def setBpmBtnDiameterLeftUp(self, double: float) -> None: ...
    def setBpmBtnDiameterRightDown(self, double: float) -> None: ...
    def setBpmBtnDiameterRightUp(self, double: float) -> None: ...
    def setBpmBtnDistToJawLeftDown(self, double: float) -> None: ...
    def setBpmBtnDistToJawLeftUp(self, double: float) -> None: ...
    def setBpmBtnDistToJawRightDown(self, double: float) -> None: ...
    def setBpmBtnDistToJawRightUp(self, double: float) -> None: ...
    def setBpmBtnDistToSfcLeftDown(self, double: float) -> None: ...
    def setBpmBtnDistToSfcLeftUp(self, double: float) -> None: ...
    def setBpmBtnDistToSfcRightDown(self, double: float) -> None: ...
    def setBpmBtnDistToSfcRightUp(self, double: float) -> None: ...
    def setBpmChannelIdLeftDown(self, double: float) -> None: ...
    def setBpmChannelIdLeftUp(self, double: float) -> None: ...
    def setBpmChannelIdRightDown(self, double: float) -> None: ...
    def setBpmChannelIdRightUp(self, double: float) -> None: ...
    def setBpmFrontEndIdDown(self, double: float) -> None: ...
    def setBpmFrontEndIdUp(self, double: float) -> None: ...
    def setBpmInstalled(self, boolean: bool) -> None: ...
    def setBpmNameDown(self, string: str) -> None: ...
    def setBpmNameE(self, string: str) -> None: ...
    def setBpmNameUp(self, string: str) -> None: ...
    def setCercaName(self, string: str) -> None:
        """
        
            Parameters:
                cercaName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the cercaName to set
        
        
        """
        ...
    def setDisplayName(self, string: str) -> None:
        """
        
            Parameters:
                displayName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the displayName to set
        
        
        """
        ...
    def setFamily(self, string: str) -> None:
        """
        
            Parameters:
                family (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the family to set
        
        
        """
        ...
    def setJawLeftDown(self, string: str) -> None:
        """
        
            Parameters:
                jawLeftDown (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the jawLeftDown to set
        
        
        """
        ...
    def setJawLeftUp(self, string: str) -> None:
        """
        
            Parameters:
                jawLeftUp (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the jawLeftUp to set
        
        
        """
        ...
    def setJawRightDown(self, string: str) -> None:
        """
        
            Parameters:
                jawRightDown (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the jawRightDown to set
        
        
        """
        ...
    def setJawRightUp(self, string: str) -> None:
        """
        
            Parameters:
                jawRightUp (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the jawRightUp to set
        
        
        """
        ...
    def setLastUpdate(self, date: java.util.Date) -> None:
        """
        
            Parameters:
                lastUpdate (`Date <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true>`): the lastUpdate to set
        
        
        """
        ...
    def setLength(self, double: float) -> None:
        """
        
            Parameters:
                length (double): the length to set
        
        
        """
        ...
    def setMaterial(self, string: str) -> None:
        """
        
            Parameters:
                material (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the material to set
        
        
        """
        ...
    def setMaxFlatErrLeft(self, double: float) -> None:
        """
        
            Parameters:
                maxFlatErrLeft (double): the maxFlatErrLeft to set
        
        
        """
        ...
    def setMaxFlatErrRight(self, double: float) -> None:
        """
        
            Parameters:
                maxFlatErrRight (double): the maxFlatErrRight to set
        
        
        """
        ...
    def setMaxTiltLeftMinus(self, double: float) -> None:
        """
        
            Parameters:
                maxTiltLeftMinus (double): the maxTiltLeftMinus to set
        
        
        """
        ...
    def setMaxTiltLeftPlus(self, double: float) -> None:
        """
        
            Parameters:
                maxTiltLeftPlus (double): the maxTiltLeftPlus to set
        
        
        """
        ...
    def setMaxTiltRightMinus(self, double: float) -> None:
        """
        
            Parameters:
                maxTiltRightMinus (double): the maxTiltRightMinus to set
        
        
        """
        ...
    def setMaxTiltRightPlus(self, double: float) -> None:
        """
        
            Parameters:
                maxTiltRightPlus (double): the maxTiltRightPlus to set
        
        
        """
        ...
    def setMechPlayLeftDown(self, double: float) -> None:
        """
        
            Parameters:
                mechPlayLeftDown (double): the mechPlayLeftDown to set
        
        
        """
        ...
    def setMechPlayLeftUp(self, double: float) -> None:
        """
        
            Parameters:
                mechPlayLeftUp (double): the mechPlayLeftUp to set
        
        
        """
        ...
    def setMechPlayRightDown(self, double: float) -> None:
        """
        
            Parameters:
                mechPlayRightDown (double): the mechPlayRightDown to set
        
        
        """
        ...
    def setMechPlayRightUp(self, double: float) -> None:
        """
        
            Parameters:
                mechPlayRightUp (double): the mechPlayRightUp to set
        
        
        """
        ...
    def setMtfName(self, string: str) -> None:
        """
        
            Parameters:
                mtfName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the mtfName to set
        
        
        """
        ...
    def setRegion(self, collimatorRegion: cern.lsa.domain.cern.devices.CollimatorRegion) -> None:
        """
        
            Parameters:
                region (:class:`~cern.lsa.domain.cern.devices.CollimatorRegion`): the region to set
        
        
        """
        ...
    def setScrewSerialNumberLeftDown(self, string: str) -> None: ...
    def setScrewSerialNumberLeftUp(self, string: str) -> None: ...
    def setScrewSerialNumberRightDown(self, string: str) -> None: ...
    def setScrewSerialNumberRightUp(self, string: str) -> None: ...
    def setStopAntiDown(self, double: float) -> None:
        """
        
            Parameters:
                stopAntiDown (double): the stopAntiDown to set
        
        
        """
        ...
    def setStopAntiUp(self, double: float) -> None:
        """
        
            Parameters:
                stopAntiUp (double): the stopAntiUp to set
        
        
        """
        ...
    def setStopLeftDownIn(self, double: float) -> None:
        """
        
            Parameters:
                stopLeftDownIn (double): the stopLeftDownIn to set
        
        
        """
        ...
    def setStopLeftDownOut(self, double: float) -> None:
        """
        
            Parameters:
                stopLeftDownOut (double): the stopLeftDownOut to set
        
        
        """
        ...
    def setStopLeftUpIn(self, double: float) -> None:
        """
        
            Parameters:
                stopLeftUpIn (double): the stopLeftUpIn to set
        
        
        """
        ...
    def setStopLeftUpOut(self, double: float) -> None:
        """
        
            Parameters:
                stopLeftUpOut (double): the stopLeftUpOut to set
        
        
        """
        ...
    def setStopRightDownIn(self, double: float) -> None:
        """
        
            Parameters:
                stopRightDownIn (double): the stopRightDownIn to set
        
        
        """
        ...
    def setStopRightDownOut(self, double: float) -> None:
        """
        
            Parameters:
                stopRightDownOut (double): the stopRightDownOut to set
        
        
        """
        ...
    def setStopRightUpIn(self, double: float) -> None:
        """
        
            Parameters:
                stopRightUpIn (double): the stopRightUpIn to set
        
        
        """
        ...
    def setStopRightUpOut(self, double: float) -> None:
        """
        
            Parameters:
                stopRightUpOut (double): the stopRightUpOut to set
        
        
        """
        ...
    def setSwitchAntiDown(self, double: float) -> None:
        """
        
            Parameters:
                switchAntiDown (double): the switchAntiDown to set
        
        
        """
        ...
    def setSwitchAntiUp(self, double: float) -> None:
        """
        
            Parameters:
                switchAntiUp (double): the switchAntiUp to set
        
        
        """
        ...
    def setSwitchLeftDownIn(self, double: float) -> None:
        """
        
            Parameters:
                switchLeftDownIn (double): the switchLeftDownIn to set
        
        
        """
        ...
    def setSwitchLeftDownOut(self, double: float) -> None:
        """
        
            Parameters:
                switchLeftDownOut (double): the switchLeftDownOut to set
        
        
        """
        ...
    def setSwitchLeftUpIn(self, double: float) -> None:
        """
        
            Parameters:
                switchLeftUpIn (double): the switchLeftUpIn to set
        
        
        """
        ...
    def setSwitchLeftUpOut(self, double: float) -> None:
        """
        
            Parameters:
                switchLeftUpOut (double): the switchLeftUpOut to set
        
        
        """
        ...
    def setSwitchRightDownIn(self, double: float) -> None:
        """
        
            Parameters:
                switchRightDownIn (double): the switchRightDownIn to set
        
        
        """
        ...
    def setSwitchRightDownOut(self, double: float) -> None:
        """
        
            Parameters:
                switchRightDownOut (double): the switchRightDownOut to set
        
        
        """
        ...
    def setSwitchRightUpIn(self, double: float) -> None:
        """
        
            Parameters:
                switchRightUpIn (double): the switchRightUpIn to set
        
        
        """
        ...
    def setSwitchRightUpOut(self, double: float) -> None:
        """
        
            Parameters:
                switchRightUpOut (double): the switchRightUpOut to set
        
        
        """
        ...
    def setTankBpmInstalled(self, boolean: bool) -> None: ...
    def setTankCalibration(self, double: float) -> None:
        """
        
            Parameters:
                tankCalibration (double): 
        
        """
        ...
    def setTankPosSetPoint(self, double: float) -> None:
        """
        
            Parameters:
                tankPosSetPoint (double): the tankPosSetPoint to set
        
        
        """
        ...
    def setTankPosStopDown(self, double: float) -> None:
        """
        
            Parameters:
                tankPosStopDown (double): the tankPosStopDown to set
        
        
        """
        ...
    def setTankPosStopUp(self, double: float) -> None:
        """
        
            Parameters:
                tankPosStopUp (double): the tankPosStopUp to set
        
        
        """
        ...
    def setTankPosSwitchDown(self, double: float) -> None:
        """
        
            Parameters:
                tankPosSwitchDown (double): the tankPosSwitchDown to set
        
        
        """
        ...
    def setTankPosSwitchUp(self, double: float) -> None:
        """
        
            Parameters:
                tankPosSwitchUp (double): the tankPosSwitchUp to set
        
        
        """
        ...

class RfFgcChannelImpl(cern.lsa.domain.cern.devices.RfFgcChannel, java.io.Serializable):
    """
    public class RfFgcChannelImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.devices.RfFgcChannel`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def getChannelName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.RfFgcChannel.getChannelName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.RfFgcChannel`
        
            Returns:
                the name of the channel
        
        
        """
        ...
    def getChannelNumber(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.RfFgcChannel.getChannelNumber`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.RfFgcChannel`
        
            Returns:
                the channel number
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.RfFgcChannel.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.RfFgcChannel`
        
            Returns:
                the description of the parameter associated with the channel
        
        
        """
        ...
    def getFGCName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.RfFgcChannel.getFGCName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.RfFgcChannel`
        
            Returns:
                the name of the FGC the channel belongs to
        
        
        """
        ...
    def getMaxSlope(self) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.devices.RfFgcChannel.getMaxSlope`
            return tne maximum slope to be used when doing a PLP or CTRIM on the function
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.RfFgcChannel.getMaxSlope`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.RfFgcChannel`
        
            Returns:
        
        
        """
        ...
    def getMaxValue(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.RfFgcChannel.getMaxValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.RfFgcChannel`
        
            Returns:
                the max value of the parameter
        
        
        """
        ...
    def getMinValue(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.RfFgcChannel.getMinValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.RfFgcChannel`
        
            Returns:
                the min value of the parameter
        
        
        """
        ...
    def getParameterName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.RfFgcChannel.getParameterName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.RfFgcChannel`
        
            Returns:
                the name of the parameter associated with the channel
        
        
        """
        ...
    def getUnit(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.devices.RfFgcChannel.getUnit`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.devices.RfFgcChannel`
        
            Returns:
                the unit of the parameter associated with the channel
        
        
        """
        ...
    def setChannelName(self, string: str) -> None: ...
    def setChannelNumber(self, int: int) -> None: ...
    def setDescription(self, string: str) -> None: ...
    def setFGCName(self, string: str) -> None: ...
    def setMaxSlope(self, double: float) -> None: ...
    def setMaxValue(self, double: float) -> None: ...
    def setMinValue(self, double: float) -> None: ...
    def setParameterName(self, string: str) -> None: ...
    def setUnit(self, string: str) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.devices.spi")``.

    BlmCrateInfoImpl: typing.Type[BlmCrateInfoImpl]
    BlmFamilyImpl: typing.Type[BlmFamilyImpl]
    BlmInfoImpl: typing.Type[BlmInfoImpl]
    CollimatorAlignmentImpl: typing.Type[CollimatorAlignmentImpl]
    LhcBeamLossMapImpl: typing.Type[LhcBeamLossMapImpl]
    LhcCollimatorInfoImpl: typing.Type[LhcCollimatorInfoImpl]
    RfFgcChannelImpl: typing.Type[RfFgcChannelImpl]
