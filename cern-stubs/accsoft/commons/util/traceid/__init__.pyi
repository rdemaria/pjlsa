import cern.accsoft.commons.util.executor
import java.nio.charset
import java.util
import typing



class TraceIdContextForwarder(cern.accsoft.commons.util.executor.ContextForwarder):
    """
    public class TraceIdContextForwarder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.executor.ContextForwarder`
    
        Forwards the traceId, which is a UUID represented as a String and stored on the :code:`MDC`.
    """
    def __init__(self): ...
    def clearContext(self) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.executor.ContextForwarder.clearContext`
            Clears the context after the end of execution.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.executor.ContextForwarder.clearContext`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.executor.ContextForwarder`
        
        
        """
        ...
    def setContext(self) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.executor.ContextForwarder.setContext`
            Sets the context from the calling thread.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.executor.ContextForwarder.setContext`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.executor.ContextForwarder`
        
        
        """
        ...

class TraceIds:
    """
    public class TraceIds extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class to handle traceIds
    """
    TRACE_ID: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TRACE_ID
    
        Key under which the traceId is stored in the :code:`MDC`
    
        Also see:
            :meth:`~constant`
    
    
    """
    TRACE_ID_CONTEXT_DEFINITION: typing.ClassVar[cern.accsoft.commons.util.executor.ContextDefinition] = ...
    """
    public static final :class:`~cern.accsoft.commons.util.executor.ContextDefinition` TRACE_ID_CONTEXT_DEFINITION
    
    
    """
    TRACE_ID_EXECUTORS: typing.ClassVar[cern.accsoft.commons.util.executor.ContextAwareExecutors] = ...
    """
    public static final :class:`~cern.accsoft.commons.util.executor.ContextAwareExecutors` TRACE_ID_EXECUTORS
    
    
    """
    def __init__(self): ...
    @staticmethod
    def clearTraceId() -> None:
        """
            Removes the traceId stored in the :code:`MDC`
        
        """
        ...
    @staticmethod
    def generateUniqueId() -> str:
        """
            Generates a new time-based UUID (version 1).
        
            Returns:
                the generated UUID
        
        
        """
        ...
    @staticmethod
    def getTraceId() -> str:
        """
        
            Returns:
                The traceId stored in the :code:`MDC` (can be null)
        
        
        """
        ...
    @staticmethod
    def setNewTraceId() -> str:
        """
            Sets a new traceId on the :code:`MDC` It can be used in the logger configuration to add the traceId in the logs, for
            example in log4j with the pattern %X{traceId}
        
            Returns:
                the new traceId
        
        
        """
        ...
    @staticmethod
    def setNewTraceIdIfMissing() -> str:
        """
            Sets a new traceId on the :code:`MDC` if none is currently set.
        
            Returns:
                the new traceId or existing one
        
        
        """
        ...
    @staticmethod
    def setTraceId(string: str) -> None:
        """
            Sets the given traceId on the :code:`MDC` if it is not null. If it is null, the call is ignored.
        
            Parameters:
                traceId (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the traceId to set
        
        
        """
        ...

class UUIDs:
    """
    public final class UUIDs extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility methods to work with UUID and most specifically with time-based ones (version 1).
    """
    UTF_8: typing.ClassVar[java.nio.charset.Charset] = ...
    """
    public static final `Charset <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/nio/charset/Charset.html?is-external=true>` UTF_8
    
    
    """
    @staticmethod
    def endOf(long: int) -> java.util.UUID:
        """
            Creates a "fake" time-based UUID that sorts as the biggest possible version 1 UUID generated at the provided timestamp.
        
            Such created UUID are useful in queries to select a time range of a :code:`timeuuid` column.
        
            The UUID created by this method **are not unique** and as such are **not** suitable for anything else than querying a
            specific time range. In particular, you should not insert such UUID.
        
            Also, the timestamp to provide as parameter must be a unix timestamp (as returned by `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/System.html?is-external=true#currentTimeMillis()>` or
            `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true#getTime()>`), not a UUID
            100-nanoseconds intervals since 15 October 1582. In other words, given a UUID :code:`uuid`, you should never do
            :code:`startOf(uuid.timestamp())` but rather :code:`startOf(unixTimestamp(uuid.timestamp()))`.
        
            Lastly, please note that Cassandra's timeuuid sorting is not compatible with `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/UUID.html?is-external=true#compareTo(java.util.UUID)>` and
            hence the UUID created by this method are not necessarily upper bound for that latter method.
        
            Parameters:
                timestamp (long): the unix timestamp for which the created UUID must be an upper bound.
        
            Returns:
                the biggest (for Cassandra timeuuid sorting) UUID of :code:`timestamp`.
        
        
        """
        ...
    @staticmethod
    def random() -> java.util.UUID:
        """
            Creates a new random (version 4) UUID.
        
            This method is just a convenience for :code:`UUID.randomUUID()`.
        
            Returns:
                a newly generated, pseudo random, version 4 UUID.
        
        
        """
        ...
    @staticmethod
    def startOf(long: int) -> java.util.UUID:
        """
            Creates a "fake" time-based UUID that sorts as the smallest possible version 1 UUID generated at the provided timestamp.
        
            Such created UUID are useful in queries to select a time range of a :code:`timeuuid` column.
        
            The UUID created by this method **are not unique** and as such are **not** suitable for anything else than querying a
            specific time range. In particular, you should not insert such UUID.
        
            Also, the timestamp to provide as parameter must be a unix timestamp (as returned by `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/System.html?is-external=true#currentTimeMillis()>` or
            `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true#getTime()>`), not a UUID
            100-nanoseconds intervals since 15 October 1582. In other words, given a UUID :code:`uuid`, you should never do
            :code:`startOf(uuid.timestamp())` but rather :code:`startOf(unixTimestamp(uuid.timestamp()))`.
        
            Lastly, please note that Cassandra's timeuuid sorting is not compatible with `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/UUID.html?is-external=true#compareTo(java.util.UUID)>` and
            hence the UUID created by this method are not necessarily lower bound for that latter method.
        
            Parameters:
                timestamp (long): the unix timestamp for which the created UUID must be a lower bound.
        
            Returns:
                the smallest (for Cassandra timeuuid sorting) UUID of :code:`timestamp`.
        
        
        """
        ...
    @staticmethod
    def timeBased() -> java.util.UUID:
        """
            Creates a new time-based (version 1) UUID.
        
            UUID generated by this method are suitable for use with the :code:`timeuuid` Cassandra type. In particular the generated
            UUID includes the timestamp of its generation.
        
            Returns:
                a new time-based UUID.
        
        
        """
        ...
    @staticmethod
    def unixTimestamp(uUID: java.util.UUID) -> int:
        """
            Return the unix timestamp contained by the provided time-based UUID.
        
            This method is not equivalent to :code:`uuid.timestamp()`. More precisely, a version 1 UUID stores a timestamp that
            represents the number of 100-nanoseconds intervals since midnight, 15 October 1582 and that is what
            :code:`uuid.timestamp()` returns. This method however converts that timestamp to the equivalent unix timestamp in
            milliseconds, i.e. a timestamp representing a number of milliseconds since midnight, January 1, 1970 UTC. In particular
            the timestamps returned by this method are comparable to the timestamp returned by `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/System.html?is-external=true#currentTimeMillis()>`, `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true#getTime()>`, etc.
        
            Parameters:
                uuid (`UUID <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/UUID.html?is-external=true>`): the UUID to return the timestamp of.
        
            Returns:
                the unix timestamp of :code:`uuid`.
        
            Raises:
                : if :code:`uuid` is not a version 1 UUID.
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.traceid")``.

    TraceIdContextForwarder: typing.Type[TraceIdContextForwarder]
    TraceIds: typing.Type[TraceIds]
    UUIDs: typing.Type[UUIDs]
