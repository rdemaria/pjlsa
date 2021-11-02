import cern.accsoft.commons.domain.beams
import cern.accsoft.commons.domain.lhc
import cern.accsoft.commons.util
import cern.lsa.domain.cern.devices.spi
import cern.lsa.domain.commons
import cern.lsa.domain.devices
import java.io
import java.lang
import java.util
import typing



class BlmCrateInfo(cern.accsoft.commons.util.Named):
    """
    public interface BlmCrateInfo extends cern.accsoft.commons.util.Named
    
        Represents info about a single BLM crate. All data in this bean is loaded from LSA database from table
        BLM_MASTER_COMBINER_INFO.
    """
    def getBlecfPresent(self) -> int:
        """
            Returns encoded information about presence of CF sub cards. On every BLM crate there might be up to 16 cards (TC), each
            with two sub cards (CF) which gives in total 32 CF sub cards. The most significant bit (MSB) in the returned value
            corresponds to the sub card A of the first card (nr 1). The least significant bit (LSB) in the returned value
            corresponds to the sub card B of the last card (nr 16).
        
            The verification whether the sub card is present or not is done based on BLM expert names i.e. whether the names start
            with 'BLMM.' prefix (spare BLMs). If all BLMs on a given sub card are spare - this means that the sub card is not
            present and the corresponding bit is set to 0. If there is at least one BLM which is not spare on a given sub card - the
            corresponding bit is set to 1.
        
            Returns:
                encoded BLECF presence flags which corresponds to the FESA field: BLMLHC:BLECSFlash:blecsFBLECFPRES
        
        
        """
        ...
    def getBlecsFirmwareVersion(self) -> int:
        """
        
            Returns:
        
        
        """
        ...
    def getBlecsSerial(self) -> int:
        """
            Serial number of the combiner board.
        
            Returns:
                serial number of the combiner board
        
        
        """
        ...
    def getBletcPresent(self) -> int:
        """
            Returns encoded information about presence of cards. On every BLM crate there might be up to 16 cards (TC). The most
            significant bit (MSB) in the returned value corresponds to the first card (nr 1). The bit with index MSB - 16 in the
            returned value corresponds to the last card (nr 16).
        
            The verification whether the card is present or not is done based on BLM expert names i.e. whether the names start with
            'BLMM.' prefix (spare BLMs). If all BLMs on a given card are spare - this means that the card is not present and the
            corresponding bit is set to 0. If there is at least one BLM which is not spare on a given card - the corresponding bit
            is set to 1.
        
            Returns:
                encoded BLETC presence flags which corresponds to the FESA field: BLMLHC:BLECSFlash:blecsFBLETCPRES
        
        
        """
        ...
    def getChannelCableConnected(self) -> typing.List[int]:
        """
            Returns and array of 8 integers which contain information about whether each channel is
            :meth:`~cern.lsa.domain.cern.devices.BlmInfo.isCableConnected`. Since there are 256 channels on each crate and one
            integer has 32 bits - we need 8 integers to encode these 256 flags. The most significant bit (MSB) of the first element
            of this array corresponds to the first channel on the first card (number 1). The least significant bit (LSB) of the last
            element of this array corresponds to the last channel of the last card (number 16). If the bit is set to 1 - the channel
            is cable connected, if it's 0 - it's not connected.
        
            If channel is cable connected - it means that there is physically connected monitor on the channel. This status is used
            in the connectivity check.
        
            This property is populated from IS_CABLE_CONNECTED column.
        
            Returns:
                encoded channel present flags which corresponds to FESA field: BLMLHC:BLECSFlash:blecsFCHPRES.
        
        
        """
        ...
    def getExpertNames(self) -> typing.List[typing.List[str]]:
        """
            Returns the 2 dimensional array [cardIndex-1][channelIndex-1] containing the expert names
        
            Returns:
        
        
        """
        ...
    def getHvcfcTestHv(self) -> int:
        """
            Settings for High Voltage of monitors (per IP).
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getHvcfcTestHvPeak(self) -> int:
        """
            Settings for High Voltage of monitors (per IP).
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getLastLSAModification(self) -> int: ...
    def getLhcInteractionPoint(self) -> cern.accsoft.commons.domain.lhc.LhcInteractionPoint:
        """
            Returns the LHC Interaction Point that this crate belongs to.
        
            Returns:
                the LHC Interaction Point of this BLM crate
        
        
        """
        ...
    def getMod1GainMax(self) -> typing.List[int]:
        """
            Thresholds for the connectivity check test.
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod1GainMin(self) -> typing.List[int]:
        """
            Thresholds for the connectivity check test.
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod1Period(self) -> int:
        """
            Returns modulation period for first frequency.
        
            Returns:
                modulation period for first frequency
        
        
        """
        ...
    def getMod1PhaseMax(self) -> typing.List[int]:
        """
            Thresholds for the connectivity check test.
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod1PhaseMin(self) -> typing.List[int]:
        """
            Thresholds for the connectivity check test.
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod1Voltage(self) -> int:
        """
            Returns modulation voltage for first frequency.
        
            Returns:
                modulation voltage for first frequency
        
        
        """
        ...
    def getMod2GainMax(self) -> typing.List[int]:
        """
            Thresholds for the connectivity check test.
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod2GainMin(self) -> typing.List[int]:
        """
            Thresholds for the connectivity check test.
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod2Period(self) -> int:
        """
            Returns modulation period for second frequency.
        
            Returns:
                modulation period for second frequency
        
        
        """
        ...
    def getMod2PhaseMax(self) -> typing.List[int]:
        """
            Thresholds for the connectivity check test.
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod2PhaseMin(self) -> typing.List[int]:
        """
            Thresholds for the connectivity check test.
        
            Returns:
                thresholds for the connectivity check test.
        
        
        """
        ...
    def getMod2Voltage(self) -> int:
        """
            Returns modulation voltage for second frequency.
        
            Returns:
                modulation voltage for second frequency
        
        
        """
        ...
    def getModTestHv(self) -> int:
        """
            Settings for High Voltage of monitors (per IP).
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getNormalOpHv(self) -> int:
        """
            Settings for High Voltage of monitors (per IP).
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getNormalOpHv1Hv2Diff(self) -> int:
        """
            Settings for High Voltage of monitors (per IP).
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getOfficialNames(self) -> typing.List[typing.List[str]]:
        """
            Returns the 2 dimensional array [cardIndex-1][channelIndex-1] containing the official names
        
            Returns:
        
        
        """
        ...
    def getRdacResetHv(self) -> int:
        """
            Settings for High Voltage of monitors (per IP).
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getRdacResetHvPeak(self) -> int:
        """
            Settings for High Voltage of monitors (per IP).
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getRgohResetHv(self) -> int:
        """
            Settings for High Voltage of monitors (per IP).
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...
    def getRgohResetHvPeak(self) -> int:
        """
            Settings for High Voltage of monitors (per IP).
        
            Returns:
                settings for High Voltage of monitors (per IP).
        
        
        """
        ...

class BlmFamily(cern.accsoft.commons.util.Named):
    """
    public interface BlmFamily extends cern.accsoft.commons.util.Named
    
        Represents one BLM Family object read from DB.
    """
    def getAmpsFactor(self) -> float:
        """
            Returns special conversion factor used to calculate Amps based on Greys. Defined per BLM Family.
        
            Returns:
                the ampsFactor
        
        
        """
        ...
    def getGysFactor(self) -> float:
        """
            Returns special conversion factor used to calculate Greys based on Blm bits. Defined per BLM Family.
        
            Returns:
                the gysFactor
        
        
        """
        ...
    def getThresholds(self) -> typing.List[int]:
        """
            Returns the thresholds Master Table for the family.
        
            Returns:
                an array representing a row-major matrix, indexed by the energy levels (rows) and the running sums (columns).
        
        
        """
        ...

class BlmInfo(cern.accsoft.commons.util.Named):
    """
    public interface BlmInfo extends cern.accsoft.commons.util.Named
    
        Represents one BLM Info object read from DB.
    """
    ALL_THRESHOLDS_INCLUDED: typing.ClassVar[typing.List[bool]] = ...
    """
    static final boolean[] ALL_THRESHOLDS_INCLUDED
    
    
    """
    NUM_CARDS: typing.ClassVar[int] = ...
    """
    static final int NUM_CARDS
    
        Total number of cards in one BLM crate - :code:`16`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    NUM_CHANNELS_PER_CARD: typing.ClassVar[int] = ...
    """
    static final int NUM_CHANNELS_PER_CARD
    
        Total number of channels per BLM card - :code:`16`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    NUM_ENERGY_LEVELS: typing.ClassVar[int] = ...
    """
    static final int NUM_ENERGY_LEVELS
    
        Number of energy levels - :code:`32`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    NUM_RUNNING_SUMS: typing.ClassVar[int] = ...
    """
    static final int NUM_RUNNING_SUMS
    
        Number of running sums - :code:`12`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    NUM_MAX_VALUES_PER_CARD: typing.ClassVar[int] = ...
    """
    static final int NUM_MAX_VALUES_PER_CARD
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getBlecfSerial(self) -> int:
        """
            Returns BLECF card serial number.
        
            Returns:
                BLECF card serial number.
        
        
        """
        ...
    def getBletcFirmwareVersion(self) -> int:
        """
            Returns the bletc firmware version.
        
            Returns:
                the bletc firmware version
        
        
        """
        ...
    def getBletcSerial(self) -> int:
        """
            Returns BLETC card serial number.
        
            Returns:
                BLETC card serial number.
        
        
        """
        ...
    def getBlmFamily(self) -> BlmFamily:
        """
            Returns BLM family that this BLM belongs to. The method can return :code:`null` in case the BLM doesn't belong to any
            family e.g. when this object represents a spare slot or a mobile BLM.
        
            Returns:
                blmFamily or :code:`null`
        
        
        """
        ...
    def getCardIndex(self) -> int:
        """
            Returns the crate card index.
        
            Returns:
                crate card index of this BLM.
        
        
        """
        ...
    def getChannelIndex(self) -> int:
        """
            Returns the crate card channel index.
        
            Returns:
                crate card channel index of this BLM.
        
        
        """
        ...
    def getCrateName(self) -> str:
        """
            Returns the name of the crate hosting the BLM.
        
            Returns:
                crate name hosting the BLM.
        
        
        """
        ...
    def getDcum(self) -> int:
        """
            Returns DCUM number for the BLM. It is a position of this BLM in the ring.
        
            Returns:
                dcum value for a BLM
        
        
        """
        ...
    def getFilterValueCapacitor(self) -> int:
        """
            Returns capacitor value of the filter in the input channel of the monitor.
        
        """
        ...
    def getFilterValueResistor(self) -> int:
        """
            Returns resistor value of the filter in the input channel of the monitor.
        
        """
        ...
    def getIncludedRunningSums(self) -> typing.List[bool]:
        """
            Returns an array of 12 boolean values denoting whether their corresponding acq/threshold values for a certain BLM are
            included in Logging process. Namely, n-th boolean value indicates whether n-th acquired/threshold BLM value is
            monitored.
        
            Returns:
                the includedThresholds
        
        
        """
        ...
    def getLastLSAModification(self) -> int:
        """
            Returns the moment (number of milliseconds since January 1, 1970, 00:00:00 GMT) of last modification of LSA database.
        
            Returns:
        
        
        """
        ...
    def getLhcInteractionPoint(self) -> cern.accsoft.commons.domain.lhc.LhcInteractionPoint:
        """
            Returns the LHC Interaction Point that this BLM is installed in.
        
            Returns:
                the LHC Interaction Point of this BLM
        
        
        """
        ...
    def getMobileName(self) -> str:
        """
            Returns name of a mobile monitor. If this :code:`BlmInfo` doesn't represent a mobile BLM - :code:`null` value is
            returned.
        
            Returns:
                name of a mobile monitor or :code:`null` if it's not mobile
        
            Also see:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.isSpare`
        
        
        """
        ...
    def getOfficialName(self) -> str:
        """
            Return BLM official name.
        
            Returns:
                the BLM official name.
        
        
        """
        ...
    def isCableConnected(self) -> bool:
        """
            If channel is cable connected - it means that there is physically connected monitor on the channel. This status is used
            in the connectivity check.
        
        """
        ...
    def isConnectedToBis(self) -> bool:
        """
            Returns :code:`true` if this BLM is connected to the Beam Interlock System, :code:`false` if it's not connected.
        
            Returns:
                :code:`true` if this BLM is connected to the BIS
        
        
        """
        ...
    def isMasked(self) -> bool:
        """
            Returns :code:`true` if this BLM is masked i.e. if this BLM sends signals to maskable BIS interface.
        
            Returns:
                :code:`true` if this BLM is masked
        
        
        """
        ...
    def isSpare(self) -> bool:
        """
            Specifies if this BlmInfo represents a spare slot in the crate (which can be used to install a mobile BLM). If the
            method returns :code:`true` - it doesn't mean that it represents a mobile BLM. To check this use
            :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getMobileName`
        
            Returns:
                :code:`true` if this :code:`BlmInfo` represents a spare slot in the crate (which can be used to install a mobile BLM).
        
            Also see:
                :meth:`~cern.lsa.domain.cern.devices.BlmInfo.getMobileName`
        
        
        """
        ...

class CollimatorAlignment(cern.lsa.domain.commons.IdentifiedEntity):
    """
    public interface CollimatorAlignment extends cern.lsa.domain.commons.IdentifiedEntity
    
        Represents a collimator alignment for a collimator and a beam mode category.
    """
    def getAlignmentTime(self) -> java.util.Date:
        """
        
            Returns:
                the time when the collimator was aligned
        
        
        """
        ...
    def getBeamModeCategory(self) -> str:
        """
            Returns the name of the collimator-related beam mode category (e.g. FLATTOP, INJECTION, PHYSICS, SQUEEZED)
        
            Returns:
                the name of the beam mode category
        
        
        """
        ...
    def getCollimatorName(self) -> str:
        """
        
            Returns:
                the associated collimator name
        
        
        """
        ...
    def getLeftJawPos(self) -> float: ...
    def getOpticName(self) -> str: ...
    def getRightJawPos(self) -> float: ...
    def getTcp1LeftPos(self) -> float: ...
    def getTcp1RightPos(self) -> float: ...
    def getTcp2LeftPos(self) -> float: ...
    def getTcp2RightPos(self) -> float: ...

class CollimatorRegion(java.lang.Enum['CollimatorRegion']):
    """
    public enum CollimatorRegion extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.devices.CollimatorRegion`>
    
        Enumeration for collimator regions: places where a collimator can be placed.
    """
    LHC_IP1: typing.ClassVar['CollimatorRegion'] = ...
    LHC_IP2: typing.ClassVar['CollimatorRegion'] = ...
    LHC_IP3: typing.ClassVar['CollimatorRegion'] = ...
    LHC_IP4: typing.ClassVar['CollimatorRegion'] = ...
    LHC_IP5: typing.ClassVar['CollimatorRegion'] = ...
    LHC_IP6: typing.ClassVar['CollimatorRegion'] = ...
    LHC_IP7: typing.ClassVar['CollimatorRegion'] = ...
    LHC_IP8: typing.ClassVar['CollimatorRegion'] = ...
    TI2: typing.ClassVar['CollimatorRegion'] = ...
    TI8: typing.ClassVar['CollimatorRegion'] = ...
    SPS: typing.ClassVar['CollimatorRegion'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CollimatorRegion':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['CollimatorRegion']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (CollimatorRegion c : CollimatorRegion.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class DeviceGroupTypeEnum(java.lang.Enum['DeviceGroupTypeEnum'], cern.lsa.domain.devices.DeviceGroupType):
    """
    public enum DeviceGroupTypeEnum extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.devices.DeviceGroupTypeEnum`> implements cern.lsa.domain.devices.DeviceGroupType
    
        Defines Device group types defined at CERN.
    """
    PROCESS: typing.ClassVar['DeviceGroupTypeEnum'] = ...
    WORKING_SET: typing.ClassVar['DeviceGroupTypeEnum'] = ...
    DEVICES: typing.ClassVar['DeviceGroupTypeEnum'] = ...
    SOC: typing.ClassVar['DeviceGroupTypeEnum'] = ...
    OP_CONFIG: typing.ClassVar['DeviceGroupTypeEnum'] = ...
    WORKING_SET_DEVICES: typing.ClassVar['DeviceGroupTypeEnum'] = ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :code:`getDescription` in interface :code:`cern.lsa.domain.devices.DeviceGroupType`
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'DeviceGroupTypeEnum':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['DeviceGroupTypeEnum']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (DeviceGroupTypeEnum c : DeviceGroupTypeEnum.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class LhcBeamLossMap:
    """
    public interface LhcBeamLossMap
    
        The beam loss map contains information about Beam Loss tests performed for different beam modes and for different
        configurations. These tests need to be performed periodically with different frequency for different configurations,
        varying from few weeks to few months. These tests consist on producing losses with certain characteristics and verifying
        that collimator positions are well configured to properly protect the beam.
    
        At the moment of creation of this class we have four types of configurations: BETATRON_HOR, BETATRON_VER,
        OFFMOMENTUM_NEG_DP and OFFMOMENTUM_POS_DP.
    
        The beam mode category is very similar to the :code:`BeamMode` however it is not as fine grained (INJECTION, FLATTOP,
        PHYSICS). To avoid name conflicts and confusions we called it here beam mode category rather than beam mode.
    
        The actual information kept in this object is the validity period for each triplet: beam (1 or 2), configuration type
        and beam mode category. The **validity period** is simply a start and end time stamp, where the start time represents
        the time when the test was performed and the end time is the expiration time i.e. the date when the test should be
        repeated.
    
        Information stored in this object is displayed on a fixed display so that operation crew can see when each test needs to
        be performed.
    
        For more information about beam loss maps please see with **Stefano Redaelli**.
    """
    def getAllEntries(self) -> java.util.List['LhcBeamLossMap.LhcBeamLossMapEntry']: ...
    def getEntry(self, lhcBeam: cern.accsoft.commons.domain.beams.LhcBeam, string: str, string2: str) -> 'LhcBeamLossMap.LhcBeamLossMapEntry':
        """
            Returns the beam loss map entry for the specified triplet.
        
            Parameters:
                beam (cern.accsoft.commons.domain.beams.LhcBeam): the beam identifier
                configType (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): configuration type name
                beamModeCategory (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the beam mode category
        
            Returns:
                the beam loss map entry for the specified triplet or :code:`null` if such entry does not exist i.e. there is no validity
                period defined for given triplet.
        
        
        """
        ...
    class LhcBeamLossMapEntry(java.io.Serializable):
        def getBeam(self) -> cern.accsoft.commons.domain.beams.LhcBeam: ...
        def getBeamModeCategory(self) -> str: ...
        def getConfigType(self) -> str: ...
        def getValidFrom(self) -> int: ...
        def getValidTo(self) -> int: ...

class LhcCollimatorInfo(cern.accsoft.commons.util.Named):
    """
    public interface LhcCollimatorInfo extends cern.accsoft.commons.util.Named
    """
    def getAngle(self) -> float:
        """
        
            Returns:
                the angle
        
        
        """
        ...
    def getAutoRetractionLeftDown(self) -> float:
        """
        
            Returns:
                the autoRetractionLeftDown
        
        
        """
        ...
    def getAutoRetractionLeftUp(self) -> float:
        """
        
            Returns:
                the autoRetractionLeftUp
        
        
        """
        ...
    def getAutoRetractionRightDown(self) -> float:
        """
        
            Returns:
                the autoRetractionRightDown
        
        
        """
        ...
    def getAutoRetractionRightUp(self) -> float:
        """
        
            Returns:
                the autoRetractionRightUp
        
        
        """
        ...
    def getAxisLeftDown(self) -> float:
        """
        
            Returns:
                the axisLeftDown
        
        
        """
        ...
    def getAxisLeftUp(self) -> float:
        """
        
            Returns:
                the axisLeftUp
        
        
        """
        ...
    def getAxisRightDown(self) -> float:
        """
        
            Returns:
                the axisRightDown
        
        
        """
        ...
    def getAxisRightUp(self) -> float:
        """
        
            Returns:
                the axisRightUp
        
        
        """
        ...
    def getAxisTank(self) -> float:
        """
        
            Returns:
                the axisTank
        
        
        """
        ...
    def getBeam(self) -> cern.accsoft.commons.domain.beams.LhcBeam: ...
    def getBlmi(self) -> str: ...
    def getBlmi2(self) -> str: ...
    def getBlms(self) -> str: ...
    def getBlms2(self) -> str: ...
    def getBpmBtnAttnCoeffLeftDown(self) -> float: ...
    def getBpmBtnAttnCoeffLeftUp(self) -> float: ...
    def getBpmBtnAttnCoeffRightDown(self) -> float: ...
    def getBpmBtnAttnCoeffRightUp(self) -> float: ...
    def getBpmBtnCapacitanceLeftDown(self) -> float: ...
    def getBpmBtnCapacitanceLeftUp(self) -> float: ...
    def getBpmBtnCapacitanceRightDown(self) -> float: ...
    def getBpmBtnCapacitanceRightUp(self) -> float: ...
    def getBpmBtnDiameterLeftDown(self) -> float: ...
    def getBpmBtnDiameterLeftUp(self) -> float: ...
    def getBpmBtnDiameterRightDown(self) -> float: ...
    def getBpmBtnDiameterRightUp(self) -> float: ...
    def getBpmBtnDistToJawLeftDown(self) -> float: ...
    def getBpmBtnDistToJawLeftUp(self) -> float: ...
    def getBpmBtnDistToJawRightDown(self) -> float: ...
    def getBpmBtnDistToJawRightUp(self) -> float: ...
    def getBpmBtnDistToSfcLeftDown(self) -> float: ...
    def getBpmBtnDistToSfcLeftUp(self) -> float: ...
    def getBpmBtnDistToSfcRightDown(self) -> float: ...
    def getBpmBtnDistToSfcRightUp(self) -> float: ...
    def getBpmChannelIdLeftDown(self) -> float: ...
    def getBpmChannelIdLeftUp(self) -> float: ...
    def getBpmChannelIdRightDown(self) -> float: ...
    def getBpmChannelIdRightUp(self) -> float: ...
    def getBpmFrontEndIdDown(self) -> float: ...
    def getBpmFrontEndIdUp(self) -> float: ...
    def getBpmNameDown(self) -> str: ...
    def getBpmNameE(self) -> str: ...
    def getBpmNameUp(self) -> str: ...
    def getCercaName(self) -> str: ...
    def getDisplayName(self) -> str: ...
    def getFamily(self) -> str: ...
    def getJawLeftDown(self) -> str: ...
    def getJawLeftUp(self) -> str: ...
    def getJawRightDown(self) -> str: ...
    def getJawRightUp(self) -> str: ...
    def getLastUpdate(self) -> java.util.Date: ...
    def getLength(self) -> float:
        """
        
            Returns:
                the length
        
        
        """
        ...
    def getMaterial(self) -> str: ...
    def getMaxFlatErrLeft(self) -> float:
        """
        
            Returns:
                the maxFlatErrLeft
        
        
        """
        ...
    def getMaxFlatErrRight(self) -> float:
        """
        
            Returns:
                the maxFlatErrRight
        
        
        """
        ...
    def getMaxTiltLeftMinus(self) -> float:
        """
        
            Returns:
                the maxTiltLeftMinus
        
        
        """
        ...
    def getMaxTiltLeftPlus(self) -> float:
        """
        
            Returns:
                the maxTiltLeftPlus
        
        
        """
        ...
    def getMaxTiltRightMinus(self) -> float:
        """
        
            Returns:
                the maxTiltRightMinus
        
        
        """
        ...
    def getMaxTiltRightPlus(self) -> float:
        """
        
            Returns:
                the maxTiltRightPlus
        
        
        """
        ...
    def getMechPlayLeftDown(self) -> float:
        """
        
            Returns:
                the mechPlayLeftDown
        
        
        """
        ...
    def getMechPlayLeftUp(self) -> float:
        """
        
            Returns:
                the mechPlayLeftUp
        
        
        """
        ...
    def getMechPlayRightDown(self) -> float:
        """
        
            Returns:
                the mechPlayRightDown
        
        
        """
        ...
    def getMechPlayRightUp(self) -> float:
        """
        
            Returns:
                the mechPlayRightUp
        
        
        """
        ...
    def getMtfName(self) -> str:
        """
        
            Returns:
                the mtfName
        
        
        """
        ...
    def getRegion(self) -> CollimatorRegion: ...
    def getScrewSerialNumberLeftDown(self) -> str: ...
    def getScrewSerialNumberLeftUp(self) -> str: ...
    def getScrewSerialNumberRightDown(self) -> str: ...
    def getScrewSerialNumberRightUp(self) -> str: ...
    def getStopAntiDown(self) -> float:
        """
        
            Returns:
                the stopAntiDown
        
        
        """
        ...
    def getStopAntiUp(self) -> float:
        """
        
            Returns:
                the stopAntiUp
        
        
        """
        ...
    def getStopLeftDownIn(self) -> float:
        """
        
            Returns:
                the stopLeftDownIn
        
        
        """
        ...
    def getStopLeftDownOut(self) -> float:
        """
        
            Returns:
                the stopLeftDownOut
        
        
        """
        ...
    def getStopLeftUpIn(self) -> float:
        """
        
            Returns:
                the stopLeftUpIn
        
        
        """
        ...
    def getStopLeftUpOut(self) -> float:
        """
        
            Returns:
                the stopLeftUpOut
        
        
        """
        ...
    def getStopRightDownIn(self) -> float:
        """
        
            Returns:
                the stopRightDownIn
        
        
        """
        ...
    def getStopRightDownOut(self) -> float:
        """
        
            Returns:
                the stopRightDownOut
        
        
        """
        ...
    def getStopRightUpIn(self) -> float:
        """
        
            Returns:
                the stopRightUpIn
        
        
        """
        ...
    def getStopRightUpOut(self) -> float:
        """
        
            Returns:
                the stopRightUpOut
        
        
        """
        ...
    def getSwitchAntiDown(self) -> float:
        """
        
            Returns:
                the switchAntiDown
        
        
        """
        ...
    def getSwitchAntiUp(self) -> float:
        """
        
            Returns:
                the switchAntiUp
        
        
        """
        ...
    def getSwitchLeftDownIn(self) -> float:
        """
        
            Returns:
                the switchLeftDownIn
        
        
        """
        ...
    def getSwitchLeftDownOut(self) -> float:
        """
        
            Returns:
                the switchLeftDownOut
        
        
        """
        ...
    def getSwitchLeftUpIn(self) -> float:
        """
        
            Returns:
                the switchLeftUpIn
        
        
        """
        ...
    def getSwitchLeftUpOut(self) -> float:
        """
        
            Returns:
                the switchLeftUpOut
        
        
        """
        ...
    def getSwitchRightDownIn(self) -> float:
        """
        
            Returns:
                the switchRightDownIn
        
        
        """
        ...
    def getSwitchRightDownOut(self) -> float:
        """
        
            Returns:
                the switchRightDownOut
        
        
        """
        ...
    def getSwitchRightUpIn(self) -> float:
        """
        
            Returns:
                the switchRightUpIn
        
        
        """
        ...
    def getSwitchRightUpOut(self) -> float:
        """
        
            Returns:
                the switchRightUpOut
        
        
        """
        ...
    def getTankCalibration(self) -> float:
        """
        
            Returns:
                tank calibration for fifth motor axis
        
        
        """
        ...
    def getTankPosSetPoint(self) -> float:
        """
        
            Returns:
                the tankPosSetPoint
        
        
        """
        ...
    def getTankPosStopDown(self) -> float:
        """
        
            Returns:
                the tankPosStopDown
        
        
        """
        ...
    def getTankPosStopUp(self) -> float:
        """
        
            Returns:
                the tankPosStopUp
        
        
        """
        ...
    def getTankPosSwitchDown(self) -> float:
        """
        
            Returns:
                the tankPosSwitchDown
        
        
        """
        ...
    def getTankPosSwitchUp(self) -> float:
        """
        
            Returns:
                the tankPosSwitchUp
        
        
        """
        ...
    def isBpmInstalled(self) -> bool: ...
    def isTankBpmInstalled(self) -> bool: ...

class RfFgcChannel:
    """
    public interface RfFgcChannel
    """
    def getChannelName(self) -> str:
        """
        
            Returns:
                the name of the channel
        
        
        """
        ...
    def getChannelNumber(self) -> int:
        """
        
            Returns:
                the channel number
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Returns:
                the description of the parameter associated with the channel
        
        
        """
        ...
    def getFGCName(self) -> str:
        """
        
            Returns:
                the name of the FGC the channel belongs to
        
        
        """
        ...
    def getMaxSlope(self) -> float:
        """
            return tne maximum slope to be used when doing a PLP or CTRIM on the function
        
            Returns:
        
        
        """
        ...
    def getMaxValue(self) -> float:
        """
        
            Returns:
                the max value of the parameter
        
        
        """
        ...
    def getMinValue(self) -> float:
        """
        
            Returns:
                the min value of the parameter
        
        
        """
        ...
    def getParameterName(self) -> str:
        """
        
            Returns:
                the name of the parameter associated with the channel
        
        
        """
        ...
    def getUnit(self) -> str:
        """
        
            Returns:
                the unit of the parameter associated with the channel
        
        
        """
        ...

class ThresholdsAwareBlmInfo(BlmInfo):
    """
    public interface ThresholdsAwareBlmInfo extends :class:`~cern.lsa.domain.cern.devices.BlmInfo`
    
        BlmInfo which contains additionally applied thresholds.
    """
    def getAppliedThresholds(self) -> typing.List[typing.List[int]]:
        """
            Returns applied table for this BLM from BLM_APPLIED_THRESHOLDS if loaded or :code:`null`. The first dimension specifies
            beam energy and the second - running sum.
        
            Returns:
                applied thresholds table
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.devices")``.

    BlmCrateInfo: typing.Type[BlmCrateInfo]
    BlmFamily: typing.Type[BlmFamily]
    BlmInfo: typing.Type[BlmInfo]
    CollimatorAlignment: typing.Type[CollimatorAlignment]
    CollimatorRegion: typing.Type[CollimatorRegion]
    DeviceGroupTypeEnum: typing.Type[DeviceGroupTypeEnum]
    LhcBeamLossMap: typing.Type[LhcBeamLossMap]
    LhcCollimatorInfo: typing.Type[LhcCollimatorInfo]
    RfFgcChannel: typing.Type[RfFgcChannel]
    ThresholdsAwareBlmInfo: typing.Type[ThresholdsAwareBlmInfo]
    spi: cern.lsa.domain.cern.devices.spi.__module_protocol__
