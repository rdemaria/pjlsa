import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.beams
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.domain.zones
import cern.lsa.domain.optics
import com.google.common.collect
import java.util
import typing



class ElementsRequestBuilder:
    """
    public class ElementsRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder to be used when creating instances of :class:`~cern.lsa.domain.optics.ElementsRequest` class that describe
        search criteria for device groups. The typical usage is following:
    
        .. code-block: java
        
         ElementsRequestBuilder builder = ElementsRequestBuilder.newInstance();
         // Set search criteria
         builder.setAcceleratorZone(SpsAcceleratorZone.SPS);
         // Create the request 
         ElementsRequest request = builder.build();
         //Call the ElementFinder or OpticService passing the request.  
         
    
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.optics.ElementsRequest:
        """
        
            Returns:
                instance of the :class:`~cern.lsa.domain.optics.ElementsRequest`
        
        
        """
        ...
    @staticmethod
    def byAcceleratorZone(acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.optics.ElementsRequest:
        """
        
            Parameters:
                acceleratorZone (cern.accsoft.commons.domain.zones.AcceleratorZone): accelerator zone
        
            Returns:
                elements request for specified accelerator zone
        
        
        """
        ...
    @staticmethod
    def byElementNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.optics.ElementsRequest: ...
    @staticmethod
    def byLogicalHwName(string: str) -> cern.lsa.domain.optics.ElementsRequest:
        """
        
            Parameters:
                logicalHwName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): logical HW name
        
            Returns:
                elements request for specified logical HW names
        
        
        """
        ...
    @staticmethod
    def byLogicalHwNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.optics.ElementsRequest: ...
    @staticmethod
    def byParticleTransfer(particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> cern.lsa.domain.optics.ElementsRequest:
        """
        
            Parameters:
                particleTransfer (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): particle transfer
        
            Returns:
                elements request for specified accelerator zone
        
        
        """
        ...
    @staticmethod
    def byTypes(collection: typing.Union[java.util.Collection[cern.lsa.domain.optics.ElementType], typing.Sequence[cern.lsa.domain.optics.ElementType]]) -> cern.lsa.domain.optics.ElementsRequest: ...
    def excludeObsolete(self) -> 'ElementsRequestBuilder':
        """
            Exclude obsolete elements from the request
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.optics.ElementsRequest.excludeObsolete`
        
        
        """
        ...
    def setAcceleratorZone(self, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> 'ElementsRequestBuilder':
        """
        
            Parameters:
                acceleratorZone (cern.accsoft.commons.domain.zones.AcceleratorZone): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.optics.ElementsRequest.getAcceleratorZone`
        
        
        """
        ...
    def setElementNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'ElementsRequestBuilder': ...
    def setLogicalHwNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'ElementsRequestBuilder': ...
    def setParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'ElementsRequestBuilder':
        """
        
            Parameters:
                particleTransfer (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.optics.ElementsRequest.getParticleTransfer`
        
        
        """
        ...
    def setSteering(self) -> 'ElementsRequestBuilder':
        """
            Requests steering elements. Steering elements are monitors and correctors including
            :meth:`~cern.lsa.domain.optics.ElementType.MONITOR`, :meth:`~cern.lsa.domain.optics.ElementType.HMONITOR`,
            :meth:`~cern.lsa.domain.optics.ElementType.VMONITOR`, :meth:`~cern.lsa.domain.optics.ElementType.KICKER`,
            :meth:`~cern.lsa.domain.optics.ElementType.HKICKER`, :meth:`~cern.lsa.domain.optics.ElementType.VKICKER`,
            :meth:`~cern.lsa.domain.optics.ElementType.RBEND`, :meth:`~cern.lsa.domain.optics.ElementType.SBEND` that have a
            steering plane defined.
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.optics.ElementsRequest.getSteering`
        
        
        """
        ...
    def setTypes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.optics.ElementType], typing.Sequence[cern.lsa.domain.optics.ElementType]]) -> 'ElementsRequestBuilder': ...

class MeasuredTwissBuilder:
    """
    public class MeasuredTwissBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder for :class:`~cern.lsa.domain.optics.MeasuredTwiss` objects.
    
        Usage example:
    
        .. code-block: java
        
                MeasuredTwiss persistedMeasuredTwiss = new MeasuredTwissBuilder(twiss, 10.0, measTime) //
                        .setAlfxMeas(11).setAlfxError(12).setAlfyMeas(13).setAlfyError(14) //
                        .setBetxMeas(15).setBetxError(16).setBetyMeas(17).setBetyError(18) //
                        .setDxMeas(19).setDxError(20).setDyMeas(21).setDyError(22) //
                        // Missing the MuY on purpose. They will become NaNs
                        .build();
    """
    def __init__(self, twiss: cern.lsa.domain.optics.Twiss, double: float, date: java.util.Date): ...
    def build(self) -> cern.lsa.domain.optics.MeasuredTwiss: ...
    def setAlfxError(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setAlfxMeas(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setAlfyError(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setAlfyMeas(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setBetxError(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setBetxMeas(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setBetyError(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setBetyMeas(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setDxError(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setDxMeas(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setDyError(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setDyMeas(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setMuxError(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setMuxMeas(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setMuyError(self, double: float) -> 'MeasuredTwissBuilder': ...
    def setMuyMeas(self, double: float) -> 'MeasuredTwissBuilder': ...

class OpticsRequestBuilder:
    """
    public class OpticsRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder to be used when creating instances of :class:`~cern.lsa.domain.optics.OpticsRequest` class that describe search
        criteria for optics. The typical usage is following:
    
        .. code-block: java
        
         OpticsRequestBuilder builder = OpticsRequestBuilder.newInstance();
         // Set search criteria
         builder.setAccelerator(CernAccelerator.PS);
         // Create the request 
         OpticsRequest request = builder.build();
         // Call the OpticsFinder or OpticService passing the request.  
         
    
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.optics.OpticsRequest:
        """
        
            Returns:
                instance of the :class:`~cern.lsa.domain.optics.OpticsRequest`
        
        
        """
        ...
    @staticmethod
    def byAccelerator(accelerator: cern.accsoft.commons.domain.Accelerator) -> cern.lsa.domain.optics.OpticsRequest:
        """
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): 
            Returns:
                optics request for specified accelerator
        
        
        """
        ...
    @staticmethod
    def byBeamProcessTypeNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.optics.OpticsRequest: ...
    @staticmethod
    def byOpticIds(collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> cern.lsa.domain.optics.OpticsRequest: ...
    @staticmethod
    def byParticleTransfer(particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> cern.lsa.domain.optics.OpticsRequest:
        """
        
            Parameters:
                particleTransfer (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): 
            Returns:
                optics request for specified particle transfer
        
        
        """
        ...
    def setAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'OpticsRequestBuilder':
        """
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.optics.OpticsRequest.getAccelerator`
        
        
        """
        ...
    def setBeamProcessTypeNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'OpticsRequestBuilder': ...
    def setOpticIds(self, collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> 'OpticsRequestBuilder': ...
    def setParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'OpticsRequestBuilder':
        """
        
            Parameters:
                particleTransfer (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.optics.OpticsRequest.getAccelerator`
        
        
        """
        ...

class TwissesRequestBuilder:
    """
    public class TwissesRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder to be used when creating instances of :class:`~cern.lsa.domain.optics.TwissesRequest` class that describe search
        criteria for twisses. The typical usage is following:
    
        .. code-block: java
        
         TwissesRequestBuilder builder = TwissesRequestBuilder.newInstance();
         // Set search criteria
         builder.setOpticName(opticName);
         // Create the request
         TwissesRequest request = builder.build();
         // Call the TwissFinder or OpticService passing the request.
         
    
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.optics.TwissesRequest:
        """
        
            Returns:
                instance of the :class:`~cern.lsa.domain.optics.TwissesRequest`
        
        
        """
        ...
    @staticmethod
    def byOpticName(string: str) -> cern.lsa.domain.optics.TwissesRequest:
        """
        
            Parameters:
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                twisses request for specified optic name
        
        
        """
        ...
    def setBeam(self, beam: cern.accsoft.commons.domain.beams.Beam) -> 'TwissesRequestBuilder':
        """
        
            Parameters:
                beam (cern.accsoft.commons.domain.beams.Beam): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.optics.TwissesRequest.getBeam`
        
        
        """
        ...
    def setElementNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'TwissesRequestBuilder': ...
    @typing.overload
    def setElementPositionRange(self, range: com.google.common.collect.Range[float]) -> 'TwissesRequestBuilder':
        """
        
            Parameters:
                minPosition (double):         maxPosition (double): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.optics.TwissesRequest.getElementPositionRange`
        
        public :class:`~cern.lsa.domain.optics.factory.TwissesRequestBuilder` setElementPositionRange (com.google.common.collect.Range<`Double <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Double.html?is-external=true>`> elementPositionRange)
        
        
            Parameters:
                elementPositionRange (com.google.common.collect.Range<`Double <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Double.html?is-external=true>`> elementPositionRange): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.optics.TwissesRequest.getElementPositionRange`
        
        
        """
        ...
    @typing.overload
    def setElementPositionRange(self, double: float, double2: float) -> 'TwissesRequestBuilder': ...
    def setElementTypes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.optics.ElementType], typing.Sequence[cern.lsa.domain.optics.ElementType]]) -> 'TwissesRequestBuilder': ...
    def setOpticName(self, string: str) -> 'TwissesRequestBuilder':
        """
        
            Parameters:
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.optics.TwissesRequest.getOpticName`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.optics.factory")``.

    ElementsRequestBuilder: typing.Type[ElementsRequestBuilder]
    MeasuredTwissBuilder: typing.Type[MeasuredTwissBuilder]
    OpticsRequestBuilder: typing.Type[OpticsRequestBuilder]
    TwissesRequestBuilder: typing.Type[TwissesRequestBuilder]
