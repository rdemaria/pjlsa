import _jpype
import cern
import cern.accsoft.commons.util.annotation
import cern.accsoft.commons.util.collections
import cern.accsoft.commons.util.concurrent
import cern.accsoft.commons.util.enums
import cern.accsoft.commons.util.event
import cern.accsoft.commons.util.executor
import cern.accsoft.commons.util.format
import cern.accsoft.commons.util.jmx
import cern.accsoft.commons.util.mail
import cern.accsoft.commons.util.marker
import cern.accsoft.commons.util.metric
import cern.accsoft.commons.util.proc
import cern.accsoft.commons.util.rba
import cern.accsoft.commons.util.reflect
import cern.accsoft.commons.util.regexp
import cern.accsoft.commons.util.remoting
import cern.accsoft.commons.util.traceid
import cern.accsoft.commons.util.trigger
import cern.accsoft.commons.util.userctx
import cern.accsoft.commons.util.userinfo
import cern.accsoft.commons.util.value
import cern.accsoft.commons.util.xml
import java.awt
import java.beans
import java.io
import java.lang
import java.lang.reflect
import java.net
import java.nio.file
import java.text
import java.util
import java.util.stream
import jpype.protocol
import typing



class AppLauncher:
    @staticmethod
    def launch(stringArray: typing.List[str]) -> None: ...

class ArrayUtils:
    """
    public abstract class ArrayUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class with methods to manipulate arrays.
    """
    def __init__(self): ...
    @staticmethod
    def addObjectToArray(objectArray: typing.List[typing.Any], object2: typing.Any) -> typing.List[typing.Any]:
        """
            Append the given Object to the given array, returning a new array consisting of the input array contents plus the given
            Object.
        
            Parameters:
                array (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`[]): the array to append to (can be :code:`null`)
                obj (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the Object to append
        
            Returns:
                the new array (of the same component type; never :code:`null`)
        
        
        """
        ...
    _concatenateArrays__T = typing.TypeVar('_concatenateArrays__T')  # <T>
    @staticmethod
    def concatenateArrays(tArray: typing.List[_concatenateArrays__T], tArray2: typing.List[_concatenateArrays__T]) -> typing.List[_concatenateArrays__T]:
        """
            Concatenates two arrays.
        
            Parameters:
                first (T[]): first array (should not be :code:`null`)
                second (T[]): second array (should not be :code:`null`)
        
            Returns:
                the result array
        
        
        """
        ...
    @staticmethod
    def isEmpty(objectArray: typing.List[typing.Any]) -> bool:
        """
            Return whether the given array is empty: that is, :code:`null` or of zero length.
        
            Parameters:
                array (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`[]): the array to check
        
            Returns:
                whether the given array is empty
        
        
        """
        ...
    _toArray__T = typing.TypeVar('_toArray__T')  # <T>
    @staticmethod
    def toArray(collection: typing.Union[java.util.Collection[_toArray__T], typing.Sequence[_toArray__T]], class_: typing.Type[_toArray__T]) -> typing.List[_toArray__T]: ...
    @staticmethod
    def toDoubleArray(collection: typing.Union[java.util.Collection[float], typing.Sequence[float]]) -> typing.List[float]: ...
    @staticmethod
    def toFloatArray(collection: typing.Union[java.util.Collection[float], typing.Sequence[float]]) -> typing.List[float]: ...
    @staticmethod
    def toLongArray(collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> typing.List[int]: ...
    @staticmethod
    def toObjectArray(object: typing.Any) -> typing.List[typing.Any]:
        """
            Convert the given array (which may be a primitive array) to an object array (if necessary of primitive wrapper objects).
        
            A :code:`null` source value will be converted to an empty Object array.
        
            Parameters:
                source (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the (potentially primitive) array
        
            Returns:
                the corresponding object array (never :code:`null`)
        
            Raises:
                : if the parameter is not an array
        
        
        """
        ...
    @staticmethod
    def toStringArray(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> typing.List[str]: ...

class Assert:
    """
    public abstract class Assert extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Assertion utility class that assists in validating arguments. Useful for identifying programmer errors early and clearly
        at runtime.
    
        For example, if the contract of a public method states it does not allow :code:`null` arguments, Assert can be used to
        validate that contract. Doing this clearly indicates a contract violation when it occurs and protects the class's
        invariants.
    
        Typically used to validate method arguments rather than configuration properties, to check for cases that are usually
        programmer errors rather than configuration errors. In contrast to config initialization code, there is usally no point
        in falling back to defaults in such methods.
    
        This class is similar to JUnit's assertion library. If an argument value is deemed invalid, an `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` is thrown
        (typically). For example:
    
        .. code-block: java
        
         Assert.notNull(clazz, "The class must not be null");
         Assert.isTrue(i > 0, "The value must be greater than zero");
        Mainly for internal use within the framework; consider Jakarta's Commons Lang >= 2.0 for a more comprehensive suite of
        assertion utilities.
    
        Since:
            1.1.2
    """
    def __init__(self): ...
    @staticmethod
    def argHasText(string: str, string2: str) -> None:
        """
            Calls :meth:`~cern.accsoft.commons.util.Assert.hasText` passing the following error message: :code:`"The '" + argName +
            "' is required; it must not be null, empty or blank"`
        
            Parameters:
                text (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the string to check
                argName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the argument to be used in the message string
        
        
        """
        ...
    @staticmethod
    def argIsNumber(double: float, string: str) -> None:
        """
            Asserts a provided number is a finite number.
        
            Parameters:
                number (double):         argName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Raises:
                : if the provided argument is not a finite number
        
        
        """
        ...
    @staticmethod
    def argNotNull(object: typing.Any, string: str) -> None:
        """
            Calls :code:`#notNull(String, String)` passing the following error message: :code:`"The '" + argName + "' is required;
            it must not be null"`
        
            Parameters:
                object (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the object to check
                argName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the argument to be used in the message string
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def doesNotContain(string: str, string2: str) -> None:
        """
            Assert that the given text does not contain the given substring. :code:`Assert.doesNotContain(name, "rod");`
        
            Parameters:
                textToSearch (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the text to search
                substring (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the substring to find within the text
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def doesNotContain(string: str, string2: str, string3: str) -> None:
        """
            Assert that the given text does not contain the given substring. :code:`Assert.doesNotContain(name, "rod", "Name must
            not contain 'rod'");`
        
            Parameters:
                textToSearch (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the text to search
                substring (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the substring to find within the text
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the exception message to use if the assertion fails
        
        """
        ...
    @typing.overload
    @staticmethod
    def hasLength(string: str) -> None:
        """
            Assert that a string is not empty; that is, it must not be :code:`null` and not empty. :code:`Assert.hasLength(name);`
        
            Parameters:
                text (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the string to check
        
            Also see:
                :meth:`~cern.accsoft.commons.util.StringUtils.hasLength`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def hasLength(string: str, string2: str) -> None:
        """
            Assert that a string is not empty; that is, it must not be :code:`null` and not empty. :code:`Assert.hasLength(name,
            "Name must not be empty");`
        
            Parameters:
                text (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the string to check
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the exception message to use if the assertion fails
        
            Also see:
                :meth:`~cern.accsoft.commons.util.StringUtils.hasLength`
        
        """
        ...
    @typing.overload
    @staticmethod
    def hasText(string: str) -> None:
        """
            Assert that a string has valid text content; that is, it must not be :code:`null` and must contain at least one
            non-whitespace character. :code:`Assert.hasText(name, "'name' must not be empty");`
        
            Parameters:
                text (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the string to check
        
            Also see:
                :meth:`~cern.accsoft.commons.util.StringUtils.hasText`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def hasText(string: str, string2: str) -> None:
        """
            Assert that a string has valid text content; that is, it must not be :code:`null` and must contain at least one
            non-whitespace character. :code:`Assert.hasText(name, "'name' must not be empty");`
        
            Parameters:
                text (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the string to check
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the exception message to use if the assertion fails
        
            Also see:
                :meth:`~cern.accsoft.commons.util.StringUtils.hasText`
        
        """
        ...
    @typing.overload
    @staticmethod
    def isAssignable(class_: typing.Type, class2: typing.Type) -> None:
        """
            Assert that :code:`superType.isAssignableFrom(subType)` is :code:`true`. :code:`Assert.isAssignable(Number.class,
            myClass);`
        
            Parameters:
                superType (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the super type to check
                subType (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the sub type to check
        
            Raises:
                : if the classes are not assignable
        
        """
        ...
    @typing.overload
    @staticmethod
    def isAssignable(class_: typing.Type, class2: typing.Type, string: str) -> None:
        """
            Assert that :code:`superType.isAssignableFrom(subType)` is :code:`true`. :code:`Assert.isAssignable(Number.class,
            myClass);`
        
            Parameters:
                superType (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the super type to check against
                subType (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the sub type to check
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a message which will be prepended to the message produced by the function itself, and which may be used to provide
                    context. It should normally end in a ": " or ". " so that the function generate message looks ok when prepended to it.
        
            Raises:
                : if the classes are not assignable
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isInstanceOf(class_: typing.Type, object: typing.Any) -> None:
        """
            Assert that the provided object is an instance of the provided class. :code:`Assert.instanceOf(Foo.class, foo);`
        
            Parameters:
                clazz (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the required class
                obj (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the object to check
        
            Raises:
                : if the object is not an instance of clazz
        
            Also see:
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true#isInstance(java.lang.Object)>`
        
        """
        ...
    @typing.overload
    @staticmethod
    def isInstanceOf(class_: typing.Type, object: typing.Any, string: str) -> None:
        """
            Assert that the provided object is an instance of the provided class. :code:`Assert.instanceOf(Foo.class, foo);`
        
            Parameters:
                type (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the type to check against
                obj (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the object to check
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a message which will be prepended to the message produced by the function itself, and which may be used to provide
                    context. It should normally end in a ": " or ". " so that the function generate message looks ok when prepended to it.
        
            Raises:
                : if the object is not an instance of clazz
        
            Also see:
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true#isInstance(java.lang.Object)>`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isNull(object: typing.Any) -> None:
        """
            Assert that an object is :code:`null` . :code:`Assert.isNull(value);`
        
            Parameters:
                object (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the object to check
        
            Raises:
                : if the object is not :code:`null`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isNull(object: typing.Any, string: str) -> None:
        """
            Assert that an object is :code:`null` . :code:`Assert.isNull(value, "The value must be null");`
        
            Parameters:
                object (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the object to check
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the exception message to use if the assertion fails
        
            Raises:
                : if the object is not :code:`null`
        
        """
        ...
    @staticmethod
    def isNumber(double: float, string: str) -> None:
        """
            Asserts a provided number is a finite number.
        
            Parameters:
                number (double):         message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Raises:
                : if the provided argument is not a finite number
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isTrue(boolean: bool) -> None:
        """
            Assert a boolean expression, throwing :code:`IllegalArgumentException` if the test result is :code:`false`.
            :code:`Assert.isTrue(i > 0, "The value must be greater than zero");`
        
            Parameters:
                expression (boolean): a boolean expression
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the exception message to use if the assertion fails
        
            Raises:
                : if expression is :code:`false`
        
            Assert a boolean expression, throwing :code:`IllegalArgumentException` if the test result is :code:`false`.
            :code:`Assert.isTrue(i > 0);`
        
            Parameters:
                expression (boolean): a boolean expression
        
            Raises:
                : if expression is :code:`false`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isTrue(boolean: bool, string: str) -> None: ...
    @typing.overload
    @staticmethod
    def notEmpty(objectArray: typing.List[typing.Any]) -> None:
        """
            Assert that an array has elements; that is, it must not be :code:`null` and must have at least one element.
            :code:`Assert.notEmpty(array);`
        
            Parameters:
                array (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`[]): the array to check
        
            Raises:
                : if the object array is :code:`null` or has no elements
        
            Assert that a collection has elements; that is, it must not be :code:`null` and must have at least one element.
            :code:`Assert.notEmpty(collection, "Collection must have elements");`
        
            Parameters:
                collection (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`): the collection to check
        
            Raises:
                : if the collection is :code:`null` or has no elements
        
            Assert that a Map has entries; that is, it must not be :code:`null` and must have at least one entry.
            :code:`Assert.notEmpty(map);`
        
            Parameters:
                map (`Map <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Map.html?is-external=true>`): the map to check
        
            Raises:
                : if the map is :code:`null` or has no entries
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def notEmpty(objectArray: typing.List[typing.Any], string: str) -> None:
        """
            Assert that an array has elements; that is, it must not be :code:`null` and must have at least one element.
        
            .. code-block: java
            
             Assert.notEmpty(array, "The array must have elements");
             
        
            Parameters:
                array (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`[]): the array to check
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the exception message to use if the assertion fails
        
            Raises:
                : if the object array is :code:`null` or has no elements
        
            Assert that a collection has elements; that is, it must not be :code:`null` and must have at least one element.
            :code:`Assert.notEmpty(collection, "Collection must have elements");`
        
            Parameters:
                collection (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`): the collection to check
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the exception message to use if the assertion fails
        
            Raises:
                : if the collection is :code:`null` or has no elements
        
            Assert that a Map has entries; that is, it must not be :code:`null` and must have at least one entry.
            :code:`Assert.notEmpty(map, "Map must have entries");`
        
            Parameters:
                map (`Map <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Map.html?is-external=true>`): the map to check
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the exception message to use if the assertion fails
        
            Raises:
                : if the map is :code:`null` or has no entries
        
        """
        ...
    @typing.overload
    @staticmethod
    def notEmpty(collection: typing.Union[java.util.Collection, typing.Sequence]) -> None: ...
    @typing.overload
    @staticmethod
    def notEmpty(collection: typing.Union[java.util.Collection, typing.Sequence], string: str) -> None: ...
    @typing.overload
    @staticmethod
    def notEmpty(map: typing.Union[java.util.Map, typing.Mapping]) -> None: ...
    @typing.overload
    @staticmethod
    def notEmpty(map: typing.Union[java.util.Map, typing.Mapping], string: str) -> None: ...
    @typing.overload
    @staticmethod
    def notNull(object: typing.Any) -> None:
        """
            Assert that an object is not :code:`null` . :code:`Assert.notNull(clazz);`
        
            Parameters:
                object (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the object to check
        
            Raises:
                : if the object is :code:`null`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def notNull(object: typing.Any, string: str) -> None:
        """
            Assert that an object is not :code:`null` . :code:`Assert.notNull(clazz, "The class must not be null");`
        
            Parameters:
                object (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the object to check
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the exception message to use if the assertion fails
        
            Raises:
                : if the object is :code:`null`
        
        """
        ...
    @typing.overload
    @staticmethod
    def notNullElements(objectArray: typing.List[typing.Any]) -> None:
        """
            Assert that an array is not :code:`null` and if it has elements, none of them is :code:`null`.
        
        
            If the array is empty - assertion passes.
        
            Parameters:
                array (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`[]): the array to check
        
            Also see:
                :meth:`~cern.accsoft.commons.util.Assert.notEmpty`
        
        """
        ...
    @typing.overload
    @staticmethod
    def notNullElements(objectArray: typing.List[typing.Any], string: str) -> None:
        """
            Assert that an array is not :code:`null` and if it has elements, none of them is :code:`null`.
        
        
            If the array is empty - assertion passes.
        
            Parameters:
                array (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`[]): the array to check
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the exception message to use if the assertion fails
        
            Also see:
                :meth:`~cern.accsoft.commons.util.Assert.notEmpty`
        
        public static void notNullElements (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<?> collection, `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` message)
        
            Assert that a collection is not :code:`null` and if it has elements, none of them is :code:`null`.
        
        
            If the collection is empty - assertion passes.
        
            Parameters:
                collection (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<?> collection): the collection to check
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the exception message to use if the assertion fails
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def notNullElements(collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]], string: str) -> None: ...
    @typing.overload
    @staticmethod
    def state(boolean: bool) -> None:
        """
            Assert a boolean expression, throwing :code:`IllegalStateException` if the test result is :code:`false`. Call isTrue if
            you wish to throw IllegalArgumentException on an assertion failure. :code:`Assert.state(id == null, "The id property
            must not already be initialized");`
        
            Parameters:
                expression (boolean): a boolean expression
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the exception message to use if the assertion fails
        
            Raises:
                : if expression is :code:`false`
        
            Assert a boolean expression, throwing `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalStateException.html?is-external=true>` if the test
            result is :code:`false`.
        
            Call :meth:`~cern.accsoft.commons.util.Assert.isTrue` if you wish to throw `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` on an
            assertion failure. :code:`Assert.state(id == null);`
        
            Parameters:
                expression (boolean): a boolean expression
        
            Raises:
                : if the supplied expression is :code:`false`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def state(boolean: bool, string: str) -> None: ...

class BeanSupport:
    def __init__(self, object: typing.Any): ...
    @typing.overload
    def addPropertyChangeListener(self, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    @typing.overload
    def addPropertyChangeListener(self, string: str, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    @typing.overload
    def removePropertyChangeListener(self, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    @typing.overload
    def removePropertyChangeListener(self, string: str, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...

class BeanUtils:
    """
    public abstract class BeanUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Static convenience methods for JavaBeans: for instantiating beans, checking bean property types, copying bean
        properties, etc.
    
        Mainly for use within the framework, but to some degree also useful for application classes.
    """
    def __init__(self): ...
    @staticmethod
    def findDeclaredMethod(class_: typing.Type, string: str, classArray: typing.List[typing.Type]) -> java.lang.reflect.Method:
        """
            Find a method with the given method name and the given parameter types, declared on the given class or one of its
            superclasses. Will return a public, protected, package access, or private method.
        
            Checks :code:`Class.getDeclaredMethod`, cascading upwards to all superclasses.
        
            Parameters:
                clazz (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the class to check
                methodName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the method to find
                paramTypes (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`[]): the parameter types of the method to find
        
            Returns:
                the Method object, or :code:`null` if not found
        
            Also see:
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true#getDeclaredMethod(java.lang.String,java.lang.Class...)>`
        
        
        """
        ...
    @staticmethod
    def findDeclaredMethodWithMinimalParameters(class_: typing.Type, string: str) -> java.lang.reflect.Method: ...
    @staticmethod
    def findMethod(class_: typing.Type, string: str, classArray: typing.List[typing.Type]) -> java.lang.reflect.Method:
        """
            Find a method with the given method name and the given parameter types, declared on the given class or one of its
            superclasses. Prefers public methods, but will return a protected, package access, or private method too.
        
            Checks :code:`Class.getMethod` first, falling back to :code:`findDeclaredMethod`. This allows to find public methods
            without issues even in environments with restricted Java security settings.
        
            Parameters:
                clazz (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the class to check
                methodName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the method to find
                paramTypes (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`[]): the parameter types of the method to find
        
            Returns:
                the Method object, or :code:`null` if not found
        
            Also see:
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true#getMethod(java.lang.String,java.lang.Class...)>`,
                :meth:`~cern.accsoft.commons.util.BeanUtils.findDeclaredMethod`
        
        
        """
        ...
    @staticmethod
    def findMethodWithMinimalParameters(class_: typing.Type, string: str) -> java.lang.reflect.Method: ...
    @staticmethod
    def getNames(objectArray: typing.List[typing.Any]) -> typing.List[str]: ...
    @staticmethod
    def getPropertyType(class_: typing.Type, string: str) -> typing.Type: ...
    @staticmethod
    def getPropertyValue(object: typing.Any, string: str) -> typing.Any:
        """
            Returns property value of the specified bean. The value is retrieved using getter method which must be defined in the
            bean.
        
            If the given property is :code:`a`, the method tries to call :code:`getA()`, :code:`isA()` and :code:`a()` in this
            order. The method supports also chaining of getters called i.e. if the :code:`propertyName` is specified as
            :code:`a.b.c` the method will try to return result of :code:`bean.getA().getB().getC()`.
        
            Parameters:
                bean (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): bean
                propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of a property
        
            Returns:
                value of the property
        
        
        """
        ...
    @staticmethod
    def isSimpleProperty(class_: typing.Type) -> bool:
        """
            Check if the given type represents a "simple" property: a primitive, a String, a Class, or a corresponding array.
        
            Used to determine properties to check for a "simple" dependency-check.
        
            Parameters:
                clazz (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the type to check
        
            Returns:
                whether the given type represent a "simple" property
        
            Also see:
                :code:`AbstractBeanDefinition.DEPENDENCY_CHECK_SIMPLE`,
                :code:`AbstractAutowireCapableBeanFactory.checkDependencies(java.lang.String,
                org.springframework.beans.factory.support.AbstractBeanDefinition, java.beans.PropertyDescriptor[],
                org.springframework.beans.PropertyValues)`
        
        
        """
        ...
    @staticmethod
    def resolveSignature(string: str, class_: typing.Type) -> java.lang.reflect.Method:
        """
            Parse a method signature in the form :code:`methodName[([arg_list])]`, where :code:`arg_list` is an optional,
            comma-separated list of fully-qualified type names, and attempts to resolve that signature against the supplied
            :code:`Class`.
        
            When not supplying an argument list (:code:`methodName`) the method whose name matches and has the least number of
            parameters will be returned. When supplying an argument type list, only the method whose name and argument types match
            will be returned.
        
            Note then that :code:`methodName` and :code:`methodName()` are **not** resolved in the same way. The signature
            :code:`methodName` means the method called :code:`methodName` with the least number of arguments, whereas
            :code:`methodName()` means the method called :code:`methodName` with exactly 0 arguments.
        
            If no method can be found, then :code:`null` is returned.
        
            Parameters:
                signature (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the method signature as String representation
                clazz (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the class to resolve the method signature against
        
            Returns:
                the resolved Method
        
            Also see:
                :meth:`~cern.accsoft.commons.util.BeanUtils.findMethod`,
                :meth:`~cern.accsoft.commons.util.BeanUtils.findMethodWithMinimalParameters`
        
        
        """
        ...
    @staticmethod
    def toPropertyValues(objectArray: typing.List[typing.Any], string: str, class_: typing.Type) -> typing.List[typing.Any]: ...

class ClassLoaderJarInfo:
    """
    public class ClassLoaderJarInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        This static class allows you to get information about the currently loaded jar files appearing on your class path such
        as: jar file name/path, vendor name and version numbers.
    """
    JAR_EXT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JAR_EXT
    
        Default jar extension is '.jar'
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    @staticmethod
    def getJarInfo(string: str) -> 'JarInfo':
        """
            Return a JarInfo object containing main informations about the given jar name.
        
            Parameters:
                jarName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the jar/product name you need to get info from.(may not have extension)
        
            Returns:
                a JarInfo object containing main informations about the given jar name.
        
        """
        ...
    @typing.overload
    @staticmethod
    def getJarInfo(string: str, object: typing.Any) -> 'JarInfo':
        """
            Return a JarInfo object containing main informations about the given jar name.
        
            Parameters:
                jarName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the jar/product name you need to get info from.(may not have extension)
                object (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): needed to retreive the reference to the current classloader as the system clasloader do not contains reference to all
                    the loaded jar files.
        
            Returns:
                a JarInfo object containing main informations about the given jar name.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getLoadedJarInfo() -> java.util.HashMap[str, 'JarInfo']: ...
    @typing.overload
    @staticmethod
    def getLoadedJarInfo(object: typing.Any) -> java.util.HashMap[str, 'JarInfo']: ...

class ClassLoaderUtils:
    """
    public abstract class ClassLoaderUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class for diagnostic purposes, to analyze the ClassLoader hierarchy for any given object or class loader.
    
        Since:
            02 April 2001
    
        Also see:
            `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/ClassLoader.html?is-external=true>`
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def showClassLoaderHierarchy(classLoader: java.lang.ClassLoader) -> str:
        """
            Show the class loader hierarchy for the given class loader. Uses default line break and tab text characters.
        
            Parameters:
                cl (`ClassLoader <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/ClassLoader.html?is-external=true>`): class loader to analyze hierarchy for
        
            Returns:
                a String showing the class loader hierarchy for this class
        
        """
        ...
    @typing.overload
    @staticmethod
    def showClassLoaderHierarchy(classLoader: java.lang.ClassLoader, string: str, string2: str) -> str:
        """
            Show the class loader hierarchy for the given class loader.
        
            Parameters:
                cl (`ClassLoader <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/ClassLoader.html?is-external=true>`): class loader to analyze hierarchy for
                lineBreak (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): line break
                tabText (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): text to use to set tabs
        
            Returns:
                a String showing the class loader hierarchy for this class
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def showClassLoaderHierarchy(object: typing.Any, string: str) -> str:
        """
            Show the class loader hierarchy for this class. Uses default line break and tab text characters.
        
            Parameters:
                obj (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): object to analyze loader hierarchy for
                role (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a description of the role of this class in the application (e.g., "servlet" or "EJB reference")
        
            Returns:
                a String showing the class loader hierarchy for this class
        
        """
        ...
    @typing.overload
    @staticmethod
    def showClassLoaderHierarchy(object: typing.Any, string: str, string2: str, string3: str) -> str:
        """
            Show the class loader hierarchy for this class.
        
            Parameters:
                obj (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): object to analyze loader hierarchy for
                role (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a description of the role of this class in the application (e.g., "servlet" or "EJB reference")
                lineBreak (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): line break
                tabText (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): text to use to set tabs
        
            Returns:
                a String showing the class loader hierarchy for this class
        
        """
        ...

class ClassUtils:
    ARRAY_SUFFIX: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def addResourcePathToPackagePath(class_: typing.Type, string: str) -> str: ...
    @typing.overload
    @staticmethod
    def classNamesToString(classArray: typing.List[typing.Type]) -> str: ...
    @typing.overload
    @staticmethod
    def classNamesToString(collection: typing.Union[java.util.Collection, typing.Sequence]) -> str: ...
    @staticmethod
    def classPackageAsResourcePath(class_: typing.Type) -> str: ...
    @staticmethod
    def createCompositeInterface(classArray: typing.List[typing.Type], classLoader: java.lang.ClassLoader) -> typing.Type: ...
    @staticmethod
    def findClassVersion(class_: typing.Type[typing.Any]) -> str: ...
    @typing.overload
    @staticmethod
    def forName(string: str) -> typing.Type: ...
    @typing.overload
    @staticmethod
    def forName(string: str, classLoader: java.lang.ClassLoader) -> typing.Type: ...
    @staticmethod
    def getAllInterfaces(object: typing.Any) -> typing.List[typing.Type]: ...
    @staticmethod
    def getAllInterfacesAsSet(object: typing.Any) -> java.util.Set: ...
    @staticmethod
    def getAllInterfacesForClass(class_: typing.Type) -> typing.List[typing.Type]: ...
    @staticmethod
    def getAllInterfacesForClassAsSet(class_: typing.Type) -> java.util.Set: ...
    @staticmethod
    def getClassFileName(class_: typing.Type) -> str: ...
    @staticmethod
    def getConstructorIfAvailable(class_: typing.Type, classArray: typing.List[typing.Type]) -> java.lang.reflect.Constructor: ...
    @staticmethod
    def getDefaultClassLoader() -> java.lang.ClassLoader: ...
    @staticmethod
    def getMethodCountForName(class_: typing.Type, string: str) -> int: ...
    @staticmethod
    def getMethodIfAvailable(class_: typing.Type, string: str, classArray: typing.List[typing.Type]) -> java.lang.reflect.Method: ...
    @staticmethod
    def getQualifiedMethodName(method: java.lang.reflect.Method) -> str: ...
    @staticmethod
    def getQualifiedName(class_: typing.Type) -> str: ...
    @typing.overload
    @staticmethod
    def getShortName(class_: typing.Type) -> str: ...
    @typing.overload
    @staticmethod
    def getShortName(string: str) -> str: ...
    @staticmethod
    def getShortNameAsProperty(class_: typing.Type) -> str: ...
    @staticmethod
    def getStaticMethod(class_: typing.Type, string: str, classArray: typing.List[typing.Type]) -> java.lang.reflect.Method: ...
    @typing.overload
    @staticmethod
    def getUserClass(class_: typing.Type) -> typing.Type: ...
    @typing.overload
    @staticmethod
    def getUserClass(object: typing.Any) -> typing.Type: ...
    @staticmethod
    def hasAtLeastOneMethodWithName(class_: typing.Type, string: str) -> bool: ...
    @staticmethod
    def hasConstructor(class_: typing.Type, classArray: typing.List[typing.Type]) -> bool: ...
    @staticmethod
    def hasMethod(class_: typing.Type, string: str, classArray: typing.List[typing.Type]) -> bool: ...
    @staticmethod
    def isAssignable(class_: typing.Type, class2: typing.Type) -> bool: ...
    @staticmethod
    def isAssignableValue(class_: typing.Type, object: typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def isPresent(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isPresent(string: str, classLoader: java.lang.ClassLoader) -> bool: ...
    @staticmethod
    def isPrimitiveArray(class_: typing.Type) -> bool: ...
    @staticmethod
    def isPrimitiveOrWrapper(class_: typing.Type) -> bool: ...
    @staticmethod
    def isPrimitiveWrapper(class_: typing.Type) -> bool: ...
    @staticmethod
    def isPrimitiveWrapperArray(class_: typing.Type) -> bool: ...
    @staticmethod
    def resolveClassName(string: str, classLoader: java.lang.ClassLoader) -> typing.Type: ...
    @staticmethod
    def resolvePrimitiveClassName(string: str) -> typing.Type: ...

class ClasspathUtils:
    """
    public class ClasspathUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class to retreive all subclasses of the given class in the given package.
    """
    @staticmethod
    def findSubClassesInPackage(class_: typing.Type[typing.Any], string: str, boolean: bool) -> java.util.Set[typing.Type[typing.Any]]: ...

class Cleanable:
    """
    public interface Cleanable
    
        Objects implementing this interface are supporting cleanup().
    
    
    
    
        As several instances of the same GUI components/object could be use in a unique java virtual machine, when closing a
        window containing one of these instances you are expecting that all object, listeners, etc referenced by the this GUI to
        be carefully cleaned-up in order to avoid memory leaks.
    
    
        All objects implementing the Cleanable interfaces contained in the RootPane of ContextFrame/ExternalFrame class will
        have their :meth:`~cern.accsoft.commons.util.Cleanable.cleanup` method called by the ContextFrame/ExternalFrame.
    
    
        Notice that it is up to you to implement the following code given as example below in order to cleanup properly all
        objects referenced by your Cleanable objects recursively.
    
    
    
    
        The :meth:`~cern.accsoft.commons.util.Cleanable.isCleaning` method is very important as it can prevent
        NullPointerExceptions due to asynchronous calls from method called by EventListeners **during the cleanup phase** of
        your object.
    """
    def cleanup(self) -> None:
        """
            Clean the current object. Free ressources, set references to null,...
        
        
            Sample usage:
        
            .. code-block: java
            
              private AtomicBoolean cleaning = new AtomicBoolean(false);
              ...
              @Override
                 public void cleanup() {
                     // allow only one unique call for this method
                     if (cleaning.compareAndSet(false, true)) {
                         // cleanup all references on any object you are using here
                         
                         if (chartRenderer != null) {
                             // recursively cleanup also objects you are using
                             chartRenderer.cleanup();
                             chartRenderer = null;
                         }
                         
                         edChart = null;
                         name = null;
                         dataProvider = null;
                         currentEditionEntry = null;
                         ...
                     }
                 }
             
        
        """
        ...
    def isCleaning(self) -> bool:
        """
        
            Returns:
                true if the :meth:`~cern.accsoft.commons.util.Cleanable.cleanup` method is currently being executed, false otherwise.
        
        
                Sample usage:
        
        
        
                    .. code-block: java
                    
                      private AtomicBoolean cleaning = new AtomicBoolean(false);
                      ...
                      @Override
                      public boolean isCleaning() {
                         return cleaning.get();
                      }
                     
        
        
        """
        ...

class CleanableUtil:
    """
    public class CleanableUtil extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility methods related to the :class:`~cern.accsoft.commons.util.Cleanable` interface.
    """
    @staticmethod
    def cleanupContainer(container: java.awt.Container) -> None:
        """
            Calls the :meth:`~cern.accsoft.commons.util.Cleanable.cleanup` method recursively on all containers contained by the
            given container argument. Can be null.
        
            Parameters:
                container (`Container <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/awt/Container.html?is-external=true>`): the Container on which the :meth:`~cern.accsoft.commons.util.Cleanable.cleanup` method will be applied.
        
        
        """
        ...

class CollectionUtils:
    """
    public abstract class CollectionUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Miscellaneous collection utility methods.
    
        Since:
            1.1.3
    """
    def __init__(self): ...
    @staticmethod
    def arrayToList(object: typing.Any) -> java.util.List:
        """
            Convert the supplied array into a List. A primitive array gets converted into a List of the appropriate wrapper type.
        
            A :code:`null` source value will be converted to an empty List.
        
            Parameters:
                source (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the (potentially primitive) array
        
            Returns:
                the converted List result
        
            Also see:
                :code:`ObjectUtils#toObjectArray(Object)`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def contains(enumeration: java.util.Enumeration, object: typing.Any) -> bool:
        """
            Check whether the given Iterator contains the given element.
        
            Parameters:
                iterator (`Iterator <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Iterator.html?is-external=true>`): the Iterator to check
                element (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the element to look for
        
            Returns:
                :code:`true` if found, :code:`false` else
        
            Check whether the given Enumeration contains the given element.
        
            Parameters:
                enumeration (`Enumeration <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Enumeration.html?is-external=true>`): the Enumeration to check
                element (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the element to look for
        
            Returns:
                :code:`true` if found, :code:`false` else
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def contains(iterator: java.util.Iterator, object: typing.Any) -> bool: ...
    @staticmethod
    def containsAny(collection: typing.Union[java.util.Collection, typing.Sequence], collection2: typing.Union[java.util.Collection, typing.Sequence]) -> bool:
        """
            Return :code:`true` if any element in ':code:`candidates`' is contained in ':code:`source`'; otherwise returns
            :code:`false`.
        
            Parameters:
                source (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`): the source Collection
                candidates (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`): the candidates to search for
        
            Returns:
                whether any of the candidates has been found
        
        
        """
        ...
    @staticmethod
    def containsInstance(collection: typing.Union[java.util.Collection, typing.Sequence], object: typing.Any) -> bool:
        """
            Check whether the given Collection contains the given element instance.
        
            Enforces the given instance to be present, rather than returning :code:`true` for an equal element as well.
        
            Parameters:
                collection (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`): the Collection to check
                element (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the element to look for
        
            Returns:
                :code:`true` if found, :code:`false` else
        
        
        """
        ...
    @staticmethod
    def findFirstMatch(collection: typing.Union[java.util.Collection, typing.Sequence], collection2: typing.Union[java.util.Collection, typing.Sequence]) -> typing.Any:
        """
            Return the first element in ':code:`candidates`' that is contained in ':code:`source`'. If no element in
            ':code:`candidates`' is present in ':code:`source`' returns :code:`null`. Iteration order is `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>` implementation
            specific.
        
            Parameters:
                source (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`): the source Collection
                candidates (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`): the candidates to search for
        
            Returns:
                the first present object, or :code:`null` if not found
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def findValueOfType(collection: typing.Union[java.util.Collection, typing.Sequence], class_: typing.Type) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def findValueOfType(collection: typing.Union[java.util.Collection, typing.Sequence], classArray: typing.List[typing.Type]) -> typing.Any: ...
    _flatten__C = typing.TypeVar('_flatten__C', bound=java.util.Collection)  # <C>
    _flatten__T = typing.TypeVar('_flatten__T')  # <T>
    @staticmethod
    def flatten(collection: typing.Union[java.util.Collection[java.util.Collection[_flatten__T]], typing.Sequence[java.util.Collection[_flatten__T]]], collector: java.util.stream.Collector[_flatten__T, typing.Any, _flatten__C]) -> _flatten__C: ...
    _flattenToList__T = typing.TypeVar('_flattenToList__T')  # <T>
    @staticmethod
    def flattenToList(collection: typing.Union[java.util.Collection[java.util.Collection[_flattenToList__T]], typing.Sequence[java.util.Collection[_flattenToList__T]]]) -> java.util.List[_flattenToList__T]: ...
    _flattenToSet__T = typing.TypeVar('_flattenToSet__T')  # <T>
    @staticmethod
    def flattenToSet(collection: typing.Union[java.util.Collection[java.util.Collection[_flattenToSet__T]], typing.Sequence[java.util.Collection[_flattenToSet__T]]]) -> java.util.Set[_flattenToSet__T]: ...
    @staticmethod
    def hasUniqueObject(collection: typing.Union[java.util.Collection, typing.Sequence]) -> bool:
        """
            Determine whether the given Collection only contains a single unique object.
        
            Parameters:
                collection (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`): the Collection to check
        
            Returns:
                :code:`true` if the collection contains a single reference or multiple references to the same instance, :code:`false`
                else
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isEmpty(collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    @typing.overload
    @staticmethod
    def isEmpty(map: typing.Union[java.util.Map[typing.Any, typing.Any], typing.Mapping[typing.Any, typing.Any]]) -> bool: ...
    @staticmethod
    def mergeArrayIntoCollection(object: typing.Any, collection: typing.Union[java.util.Collection, typing.Sequence]) -> None:
        """
            Merge the given array into the given Collection.
        
            Parameters:
                array (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the array to merge (may be :code:`null`)
                collection (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`): the target Collection to merge the array into
        
        
        """
        ...
    @staticmethod
    def mergePropertiesIntoMap(properties: java.util.Properties, map: typing.Union[java.util.Map, typing.Mapping]) -> None:
        """
            Merge the given Properties instance into the given Map, copying all properties (key-value pairs) over.
        
            Uses :code:`Properties.propertyNames()` to even catch default properties linked into the original Properties instance.
        
            Parameters:
                props (`Properties <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Properties.html?is-external=true>`): the Properties instance to merge (may be :code:`null`)
                map (`Map <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Map.html?is-external=true>`): the target Map to merge the properties into
        
        
        """
        ...
    _toSet__E = typing.TypeVar('_toSet__E')  # <E>
    @staticmethod
    def toSet(eArray: typing.List[_toSet__E]) -> java.util.Set[_toSet__E]: ...
    _toSortedList__T = typing.TypeVar('_toSortedList__T')  # <T>
    @staticmethod
    def toSortedList(collection: typing.Union[java.util.Collection[_toSortedList__T], typing.Sequence[_toSortedList__T]]) -> java.util.List[_toSortedList__T]: ...

class ExceptionUtils:
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def extractExceptionMessage(throwable: java.lang.Throwable) -> str: ...
    @typing.overload
    @staticmethod
    def extractExceptionMessage(throwable: java.lang.Throwable, boolean: bool) -> str: ...
    @staticmethod
    def filterStackTrace(throwable: java.lang.Throwable, string: str) -> None: ...
    @staticmethod
    def getCondensedStackTrace(throwable: java.lang.Throwable, int: int) -> str: ...
    @staticmethod
    def getRootCause(throwable: java.lang.Throwable) -> java.lang.Throwable: ...
    @staticmethod
    def getStackTraceAsString(throwable: java.lang.Throwable) -> str: ...

class FileCopyUtils:
    """
    public abstract class FileCopyUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Simple utility methods for file and stream copying. All copy methods use a block size of 4096 bytes, and close all
        affected streams when done.
    
        Mainly for use within the framework, but also useful for application code.
    
        Since:
            06.10.2003
    """
    BUFFER_SIZE: typing.ClassVar[int] = ...
    """
    public static final int BUFFER_SIZE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def copy(file: typing.Union[java.io.File, jpype.protocol.SupportsPath], file2: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> int: ...
    @typing.overload
    @staticmethod
    def copy(inputStream: java.io.InputStream, outputStream: java.io.OutputStream) -> int: ...
    @typing.overload
    @staticmethod
    def copy(reader: java.io.Reader, writer: java.io.Writer) -> int: ...
    @typing.overload
    @staticmethod
    def copy(byteArray: typing.List[int], file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None: ...
    @typing.overload
    @staticmethod
    def copy(byteArray: typing.List[int], outputStream: java.io.OutputStream) -> None: ...
    @typing.overload
    @staticmethod
    def copy(string: str, writer: java.io.Writer) -> None: ...
    @typing.overload
    @staticmethod
    def copyToByteArray(file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> typing.List[int]: ...
    @typing.overload
    @staticmethod
    def copyToByteArray(inputStream: java.io.InputStream) -> typing.List[int]: ...
    @staticmethod
    def copyToString(reader: java.io.Reader) -> str: ...

class FileUtils:
    """
    public class FileUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utilities for File I/O, inspired from the .NET System.IO.File class
    """
    FS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` FS
    
        The platform independent file separator. (can be "/" or "\").
    
    """
    DATA_URL: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DATA_URL
    
        This URL string is pointing to the default java development DATA directory.(/acc/java/data)
    
    
        Should be use only for READING data file. If you need to WRITE data file, please use the
        :meth:`~cern.accsoft.commons.util.FileUtils.DATA_PATH` constant.
    
    
        This constant is platform independent.
    
    
        i.e.:
    
    
        If your application is in the package cern.ade.my_app_package, you may get data files related to this application via
        the URL path: DATA_URL + FS + "ade" + FS + "my_app_package"+ FS
    
        Also see:
            :meth:`~constant`
    
    
    """
    DATA_PATH: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DATA_PATH
    
        This PATH string is pointing to the default java development DATA directory.
    
    
        This constant is platform independent.
    
    
        i.e.:
    
    
        If your application is in the package cern.ps.ade.my_app_package, you may get data files related to this application via
        the URL path: DATA_PATH + FS + "ade" + FS + "my_app_package"+ FS
    
    """
    FILE_BY_DATE_COMPARATOR: typing.ClassVar[java.util.Comparator] = ...
    """
    public static final `Comparator <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Comparator.html?is-external=true>`<? super `File <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/File.html?is-external=true>`> FILE_BY_DATE_COMPARATOR
    
        A comparator that sorts files by date, oldest first
    
    """
    def __init__(self): ...
    @staticmethod
    def createFilenameFilter(string: str) -> java.io.FilenameFilter:
        """
            Little helper method to create a `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/FilenameFilter.html?is-external=true>` for the specified
            file name to match.
        
        
            Parameters:
                fileNameToMatch (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a String to be matched or :code:`null` or "*" to match all files. Regex are not supported (yet)
        
            Returns:
                a FileNameFilter object
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def findFiles(file: typing.Union[java.io.File, jpype.protocol.SupportsPath], filenameFilter: typing.Union[java.io.FilenameFilter, typing.Callable]) -> java.util.List[java.io.File]: ...
    @typing.overload
    @staticmethod
    def findFiles(string: str, string2: str) -> java.util.List[str]: ...
    @staticmethod
    def getTempDir() -> java.io.File: ...
    @typing.overload
    @staticmethod
    def readAllLines(inputStream: java.io.InputStream) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def readAllLines(string: str) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def readAllText(inputStream: java.io.InputStream) -> str: ...
    @typing.overload
    @staticmethod
    def readAllText(string: str) -> str: ...

class JarInfo:
    """
    public class JarInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Container to store the main information about a jar file used by the
        :class:`~cern.accsoft.commons.util.ClassLoaderJarInfo` class.
    """
    classLoaderName: str = ...
    """
    public `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` classLoaderName
    
        The classloader name
    
    """
    cbngJarName: str = ...
    """
    public `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` cbngJarName
    
        The jar name which is in fact the product name + CBNG version + '.jar' extension
    
    """
    jarName: str = ...
    """
    public `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` jarName
    
        The jar name which is in fact the product name + '.jar' extension
    
    """
    vendor: str = ...
    """
    public `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` vendor
    
        The jar vendor provider... CERN for us ;o)
    
    """
    version: str = ...
    """
    public `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` version
    
        The jar version number in the format xx.xx.xx
    
    """
    version2: str = ...
    """
    public `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` version2
    
        The vendor dependent jar version number (@CERN yyyymmdd)
    
    """
    jarPath: str = ...
    """
    public `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` jarPath
    
        The jar file PATH/URL.
    
    """
    def __init__(self): ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
            Returns:
                a String representation of this object.
        
        
        """
        ...

class JdkUtils:
    """
    public class JdkUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility methods e.g. to find a valid JDK
    """
    JDK_VERSION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JDK_VERSION
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    JDK_PATH_DEFAULT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JDK_PATH_DEFAULT
    
    
    """
    def __init__(self): ...
    @staticmethod
    def findCurrentJdkDir() -> str:
        """
            Tries to find a JDK directory based on the "java.home" System property.
        
            Returns:
                the JDK directory or :code:`null` if none can be found
        
        
        """
        ...
    @staticmethod
    def findCurrentJvmPath() -> java.nio.file.Path:
        """
            Finds the Path of current Java Executable, based on "java.home"
        
            Returns:
        
            Also see:
                :code:`#findJdkDirFromJavaHome()`
        
        
        """
        ...
    @staticmethod
    def findJdkDirsUnder(string: str) -> java.util.List[str]: ...
    @staticmethod
    def findStandardJdkDirs() -> java.util.List[str]: ...
    @staticmethod
    def getPidLinux() -> int: ...

class MapUtils:
    """
    public class MapUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utilities for working with maps
    """
    def __init__(self): ...
    _extractValues__K = typing.TypeVar('_extractValues__K')  # <K>
    _extractValues__V = typing.TypeVar('_extractValues__V')  # <V>
    _extractValues__C = typing.TypeVar('_extractValues__C', bound=java.util.Collection)  # <C>
    @staticmethod
    def extractValues(map: typing.Union[java.util.Map[_extractValues__K, _extractValues__C], typing.Mapping[_extractValues__K, _extractValues__C]]) -> java.util.Set[_extractValues__V]: ...
    _findMatchingValues__T = typing.TypeVar('_findMatchingValues__T')  # <T>
    @staticmethod
    def findMatchingValues(map: typing.Union[java.util.Map[str, _findMatchingValues__T], typing.Mapping[str, _findMatchingValues__T]], string: str, matchType: 'MapUtils.MatchType') -> java.util.Map[str, _findMatchingValues__T]: ...
    _getKeyByValue__T = typing.TypeVar('_getKeyByValue__T')  # <T>
    _getKeyByValue__E = typing.TypeVar('_getKeyByValue__E')  # <E>
    @staticmethod
    def getKeyByValue(map: typing.Union[java.util.Map[_getKeyByValue__T, _getKeyByValue__E], typing.Mapping[_getKeyByValue__T, _getKeyByValue__E]], e: _getKeyByValue__E) -> _getKeyByValue__T: ...
    _getKeysByValue__T = typing.TypeVar('_getKeysByValue__T')  # <T>
    _getKeysByValue__E = typing.TypeVar('_getKeysByValue__E')  # <E>
    @staticmethod
    def getKeysByValue(map: typing.Union[java.util.Map[_getKeysByValue__T, _getKeysByValue__E], typing.Mapping[_getKeysByValue__T, _getKeysByValue__E]], e: _getKeysByValue__E) -> java.util.Set[_getKeysByValue__T]: ...
    _indexBy__T = typing.TypeVar('_indexBy__T')  # <T>
    @staticmethod
    def indexBy(tArray: typing.List[_indexBy__T], string: str, objectArray: typing.List[typing.Any]) -> java.util.Map[str, _indexBy__T]: ...
    _indexByName__T = typing.TypeVar('_indexByName__T')  # <T>
    @staticmethod
    def indexByName(tArray: typing.List[_indexByName__T]) -> java.util.Map[str, _indexByName__T]: ...
    _valuesIntersection__K = typing.TypeVar('_valuesIntersection__K')  # <K>
    _valuesIntersection__V = typing.TypeVar('_valuesIntersection__V')  # <V>
    _valuesIntersection__C = typing.TypeVar('_valuesIntersection__C', bound=java.util.Collection)  # <C>
    @staticmethod
    def valuesIntersection(map: typing.Union[java.util.Map[_valuesIntersection__K, _valuesIntersection__C], typing.Mapping[_valuesIntersection__K, _valuesIntersection__C]]) -> java.util.Set[_valuesIntersection__V]: ...
    class MatchType(java.lang.Enum['MapUtils.MatchType']):
        STARTS_WITH: typing.ClassVar['MapUtils.MatchType'] = ...
        CONTAINS: typing.ClassVar['MapUtils.MatchType'] = ...
        ENDS_WITH: typing.ClassVar['MapUtils.MatchType'] = ...
        REGEXP: typing.ClassVar['MapUtils.MatchType'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'MapUtils.MatchType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['MapUtils.MatchType']: ...

class MockitoUtil:
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def wireWithMocks(object: typing.Any) -> java.util.Map[str, typing.Any]: ...
    @typing.overload
    @staticmethod
    def wireWithMocks(object: typing.Any, class_: typing.Type[typing.Any]) -> java.util.Map[str, typing.Any]: ...

class Named:
    """
    public interface Named
    
        Everything what has a name.
    """
    def getName(self) -> str:
        """
            Returns the name.
        
            Returns:
                the name
        
        
        """
        ...

class Nameds:
    """
    public class Nameds extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility methods to work with :class:`~cern.accsoft.commons.util.Named`'s.
    """
    NAMED_MAPPER: typing.ClassVar['Mappers.Mapper'] = ...
    """
    public static final :class:`~cern.accsoft.commons.util.Mappers.Mapper`<:class:`~cern.accsoft.commons.util.Named`, `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`> NAMED_MAPPER
    
        Mapper :class:`~cern.accsoft.commons.util.Named` -> name
    
    """
    NAMED_COMPARATOR: typing.ClassVar[java.util.Comparator] = ...
    """
    public static final `Comparator <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Comparator.html?is-external=true>`<:class:`~cern.accsoft.commons.util.Named`> NAMED_COMPARATOR
    
        Comparator which uses names to compare two entities.
    
    """
    def __init__(self): ...
    _containsByName__T = typing.TypeVar('_containsByName__T', bound=Named)  # <T>
    @staticmethod
    def containsByName(collection: typing.Union[java.util.Collection[_containsByName__T], typing.Sequence[_containsByName__T]], string: str) -> bool: ...
    _filterByNames_0__T = typing.TypeVar('_filterByNames_0__T', bound=Named)  # <T>
    _filterByNames_1__T = typing.TypeVar('_filterByNames_1__T', bound=Named)  # <T>
    _filterByNames_2__T = typing.TypeVar('_filterByNames_2__T', bound=Named)  # <T>
    @typing.overload
    @staticmethod
    def filterByNames(collection: typing.Union[java.util.Collection[_filterByNames_0__T], typing.Sequence[_filterByNames_0__T]], collection2: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Collection[_filterByNames_0__T]: ...
    @typing.overload
    @staticmethod
    def filterByNames(list: java.util.List[_filterByNames_1__T], collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.List[_filterByNames_1__T]: ...
    @typing.overload
    @staticmethod
    def filterByNames(set: java.util.Set[_filterByNames_2__T], collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[_filterByNames_2__T]: ...
    _findByName_0__T = typing.TypeVar('_findByName_0__T', bound=Named)  # <T>
    _findByName_1__T = typing.TypeVar('_findByName_1__T', bound=Named)  # <T>
    @typing.overload
    @staticmethod
    def findByName(tArray: typing.List[_findByName_0__T], string: str) -> _findByName_0__T:
        """
            Finds a :class:`~cern.accsoft.commons.util.Named` by name in an array.
        
            Parameters:
                nameds (T[]): array of :class:`~cern.accsoft.commons.util.Named`'s
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name to select by
        
            Returns:
                found :class:`~cern.accsoft.commons.util.Named` or :code:`null`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def findByName(collection: typing.Union[java.util.Collection[_findByName_1__T], typing.Sequence[_findByName_1__T]], string: str) -> _findByName_1__T: ...
    @typing.overload
    @staticmethod
    def getNames(collection: typing.Union[java.util.Collection[Named], typing.Sequence[Named]]) -> java.util.Collection[str]: ...
    @typing.overload
    @staticmethod
    def getNames(namedArray: typing.List[Named]) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def getNames(list: java.util.List[Named]) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def getNames(set: java.util.Set[Named]) -> java.util.Set[str]: ...
    @staticmethod
    def getNamesList(collection: typing.Union[java.util.Collection[Named], typing.Sequence[Named]]) -> java.util.List[str]: ...
    @staticmethod
    def getNamesSet(collection: typing.Union[java.util.Collection[Named], typing.Sequence[Named]]) -> java.util.Set[str]: ...
    @typing.overload
    @staticmethod
    def getSortedNames(collection: typing.Union[java.util.Collection[Named], typing.Sequence[Named]]) -> java.util.Collection[str]: ...
    @typing.overload
    @staticmethod
    def getSortedNames(namedArray: typing.List[Named]) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def getSortedNames(list: java.util.List[Named]) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def getSortedNames(set: java.util.Set[Named]) -> java.util.Set[str]: ...
    _mapByName_0__T = typing.TypeVar('_mapByName_0__T', bound=Named)  # <T>
    _mapByName_1__T = typing.TypeVar('_mapByName_1__T', bound=Named)  # <T>
    @typing.overload
    @staticmethod
    def mapByName(tArray: typing.List[_mapByName_0__T]) -> java.util.Map[str, _mapByName_0__T]: ...
    @typing.overload
    @staticmethod
    def mapByName(collection: typing.Union[java.util.Collection[_mapByName_1__T], typing.Sequence[_mapByName_1__T]]) -> java.util.Map[str, _mapByName_1__T]: ...
    _sortByName_0__T = typing.TypeVar('_sortByName_0__T', bound=Named)  # <T>
    _sortByName_1__T = typing.TypeVar('_sortByName_1__T', bound=Named)  # <T>
    @typing.overload
    @staticmethod
    def sortByName(list: java.util.List[_sortByName_0__T]) -> java.util.List[_sortByName_0__T]: ...
    @typing.overload
    @staticmethod
    def sortByName(set: java.util.Set[_sortByName_1__T]) -> java.util.Set[_sortByName_1__T]: ...
    _sortByNameToList__T = typing.TypeVar('_sortByNameToList__T', bound=Named)  # <T>
    @staticmethod
    def sortByNameToList(collection: typing.Union[java.util.Collection[_sortByNameToList__T], typing.Sequence[_sortByNameToList__T]]) -> java.util.List[_sortByNameToList__T]: ...
    _sortByNameToSet__T = typing.TypeVar('_sortByNameToSet__T', bound=Named)  # <T>
    @staticmethod
    def sortByNameToSet(collection: typing.Union[java.util.Collection[_sortByNameToSet__T], typing.Sequence[_sortByNameToSet__T]]) -> java.util.Set[_sortByNameToSet__T]: ...

class NumberUtils:
    """
    public abstract class NumberUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Miscellaneous utility methods for number conversion and parsing. Mainly for internal use within the framework; consider
        Jakarta's Commons Lang for a more comprehensive suite of string utilities.
    
        Since:
            1.1.2
    """
    HEXADECIMAL_FORMAT_PREFIX: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` HEXADECIMAL_FORMAT_PREFIX
    
        This is the hexadecimal format prefix.
    
        Also see:
            :meth:`~constant`
    
    
    """
    HEXADECIMAL_FORMAT_RADIX: typing.ClassVar[int] = ...
    """
    public static final int HEXADECIMAL_FORMAT_RADIX
    
        This is the hexadecimal format radix.
    
        Also see:
            :meth:`~constant`
    
    
    """
    BINARY_FORMAT_PREFIX: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` BINARY_FORMAT_PREFIX
    
        This is the binary format prefix.
    
        Also see:
            :meth:`~constant`
    
    
    """
    BINARY_FORMAT_RADIX: typing.ClassVar[int] = ...
    """
    public static final int BINARY_FORMAT_RADIX
    
        This is the binary format radix.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    @staticmethod
    def convertNumberToTargetClass(number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], class_: typing.Type) -> java.lang.Number: ...
    @typing.overload
    @staticmethod
    def parseNumber(string: str, class_: typing.Type) -> java.lang.Number:
        """
            Parse the given text into a number instance of the given target class, using the corresponding default :code:`decode`
            methods. Trims the input :code:`String` before attempting to parse the number. Supports numbers in hex format (with
            leading 0x) and in octal format (with leading 0).
        
            Parameters:
                text (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the text to convert
                targetClass (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the target class to parse into
        
            Returns:
                the parsed number
        
            Raises:
                : if the target class is not supported (i.e. not a standard Number subclass as included in the JDK)
        
            Also see:
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Byte.html?is-external=true#decode(java.lang.String)>`,
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Short.html?is-external=true#decode(java.lang.String)>`,
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Integer.html?is-external=true#decode(java.lang.String)>`,
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true#decode(java.lang.String)>`,
                :meth:`~cern.accsoft.commons.util.NumberUtils.decodeBigInteger`, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Float.html?is-external=true#valueOf(java.lang.String)>`,
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Double.html?is-external=true#valueOf(java.lang.String)>`,
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/math/BigDecimal.html?is-external=true#%3Cinit%3E(java.lang.String)>`
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseNumber(string: str, class_: typing.Type, numberFormat: java.text.NumberFormat) -> java.lang.Number:
        """
            Parse the given text into a number instance of the given target class, using the given NumberFormat. Trims the input
            :code:`String` before attempting to parse the number.
        
            Parameters:
                text (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the text to convert
                targetClass (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the target class to parse into
                numberFormat (`NumberFormat <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/text/NumberFormat.html?is-external=true>`): the NumberFormat to use for parsing (if :code:`null`, this method falls back to :code:`parseNumber(String, Class)`)
        
            Returns:
                the parsed number
        
            Raises:
                : if the target class is not supported (i.e. not a standard Number subclass as included in the JDK)
        
            Also see:
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/text/NumberFormat.html?is-external=true#parse(java.lang.String,java.text.ParsePosition)>`,
                :meth:`~cern.accsoft.commons.util.NumberUtils.convertNumberToTargetClass`,
                :meth:`~cern.accsoft.commons.util.NumberUtils.parseNumber`
        
        
        """
        ...

class OSUtils:
    """
    public abstract class OSUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    IS_WINDOWS: typing.ClassVar[bool] = ...
    """
    public static final boolean IS_WINDOWS
    
    
    """
    IS_LINUX: typing.ClassVar[bool] = ...
    """
    public static final boolean IS_LINUX
    
    
    """
    def __init__(self): ...

class ObjectUtils:
    """
    public abstract class ObjectUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Miscellaneous object utility methods. Mainly for internal use within the framework; consider Jakarta's Commons Lang for
        a more comprehensive suite of object utilities.
    
        Since:
            19.03.2004
    
        Also see:
            :code:`org.apache.commons.lang.ObjectUtils`
    """
    def __init__(self): ...
    @staticmethod
    def getDisplayString(object: typing.Any) -> str:
        """
            Return a content-based String representation if :code:`obj` is not :code:`null`; otherwise returns an empty String.
        
            Differs from :meth:`~cern.accsoft.commons.util.ObjectUtils.nullSafeToString` in that it returns an empty String rather
            than "null" for a :code:`null` value.
        
            Parameters:
                obj (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the object to build a display String for
        
            Returns:
                a display String representation of :code:`obj`
        
            Also see:
                :meth:`~cern.accsoft.commons.util.ObjectUtils.nullSafeToString`
        
        
        """
        ...
    @staticmethod
    def getIdentityHexString(object: typing.Any) -> str:
        """
            Return a hex String form of an object's identity hash code.
        
            Parameters:
                obj (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the object
        
            Returns:
                the object's identity code in hex notation
        
        
        """
        ...
    @typing.overload
    def hashCode(self) -> int: ...
    @typing.overload
    @staticmethod
    def hashCode(boolean: bool) -> int:
        """
            Return the same value as .
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#hashCode()>`
        
            Return the same value as .
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Double.html?is-external=true#hashCode()>`
        
            Return the same value as .
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Float.html?is-external=true#hashCode()>`
        
            Return the same value as .
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true#hashCode()>`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def hashCode(double: float) -> int: ...
    @typing.overload
    @staticmethod
    def hashCode(float: float) -> int: ...
    @typing.overload
    @staticmethod
    def hashCode(long: int) -> int: ...
    @staticmethod
    def identityToString(object: typing.Any) -> str:
        """
            Return a String representation of an object's overall identity.
        
            Parameters:
                obj (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the object (may be :code:`null`)
        
            Returns:
                the object's identity as String representation, or :code:`null` if the object was :code:`null`
        
        
        """
        ...
    @staticmethod
    def isCheckedException(throwable: java.lang.Throwable) -> bool:
        """
            Return whether the given throwable is a checked exception: that is, neither a RuntimeException nor an Error.
        
            Parameters:
                ex (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): the throwable to check
        
            Returns:
                whether the throwable is a checked exception
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>`, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Error.html?is-external=true>`
        
        
        """
        ...
    @staticmethod
    def isCompatibleWithThrowsClause(throwable: java.lang.Throwable, classArray: typing.List[typing.Type]) -> bool:
        """
            Check whether the given exception is compatible with the exceptions declared in a throws clause.
        
            Parameters:
                ex (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): the exception to checked
                declaredExceptions (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`[]): the exceptions declared in the throws clause
        
            Returns:
                whether the given exception is compatible
        
        
        """
        ...
    @staticmethod
    def nullSafeClassName(object: typing.Any) -> str:
        """
            Determine the class name for the given object.
        
            Returns :code:`"null"` if :code:`obj` is :code:`null`.
        
            Parameters:
                obj (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the object to introspect (may be :code:`null`)
        
            Returns:
                the corresponding class name
        
        
        """
        ...
    @staticmethod
    def nullSafeEquals(object: typing.Any, object2: typing.Any) -> bool:
        """
            Determine if the given objects are equal, returning :code:`true` if both are :code:`null` or :code:`false` if only one
            is :code:`null`.
        
            Compares arrays with :code:`Arrays.equals`, performing an equality check based on the array elements rather than the
            array reference.
        
            Parameters:
                o1 (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): first Object to compare
                o2 (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): second Object to compare
        
            Returns:
                whether the given objects are equal
        
            Also see:
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Arrays.html?is-external=true#equals(long%5B%5D,long%5B%5D)>`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(booleanArray: typing.List[bool]) -> int:
        """
            Return as hash code for the given object; typically the value of . If the object is an array, this method will delegate
            to any of the :code:`nullSafeHashCode` methods for arrays in this class. If the object is :code:`null`, this method
            returns 0.
        
            Also see:
                :meth:`~cern.accsoft.commons.util.ObjectUtils.nullSafeHashCode`,
                :meth:`~cern.accsoft.commons.util.ObjectUtils.nullSafeHashCode`,
                :meth:`~cern.accsoft.commons.util.ObjectUtils.nullSafeHashCode`,
                :meth:`~cern.accsoft.commons.util.ObjectUtils.nullSafeHashCode`,
                :meth:`~cern.accsoft.commons.util.ObjectUtils.nullSafeHashCode`,
                :meth:`~cern.accsoft.commons.util.ObjectUtils.nullSafeHashCode`,
                :meth:`~cern.accsoft.commons.util.ObjectUtils.nullSafeHashCode`,
                :meth:`~cern.accsoft.commons.util.ObjectUtils.nullSafeHashCode`,
                :meth:`~cern.accsoft.commons.util.ObjectUtils.nullSafeHashCode`
        
            Return a hash code based on the contents of the specified array. If :code:`array` is :code:`null`, this method returns
            0.
            Return a hash code based on the contents of the specified array. If :code:`array` is :code:`null`, this method returns
            0.
            Return a hash code based on the contents of the specified array. If :code:`array` is :code:`null`, this method returns
            0.
            Return a hash code based on the contents of the specified array. If :code:`array` is :code:`null`, this method returns
            0.
            Return a hash code based on the contents of the specified array. If :code:`array` is :code:`null`, this method returns
            0.
            Return a hash code based on the contents of the specified array. If :code:`array` is :code:`null`, this method returns
            0.
            Return a hash code based on the contents of the specified array. If :code:`array` is :code:`null`, this method returns
            0.
            Return a hash code based on the contents of the specified array. If :code:`array` is :code:`null`, this method returns
            0.
            Return a hash code based on the contents of the specified array. If :code:`array` is :code:`null`, this method returns
            0.
        
        """
        ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(byteArray: typing.List[int]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(charArray: typing.List[str]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(doubleArray: typing.List[float]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(floatArray: typing.List[float]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(intArray: typing.List[int]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(object: typing.Any) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(objectArray: typing.List[typing.Any]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(longArray: typing.List[int]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(shortArray: typing.List[int]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(booleanArray: typing.List[bool]) -> str:
        """
            Return a String representation of the specified Object.
        
            Builds a String representation of the contents in case of an array. Returns :code:`"null"` if :code:`obj` is
            :code:`null`.
        
            Parameters:
                obj (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the object to build a String representation for
        
            Returns:
                a String representation of :code:`obj`
        
            Return a String representation of the contents of the specified array.
        
            The String representation consists of a list of the array's elements, enclosed in curly braces (:code:`"{}"`). Adjacent
            elements are separated by the characters :code:`", "` (a comma followed by a space). Returns :code:`"null"` if
            :code:`array` is :code:`null`.
        
            Parameters:
                array (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`[]): the array to build a String representation for
        
            Returns:
                a String representation of :code:`array`
        
            Return a String representation of the contents of the specified array.
        
            The String representation consists of a list of the array's elements, enclosed in curly braces (:code:`"{}"`). Adjacent
            elements are separated by the characters :code:`", "` (a comma followed by a space). Returns :code:`"null"` if
            :code:`array` is :code:`null`.
        
            Parameters:
                array (boolean[]): the array to build a String representation for
        
            Returns:
                a String representation of :code:`array`
        
            Return a String representation of the contents of the specified array.
        
            The String representation consists of a list of the array's elements, enclosed in curly braces (:code:`"{}"`). Adjacent
            elements are separated by the characters :code:`", "` (a comma followed by a space). Returns :code:`"null"` if
            :code:`array` is :code:`null`.
        
            Parameters:
                array (byte[]): the array to build a String representation for
        
            Returns:
                a String representation of :code:`array`
        
            Return a String representation of the contents of the specified array.
        
            The String representation consists of a list of the array's elements, enclosed in curly braces (:code:`"{}"`). Adjacent
            elements are separated by the characters :code:`", "` (a comma followed by a space). Returns :code:`"null"` if
            :code:`array` is :code:`null`.
        
            Parameters:
                array (char[]): the array to build a String representation for
        
            Returns:
                a String representation of :code:`array`
        
            Return a String representation of the contents of the specified array.
        
            The String representation consists of a list of the array's elements, enclosed in curly braces (:code:`"{}"`). Adjacent
            elements are separated by the characters :code:`", "` (a comma followed by a space). Returns :code:`"null"` if
            :code:`array` is :code:`null`.
        
            Parameters:
                array (double[]): the array to build a String representation for
        
            Returns:
                a String representation of :code:`array`
        
            Return a String representation of the contents of the specified array.
        
            The String representation consists of a list of the array's elements, enclosed in curly braces (:code:`"{}"`). Adjacent
            elements are separated by the characters :code:`", "` (a comma followed by a space). Returns :code:`"null"` if
            :code:`array` is :code:`null`.
        
            Parameters:
                array (float[]): the array to build a String representation for
        
            Returns:
                a String representation of :code:`array`
        
            Return a String representation of the contents of the specified array.
        
            The String representation consists of a list of the array's elements, enclosed in curly braces (:code:`"{}"`). Adjacent
            elements are separated by the characters :code:`", "` (a comma followed by a space). Returns :code:`"null"` if
            :code:`array` is :code:`null`.
        
            Parameters:
                array (int[]): the array to build a String representation for
        
            Returns:
                a String representation of :code:`array`
        
            Return a String representation of the contents of the specified array.
        
            The String representation consists of a list of the array's elements, enclosed in curly braces (:code:`"{}"`). Adjacent
            elements are separated by the characters :code:`", "` (a comma followed by a space). Returns :code:`"null"` if
            :code:`array` is :code:`null`.
        
            Parameters:
                array (long[]): the array to build a String representation for
        
            Returns:
                a String representation of :code:`array`
        
            Return a String representation of the contents of the specified array.
        
            The String representation consists of a list of the array's elements, enclosed in curly braces (:code:`"{}"`). Adjacent
            elements are separated by the characters :code:`", "` (a comma followed by a space). Returns :code:`"null"` if
            :code:`array` is :code:`null`.
        
            Parameters:
                array (short[]): the array to build a String representation for
        
            Returns:
                a String representation of :code:`array`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def nullSafeToString(byteArray: typing.List[int]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(charArray: typing.List[str]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(doubleArray: typing.List[float]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(floatArray: typing.List[float]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(intArray: typing.List[int]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(object: typing.Any) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(objectArray: typing.List[typing.Any]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(longArray: typing.List[int]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(shortArray: typing.List[int]) -> str: ...

class PcropsRepositoryDownloader:
    """
    public class PcropsRepositoryDownloader extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Downloads java classes listed in the first column of a CSV file :code:`LIST_CSV_FILE_NAME` from pcrops repository to a
        folder specified with :code:`DESTINATION`.
    
        The problem: FishEye search engine ignores punctuation characters. However sometimes it is necessary to find an exact
        string (with braces, underscores, exclamation marks, etc.). So FishEye can only pre-filter files. Then the search result
        can be exported to a CSV file and this utility can be used to download the files from release repo for further
        filtering/processing.
    
        If the CSV file contains SVN file paths then use :code:`PcropsRepositoryDownloader.SvnFilePathStrategy` as
        :code:`FILEPATH_STRATEGY`.
    
        If the CSV file contains pcrops repo file paths then use :code:`PcropsRepositoryDownloader.ReleaseRepoFilePathStrategy`
        as :code:`FILEPATH_STRATEGY`.
    
        If a class is missing in pcrops repo it will be ignored (with warning). The files are saved into the destination folder
        into the correct folder hierarchy, ex.:
    
        .. code-block: java
        
         seq\seq-ext-hwc\PRO\src\java\cern\seq\ext\hwc\pm\impl\PostMortemServiceImpl.java
    """
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...

class PcropsRepositoryJnlpSearcher:
    """
    public class PcropsRepositoryJnlpSearcher extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Specialized version of the PcropsRepositoryProductUsageSearcher class which handles only JNLP search.
    
    
        Please adapt product1, product2, version1 variables contents to your own needs and launch this application.
    """
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...

class PcropsRepositoryProductUsageSearcher:
    """
    public class PcropsRepositoryProductUsageSearcher extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Can be used to find products who depend on specified product versions. **It searches the dependencies only inside PRO
        versions of products.**
    
        This class can be only used from Eclipse i.e. command line arguments are not supported (at least at the moment). It is
        meant only for LS1 as later the PCROPS repository won't be used any more.
    """
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...

class ProcessUtils:
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public abstract class ProcessUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Deprecated.
        - use :class:`~cern.accsoft.commons.util.proc.ProcUtils` instead
        Utility methods for Operating System Processes.
    """
    def __init__(self): ...
    @staticmethod
    def getMyPid() -> int: ...
    @staticmethod
    def getMyProcessName() -> str: ...
    @staticmethod
    def getMyShortProcessName() -> str: ...

class ReflectionUtils:
    COPYABLE_FIELDS: typing.ClassVar['ReflectionUtils.FieldFilter'] = ...
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def doWithFields(class_: typing.Type, fieldCallback: 'ReflectionUtils.FieldCallback') -> None: ...
    @typing.overload
    @staticmethod
    def doWithFields(class_: typing.Type, fieldCallback: 'ReflectionUtils.FieldCallback', fieldFilter: 'ReflectionUtils.FieldFilter') -> None: ...
    @typing.overload
    @staticmethod
    def doWithMethods(class_: typing.Type, methodCallback: 'ReflectionUtils.MethodCallback') -> None: ...
    @typing.overload
    @staticmethod
    def doWithMethods(class_: typing.Type, methodCallback: 'ReflectionUtils.MethodCallback', methodFilter: 'ReflectionUtils.MethodFilter') -> None: ...
    @staticmethod
    def findAncestors(class_: typing.Type[typing.Any], list: java.util.List[typing.Type[typing.Any]]) -> None: ...
    @staticmethod
    def findMethod(class_: typing.Type, string: str, classArray: typing.List[typing.Type]) -> java.lang.reflect.Method: ...
    @staticmethod
    def getAllDeclaredMethods(class_: typing.Type) -> typing.List[java.lang.reflect.Method]: ...
    @staticmethod
    def getPropertyValue(object: typing.Any, string: str) -> typing.Any: ...
    @staticmethod
    def handleInvocationTargetException(invocationTargetException: java.lang.reflect.InvocationTargetException) -> None: ...
    @staticmethod
    def handleReflectionException(exception: java.lang.Exception) -> None: ...
    @typing.overload
    @staticmethod
    def invokeMethod(method: java.lang.reflect.Method, object: typing.Any) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def invokeMethod(method: java.lang.reflect.Method, object: typing.Any, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    @staticmethod
    def isFoundOnClassPath(string: str) -> bool: ...
    @staticmethod
    def isPublicStaticFinal(field: java.lang.reflect.Field) -> bool: ...
    @staticmethod
    def makeAccessible(field: java.lang.reflect.Field) -> None: ...
    @staticmethod
    def shallowCopyFieldState(object: typing.Any, object2: typing.Any) -> None: ...
    class FieldCallback:
        def doWith(self, field: java.lang.reflect.Field) -> None: ...
    class FieldFilter:
        def matches(self, field: java.lang.reflect.Field) -> bool: ...
    class MethodCallback:
        def doWith(self, method: java.lang.reflect.Method) -> None: ...
    class MethodFilter:
        def matches(self, method: java.lang.reflect.Method) -> bool: ...

class ResourceUtils:
    """
    public abstract class ResourceUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility methods for resolving resource locations to files in the file system. Mainly for internal use within the
        framework.
    
        Consider using Spring's Resource abstraction in the core package for handling all kinds of file resources in a uniform
        manner. :code:`ResourceLoader`'s :code:`getResource` method can resolve any location to a :code:`Resource` object, which
        in turn allows to obtain a :code:`java.io.File` in the file system through its :code:`getFile()` method.
    
        The main reason for these utility methods for resource location handling is to support :code:`Log4jConfigurer`, which
        must be able to resolve resource locations *before the logging system has been initialized*. Spring' Resource
        abstraction in the core package, on the other hand, already expects the logging system to be available.
    
        Since:
            1.1.5
    
        Also see:
            :code:`Resource`, :code:`ClassPathResource`, :code:`FileSystemResource`, :code:`UrlResource`, :code:`ResourceLoader`
    """
    CLASSPATH_URL_PREFIX: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CLASSPATH_URL_PREFIX
    
        Pseudo URL prefix for loading from the class path: "classpath:"
    
        Also see:
            :meth:`~constant`
    
    
    """
    FILE_URL_PREFIX: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` FILE_URL_PREFIX
    
        URL prefix for loading from the file system: "file:"
    
        Also see:
            :meth:`~constant`
    
    
    """
    URL_PROTOCOL_FILE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` URL_PROTOCOL_FILE
    
        URL protocol for a file in the file system: "file"
    
        Also see:
            :meth:`~constant`
    
    
    """
    URL_PROTOCOL_JAR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` URL_PROTOCOL_JAR
    
        URL protocol for an entry from a jar file: "jar"
    
        Also see:
            :meth:`~constant`
    
    
    """
    URL_PROTOCOL_ZIP: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` URL_PROTOCOL_ZIP
    
        URL protocol for an entry from a zip file: "zip"
    
        Also see:
            :meth:`~constant`
    
    
    """
    URL_PROTOCOL_WSJAR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` URL_PROTOCOL_WSJAR
    
        URL protocol for an entry from a WebSphere jar file: "wsjar"
    
        Also see:
            :meth:`~constant`
    
    
    """
    JAR_URL_SEPARATOR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JAR_URL_SEPARATOR
    
        Separator between JAR URL and file path within the JAR
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    @staticmethod
    def extractJarFileURL(uRL: java.net.URL) -> java.net.URL: ...
    @typing.overload
    @staticmethod
    def getFile(string: str) -> java.io.File: ...
    @typing.overload
    @staticmethod
    def getFile(uRL: java.net.URL) -> java.io.File: ...
    @typing.overload
    @staticmethod
    def getFile(uRL: java.net.URL, string: str) -> java.io.File: ...
    @staticmethod
    def getURL(string: str) -> java.net.URL: ...
    @staticmethod
    def isJarURL(uRL: java.net.URL) -> bool:
        """
            Determine whether the given URL points to a resource in a jar file, that is, has protocol "jar", "zip" or "wsjar".
        
            "zip" and "wsjar" are used by BEA WebLogic Server and IBM WebSphere, respectively, but can be treated like jar files.
        
            Parameters:
                url (`URL <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/net/URL.html?is-external=true>`): the URL to check
        
        
        """
        ...
    @staticmethod
    def isUrl(string: str) -> bool:
        """
            Return whether the given resource location is a URL: either a special "classpath" pseudo URL or a standard URL.
        
            Also see:
                :meth:`~cern.accsoft.commons.util.ResourceUtils.CLASSPATH_URL_PREFIX`, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/net/URL.html?is-external=true>`
        
        
        """
        ...

class SerializationObjectCloner:
    """
    public class SerializationObjectCloner extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class which performs a deep cloning of objects by serializing and de-serializing it.
    
        References to other complex objects contained in the object to clone are then also cloned.
    
        Copied from http://javatechniques.com/blog/faster-deep-copies-of-java-objects.
    """
    def __init__(self): ...
    _deepCopy__T = typing.TypeVar('_deepCopy__T', bound=java.io.Serializable)  # <T>
    @staticmethod
    def deepCopy(t: _deepCopy__T) -> _deepCopy__T: ...

class StringUtils:
    EMPTY_STRING: typing.ClassVar[str] = ...
    EMPTY_STRING_ARRAY: typing.ClassVar[typing.List[str]] = ...
    EMPTY_STRING_ARRAY2D: typing.ClassVar[typing.List[typing.List[str]]] = ...
    def __init__(self): ...
    @staticmethod
    def addStringToArray(stringArray: typing.List[str], string2: str) -> typing.List[str]: ...
    @staticmethod
    def applyRelativePath(string: str, string2: str) -> str: ...
    @staticmethod
    def arrayToCommaDelimitedString(objectArray: typing.List[typing.Any]) -> str: ...
    @staticmethod
    def arrayToDelimitedString(objectArray: typing.List[typing.Any], string: str) -> str: ...
    @staticmethod
    def capitalize(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def center(string: str, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def center(string: str, int: int, char: str) -> str: ...
    @staticmethod
    def cleanPath(string: str) -> str: ...
    @staticmethod
    def collectionToCommaDelimitedString(collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> str: ...
    @typing.overload
    @staticmethod
    def collectionToDelimitedString(collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]], string: str) -> str: ...
    @typing.overload
    @staticmethod
    def collectionToDelimitedString(collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]], string: str, string2: str, string3: str) -> str: ...
    @staticmethod
    def commaDelimitedListToSet(string: str) -> java.util.Set[str]: ...
    @staticmethod
    def commaDelimitedListToStringArray(string: str) -> typing.List[str]: ...
    @staticmethod
    def concatenateStringArrays(stringArray: typing.List[str], stringArray2: typing.List[str]) -> typing.List[str]: ...
    @staticmethod
    def containsAnySubstring(string: str, stringArray: typing.List[str]) -> bool: ...
    @staticmethod
    def containsWhitespace(string: str) -> bool: ...
    @staticmethod
    def countOccurrencesOf(string: str, string2: str) -> int: ...
    @staticmethod
    def delete(string: str, string2: str) -> str: ...
    @staticmethod
    def deleteAny(string: str, string2: str) -> str: ...
    @staticmethod
    def delimitedListToStringArray(string: str, string2: str) -> typing.List[str]: ...
    @staticmethod
    def emptyStringToNull(string: str) -> str: ...
    @staticmethod
    def endsWithIgnoreCase(string: str, string2: str) -> bool: ...
    @staticmethod
    def getFilename(string: str) -> str: ...
    @staticmethod
    def getFilenameExtension(string: str) -> str: ...
    @staticmethod
    def hasLength(string: str) -> bool: ...
    @staticmethod
    def hasText(string: str) -> bool: ...
    @staticmethod
    def mergeStringArrays(stringArray: typing.List[str], stringArray2: typing.List[str]) -> typing.List[str]: ...
    @staticmethod
    def nullToEmptyString(string: str) -> str: ...
    @staticmethod
    def parseLocaleString(string: str) -> java.util.Locale: ...
    @staticmethod
    def pathEquals(string: str, string2: str) -> bool: ...
    @staticmethod
    def quote(string: str) -> str: ...
    @staticmethod
    def quoteIfString(object: typing.Any) -> typing.Any: ...
    @staticmethod
    def removeDuplicateStrings(stringArray: typing.List[str]) -> typing.List[str]: ...
    @staticmethod
    def repeatChar(char: str, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def replace(string: str, string2: str, string3: str) -> str: ...
    @typing.overload
    @staticmethod
    def replace(stringBuilder: java.lang.StringBuilder, string2: str, string3: str, boolean: bool) -> None: ...
    @staticmethod
    def replaceCharsToHTML(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def setStringLength(string: str, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def setStringLength(string: str, int: int, char: str) -> str: ...
    @staticmethod
    def sortStringArray(stringArray: typing.List[str]) -> typing.List[str]: ...
    @staticmethod
    def split(string: str, string2: str) -> typing.List[str]: ...
    @typing.overload
    @staticmethod
    def splitArrayElementsIntoProperties(stringArray: typing.List[str], string2: str) -> java.util.Properties: ...
    @typing.overload
    @staticmethod
    def splitArrayElementsIntoProperties(stringArray: typing.List[str], string2: str, string3: str) -> java.util.Properties: ...
    @staticmethod
    def splitHTMLSentence(string: str, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def splitSentence(string: str, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def splitSentence(string: str, string2: str, int: int) -> str: ...
    @staticmethod
    def startsWithIgnoreCase(string: str, string2: str) -> bool: ...
    @staticmethod
    def stringToHTML(string: str) -> str: ...
    @staticmethod
    def stripFilenameExtension(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def toCamelCase(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def toCamelCase(string: str, firstLetterCapitalization: 'StringUtils.FirstLetterCapitalization') -> str: ...
    @staticmethod
    def toNotNullTrimmedString(string: str) -> str: ...
    @staticmethod
    def toStringArray(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> typing.List[str]: ...
    @typing.overload
    @staticmethod
    def tokenizeToStringArray(string: str, string2: str) -> typing.List[str]: ...
    @typing.overload
    @staticmethod
    def tokenizeToStringArray(string: str, string2: str, boolean: bool, boolean2: bool) -> typing.List[str]: ...
    @staticmethod
    def trimAllWhitespace(string: str) -> str: ...
    @staticmethod
    def trimLeadingWhitespace(string: str) -> str: ...
    @staticmethod
    def trimTrailingWhitespace(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def trimWhitespace(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def trimWhitespace(stringArray: typing.List[str]) -> typing.List[str]: ...
    @staticmethod
    def uncapitalize(string: str) -> str: ...
    @staticmethod
    def underscoreName(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def unqualify(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def unqualify(string: str, char: str) -> str: ...
    class FirstLetterCapitalization(java.lang.Enum['StringUtils.FirstLetterCapitalization']):
        CAPITALIZE_FIRST_LETTER: typing.ClassVar['StringUtils.FirstLetterCapitalization'] = ...
        UNCAPITALIZE_FIRST_LETTER: typing.ClassVar['StringUtils.FirstLetterCapitalization'] = ...
        DO_NOT_CHANGE_FIRST_LETTER: typing.ClassVar['StringUtils.FirstLetterCapitalization'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'StringUtils.FirstLetterCapitalization': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['StringUtils.FirstLetterCapitalization']: ...

class SystemPropertyUtils:
    """
    public abstract class SystemPropertyUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Helper class for resolving placeholders in texts. Usually applied to file paths.
    
        A text may contain :code:`${...}` placeholders, to be resolved as system properties: e.g. :code:`${user.dir}`.
    
        Since:
            1.2.5
    
        Also see:
            :meth:`~cern.accsoft.commons.util.SystemPropertyUtils.PLACEHOLDER_PREFIX`,
            :meth:`~cern.accsoft.commons.util.SystemPropertyUtils.PLACEHOLDER_SUFFIX`, `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/System.html?is-external=true#getProperty(java.lang.String)>`
    """
    PLACEHOLDER_PREFIX: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PLACEHOLDER_PREFIX
    
        Prefix for system property placeholders: "${"
    
        Also see:
            :meth:`~constant`
    
    
    """
    PLACEHOLDER_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PLACEHOLDER_SUFFIX
    
        Suffix for system property placeholders: "}"
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def getBooleanSystemPropertyValue(string: str) -> bool:
        """
            Parses a value of a VM argument or system property as boolean.
        
        
            Resolves "true" and empty string as :code:`true`. The rest, :code:`null` included, is mapped to :code:`false`.
        
        
        
        
            This is useful when using boolean VM arguments or system property without a value, for example:
        
        
            -DdisplayConfiguration (which is a shortcut for -DdisplayConfiguration=true)
        
            Parameters:
                systemProperty (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the VM argument or system property name
        
            Returns:
                a boolean corresponding to the given VM argument or system property name
        
        """
        ...
    @typing.overload
    @staticmethod
    def getBooleanSystemPropertyValue(string: str, boolean: bool) -> bool:
        """
            The `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#getBoolean(java.lang.String)>`
            method is systematically returning false if the given system property argument is not defined. This method is allowing
            you to return true as a default value in this case.
        
            Parameters:
                systemProperty (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The system property name to parse
                defaultValue (boolean): The default boolean value returned if the given system property is not defined or cannot be read.
        
            Returns:
        
        
        """
        ...
    @staticmethod
    def getProperty(stringArray: typing.List[str], string2: str) -> str:
        """
            Returns value of the first property that is set from the specified property names.
        
            Parameters:
                propertyNames (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): names of JVM properties to be scanned
                defaultValue (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): default value returned in case none of the specified properties is set
        
            Returns:
                value of the first property (among specified) that is set (is not :code:`null`)
        
            Also see:
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/System.html?is-external=true#getProperty(java.lang.String)>`
        
        
        """
        ...
    @staticmethod
    def parseBooleanSystemPropertyValue(string: str) -> bool:
        """
            Parses a string coming from a VM argument or system property as boolean.
        
        
            Resolves "true" and empty string as :code:`true`. The rest, :code:`null` included, is mapped to :code:`false`.
        
        
        
        
            This is useful when using boolean VM arguments or system property without a value, for example:
        
        
            -DdisplayConfiguration (which is a shortcut for -DdisplayConfiguration=true)
        
            Parameters:
                systemPropertyValue (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the string associated with the boolean property
        
            Returns:
                a boolean corresponding to the given string
        
        
        """
        ...
    @staticmethod
    def resolvePlaceholders(string: str) -> str:
        """
            Resolve ${...} placeholders in the given text, replacing them with corresponding system property values.
        
            Parameters:
                text (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the String to resolve
        
            Returns:
                the resolved String
        
            Also see:
                :meth:`~cern.accsoft.commons.util.SystemPropertyUtils.PLACEHOLDER_PREFIX`,
                :meth:`~cern.accsoft.commons.util.SystemPropertyUtils.PLACEHOLDER_SUFFIX`
        
        
        """
        ...

class Trace:
    @typing.overload
    def dumpMeasurement(self, outputStream: java.io.OutputStream) -> None: ...
    @typing.overload
    def dumpMeasurement(self, string: str, outputStream: java.io.OutputStream) -> None: ...
    @staticmethod
    def dumpMeasurements(outputStream: java.io.OutputStream) -> None: ...
    @staticmethod
    def getHumanReadableTime(long: int) -> str: ...
    @staticmethod
    def getInstance(string: str) -> 'Trace': ...
    def getName(self) -> str: ...
    @staticmethod
    def isTraceEnabled() -> bool: ...
    @staticmethod
    def printArray(objectArray: typing.List[typing.Any]) -> None: ...
    def printMeasurement(self, boolean: bool, string: str, string2: str, string3: str) -> int: ...
    def printMessage(self, boolean: bool, string: str, string2: str) -> None: ...
    def resetMeasurement(self) -> None: ...
    @staticmethod
    def resetMeasurements() -> None: ...
    @staticmethod
    def setStringLength(string: str, int: int) -> str: ...
    @staticmethod
    def setTraceEnabled(boolean: bool) -> None: ...
    def startMeasurement(self, boolean: bool, string: str, string2: str) -> None: ...

class UnitExponents:
    """
    public final class UnitExponents extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        This class is providing utility methods to easily prefix unit Strings with the proper unit label based on a given
        exponent value:
    
          - UnitExponents.getPrefixedUnits(3, "V") will return "kV".
          - UnitExponents.getPrefixedUnits(-6, "A") will return "ÂµA".
          - UnitExponents.getPrefixedUnits(-12, "W") will return "pW".
          - UnitExponents.getPrefixedUnits(-13, "W") will return "E-13 W".
    
        The normalized SI metric unit prefixes were extracted from :class:`~cern.accsoft.commons.util`.
    """
    @staticmethod
    def getUnit(string: str, int: int) -> str:
        """
        
            Parameters:
                baseUnit (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The base :code:`unit` (e.g. A, V, etc.)
                exponent (int): The :code:`exponent` to parse
        
            Returns:
                The base unit prefixed with the SI prefix corresponding to the given :code:`exponent` list. e.g. mA, kV, etc.
        
                **IMPORTANT** if the given exponent (ex. 16) is not recognized in the :class:`~cern.accsoft.commons.util`, the result
                will be formatted like this: e16 A
        
        
        """
        ...

_AbstractImmutableNamed__N = typing.TypeVar('_AbstractImmutableNamed__N', bound=Named)  # <N>
class AbstractImmutableNamed(Named, java.lang.Comparable[_AbstractImmutableNamed__N], typing.Generic[_AbstractImmutableNamed__N]):
    """
    public abstract class AbstractImmutableNamed<N extends :class:`~cern.accsoft.commons.util.Named`> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.Named`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<N>
    
        Basic implementation of :class:`~cern.accsoft.commons.util.Named` that is immutable.
    """
    def compareTo(self, n: _AbstractImmutableNamed__N) -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.Named.getName`
            Returns the name.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.Named.getName` in interface :class:`~cern.accsoft.commons.util.Named`
        
            Returns:
                the name
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

_AbstractImmutableNamedSerializable__N = typing.TypeVar('_AbstractImmutableNamedSerializable__N', bound=Named)  # <N>
class AbstractImmutableNamedSerializable(Named, java.lang.Comparable[_AbstractImmutableNamedSerializable__N], java.io.Serializable, typing.Generic[_AbstractImmutableNamedSerializable__N]):
    """
    public abstract class AbstractImmutableNamedSerializable<N extends :class:`~cern.accsoft.commons.util.Named`> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.Named`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<N>, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Extension of :class:`~cern.accsoft.commons.util.AbstractNamed` just to provide support of serialization.
    
        Also see:
            :meth:`~serialized`
    """
    def compareTo(self, n: _AbstractImmutableNamedSerializable__N) -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.Named.getName`
            Returns the name.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.Named.getName` in interface :class:`~cern.accsoft.commons.util.Named`
        
            Returns:
                the name
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

_AbstractNamed__N = typing.TypeVar('_AbstractNamed__N', bound=Named)  # <N>
class AbstractNamed(Named, java.lang.Comparable[_AbstractNamed__N], typing.Generic[_AbstractNamed__N]):
    """
    public abstract class AbstractNamed<N extends :class:`~cern.accsoft.commons.util.Named`> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.Named`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<N>
    
        Basic implementation of :class:`~cern.accsoft.commons.util.Named`.
    """
    def compareTo(self, n: _AbstractNamed__N) -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.Named.getName`
            Returns the name.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.Named.getName` in interface :class:`~cern.accsoft.commons.util.Named`
        
            Returns:
                the name
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the new name of this object
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

_AbstractNamedSerializable__N = typing.TypeVar('_AbstractNamedSerializable__N', bound=Named)  # <N>
class AbstractNamedSerializable(Named, java.lang.Comparable[_AbstractNamedSerializable__N], java.io.Serializable, typing.Generic[_AbstractNamedSerializable__N]):
    """
    public abstract class AbstractNamedSerializable<N extends :class:`~cern.accsoft.commons.util.Named`> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.Named`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<N>, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Extension of :class:`~cern.accsoft.commons.util.AbstractNamed` just to provide support of serialization.
    
        Also see:
            :meth:`~serialized`
    """
    def compareTo(self, n: _AbstractNamedSerializable__N) -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.Named.getName`
            Returns the name.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.Named.getName` in interface :class:`~cern.accsoft.commons.util.Named`
        
            Returns:
                the name
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the new name of this object
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

_Filters__Filter__T = typing.TypeVar('_Filters__Filter__T')  # <T>
_Filters__FilterSourceAndDestCollectionHolder__T = typing.TypeVar('_Filters__FilterSourceAndDestCollectionHolder__T')  # <T>
_Filters__FilterSourceAndDestCollectionHolder__D = typing.TypeVar('_Filters__FilterSourceAndDestCollectionHolder__D', bound=java.util.Collection)  # <D>
_Filters__FilterSourceCollectionHolder__T = typing.TypeVar('_Filters__FilterSourceCollectionHolder__T')  # <T>
_Filters__FilterSourceCollectionHolder__C = typing.TypeVar('_Filters__FilterSourceCollectionHolder__C', bound=java.util.Collection)  # <C>
class Filters:
    """
    public class Filters extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        General purpose filter utilities.
    """
    def __init__(self): ...
    _filter_0__T = typing.TypeVar('_filter_0__T')  # <T>
    _filter_1__T = typing.TypeVar('_filter_1__T')  # <T>
    _filter_2__T = typing.TypeVar('_filter_2__T')  # <T>
    @typing.overload
    @staticmethod
    def filter(collection: typing.Union[java.util.Collection[_filter_0__T], typing.Sequence[_filter_0__T]]) -> 'Filters.FilterSourceCollectionHolder'[_filter_0__T, java.util.Collection[_filter_0__T]]: ...
    @typing.overload
    @staticmethod
    def filter(list: java.util.List[_filter_1__T]) -> 'Filters.FilterSourceCollectionHolder'[_filter_1__T, java.util.List[_filter_1__T]]: ...
    @typing.overload
    @staticmethod
    def filter(set: java.util.Set[_filter_2__T]) -> 'Filters.FilterSourceCollectionHolder'[_filter_2__T, java.util.Set[_filter_2__T]]: ...
    class Filter(typing.Generic[_Filters__Filter__T]):
        def accepts(self, t: _Filters__Filter__T) -> bool: ...
    class FilterSourceAndDestCollectionHolder(cern.accsoft.commons.util.Filters.FilterCollectionHolder[_Filters__FilterSourceAndDestCollectionHolder__T, java.util.Collection[_Filters__FilterSourceAndDestCollectionHolder__T], _Filters__FilterSourceAndDestCollectionHolder__D], typing.Generic[_Filters__FilterSourceAndDestCollectionHolder__T, _Filters__FilterSourceAndDestCollectionHolder__D]): ...
    class FilterSourceCollectionHolder(cern.accsoft.commons.util.Filters.FilterCollectionHolder[_Filters__FilterSourceCollectionHolder__T, _Filters__FilterSourceCollectionHolder__C, _Filters__FilterSourceCollectionHolder__C], typing.Generic[_Filters__FilterSourceCollectionHolder__T, _Filters__FilterSourceCollectionHolder__C]):
        _to__D = typing.TypeVar('_to__D', bound=java.util.Collection)  # <D>
        def to(self, d: _to__D) -> 'Filters.FilterSourceAndDestCollectionHolder'[_Filters__FilterSourceCollectionHolder__T, _to__D]: ...
    class FilterCollectionHolder: ...

_Mappers__FlatMapSourceAndDestCollectionHolder__S = typing.TypeVar('_Mappers__FlatMapSourceAndDestCollectionHolder__S')  # <S>
_Mappers__FlatMapSourceAndDestCollectionHolder__D = typing.TypeVar('_Mappers__FlatMapSourceAndDestCollectionHolder__D')  # <D>
_Mappers__FlatMapSourceAndDestCollectionHolder__C = typing.TypeVar('_Mappers__FlatMapSourceAndDestCollectionHolder__C', bound=java.util.Collection)  # <C>
_Mappers__FlatMapSourceCollectionHolder__S = typing.TypeVar('_Mappers__FlatMapSourceCollectionHolder__S')  # <S>
_Mappers__GroupSourceCollectionHolder__S = typing.TypeVar('_Mappers__GroupSourceCollectionHolder__S')  # <S>
_Mappers__GroupSourceCollectionHolder__C = typing.TypeVar('_Mappers__GroupSourceCollectionHolder__C', bound=java.util.Collection)  # <C>
_Mappers__MapBySourceAndDestCollectionHolder__S = typing.TypeVar('_Mappers__MapBySourceAndDestCollectionHolder__S')  # <S>
_Mappers__MapBySourceAndDestCollectionHolder__D = typing.TypeVar('_Mappers__MapBySourceAndDestCollectionHolder__D')  # <D>
_Mappers__MapBySourceAndDestCollectionHolder__M = typing.TypeVar('_Mappers__MapBySourceAndDestCollectionHolder__M', bound=java.util.Map)  # <M>
_Mappers__MapSourceCollectionHolder__S = typing.TypeVar('_Mappers__MapSourceCollectionHolder__S')  # <S>
_Mappers__MapToSourceAndDestCollectionHolder__S = typing.TypeVar('_Mappers__MapToSourceAndDestCollectionHolder__S')  # <S>
_Mappers__MapToSourceAndDestCollectionHolder__D = typing.TypeVar('_Mappers__MapToSourceAndDestCollectionHolder__D')  # <D>
_Mappers__MapToSourceAndDestCollectionHolder__C = typing.TypeVar('_Mappers__MapToSourceAndDestCollectionHolder__C', bound=java.util.Collection)  # <C>
_Mappers__Mapper__S = typing.TypeVar('_Mappers__Mapper__S')  # <S>
_Mappers__Mapper__D = typing.TypeVar('_Mappers__Mapper__D')  # <D>
class Mappers:
    """
    public class Mappers extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        General purpose mapping utilities, to map a collection of items to collection of other items.
    
        Currently supports 3 operations supporting sets, list or general collection:
    
          - Map to a collection: translates each element to a single element which is put into the resulting set or list
          - Flat-map to a collection: translates each element to a collection of elements which are all put into the resulting set
            or list
          - Map by key: translates each element to a unique key pointing to the element itself
          - Group: translates each element to a non-unique key pointing to a collection of elements corresponding to the same key
    """
    def __init__(self): ...
    _flatMap__S = typing.TypeVar('_flatMap__S')  # <S>
    @staticmethod
    def flatMap(collection: typing.Union[java.util.Collection[_flatMap__S], typing.Sequence[_flatMap__S]]) -> 'Mappers.FlatMapSourceCollectionHolder'[_flatMap__S]: ...
    _group_0__S = typing.TypeVar('_group_0__S')  # <S>
    _group_1__S = typing.TypeVar('_group_1__S')  # <S>
    _group_2__S = typing.TypeVar('_group_2__S')  # <S>
    @typing.overload
    @staticmethod
    def group(collection: typing.Union[java.util.Collection[_group_0__S], typing.Sequence[_group_0__S]]) -> 'Mappers.GroupSourceCollectionHolder'[_group_0__S, java.util.Collection[_group_0__S]]: ...
    @typing.overload
    @staticmethod
    def group(list: java.util.List[_group_1__S]) -> 'Mappers.GroupSourceCollectionHolder'[_group_1__S, java.util.List[_group_1__S]]: ...
    @typing.overload
    @staticmethod
    def group(set: java.util.Set[_group_2__S]) -> 'Mappers.GroupSourceCollectionHolder'[_group_2__S, java.util.Set[_group_2__S]]: ...
    _map__S = typing.TypeVar('_map__S')  # <S>
    @staticmethod
    def map(collection: typing.Union[java.util.Collection[_map__S], typing.Sequence[_map__S]]) -> 'Mappers.MapSourceCollectionHolder'[_map__S]: ...
    class FlatMapSourceAndDestCollectionHolder(cern.accsoft.commons.util.Mappers.SourceCollectionHolder[_Mappers__FlatMapSourceAndDestCollectionHolder__S], typing.Generic[_Mappers__FlatMapSourceAndDestCollectionHolder__S, _Mappers__FlatMapSourceAndDestCollectionHolder__D, _Mappers__FlatMapSourceAndDestCollectionHolder__C]):
        def of(self, mapper: 'Mappers.Mapper'[_Mappers__FlatMapSourceAndDestCollectionHolder__S, typing.Union[java.util.Collection[_Mappers__FlatMapSourceAndDestCollectionHolder__D], typing.Sequence[_Mappers__FlatMapSourceAndDestCollectionHolder__D]]]) -> _Mappers__FlatMapSourceAndDestCollectionHolder__C: ...
    class FlatMapSourceCollectionHolder(cern.accsoft.commons.util.Mappers.SourceCollectionHolder[_Mappers__FlatMapSourceCollectionHolder__S], typing.Generic[_Mappers__FlatMapSourceCollectionHolder__S]):
        _to__D = typing.TypeVar('_to__D')  # <D>
        _to__C = typing.TypeVar('_to__C', bound=java.util.Collection)  # <C>
        def to(self, c: _to__C) -> 'Mappers.FlatMapSourceAndDestCollectionHolder'[_Mappers__FlatMapSourceCollectionHolder__S, _to__D, _to__C]: ...
        _toListOf__D = typing.TypeVar('_toListOf__D')  # <D>
        def toListOf(self, mapper: 'Mappers.Mapper'[_Mappers__FlatMapSourceCollectionHolder__S, typing.Union[java.util.Collection[_toListOf__D], typing.Sequence[_toListOf__D]]]) -> java.util.List[_toListOf__D]: ...
        _toSetOf__D = typing.TypeVar('_toSetOf__D')  # <D>
        def toSetOf(self, mapper: 'Mappers.Mapper'[_Mappers__FlatMapSourceCollectionHolder__S, typing.Union[java.util.Collection[_toSetOf__D], typing.Sequence[_toSetOf__D]]]) -> java.util.Set[_toSetOf__D]: ...
    class GroupSourceCollectionHolder(typing.Generic[_Mappers__GroupSourceCollectionHolder__S, _Mappers__GroupSourceCollectionHolder__C]):
        _by__D = typing.TypeVar('_by__D')  # <D>
        def by(self, mapper: 'Mappers.Mapper'[_Mappers__GroupSourceCollectionHolder__S, _by__D]) -> java.util.Map[_by__D, _Mappers__GroupSourceCollectionHolder__C]: ...
    class MapBySourceAndDestCollectionHolder(cern.accsoft.commons.util.Mappers.SourceCollectionHolder[_Mappers__MapBySourceAndDestCollectionHolder__S], typing.Generic[_Mappers__MapBySourceAndDestCollectionHolder__S, _Mappers__MapBySourceAndDestCollectionHolder__D, _Mappers__MapBySourceAndDestCollectionHolder__M]):
        def by(self, mapper: 'Mappers.Mapper'[_Mappers__MapBySourceAndDestCollectionHolder__S, _Mappers__MapBySourceAndDestCollectionHolder__D]) -> _Mappers__MapBySourceAndDestCollectionHolder__M: ...
    class MapSourceCollectionHolder(cern.accsoft.commons.util.Mappers.SourceCollectionHolder[_Mappers__MapSourceCollectionHolder__S], typing.Generic[_Mappers__MapSourceCollectionHolder__S]):
        _by__D = typing.TypeVar('_by__D')  # <D>
        def by(self, mapper: 'Mappers.Mapper'[_Mappers__MapSourceCollectionHolder__S, _by__D]) -> java.util.Map[_by__D, _Mappers__MapSourceCollectionHolder__S]: ...
        _to_0__D = typing.TypeVar('_to_0__D')  # <D>
        _to_0__M = typing.TypeVar('_to_0__M', bound=java.util.Map)  # <M>
        _to_1__D = typing.TypeVar('_to_1__D')  # <D>
        _to_1__C = typing.TypeVar('_to_1__C', bound=java.util.Collection)  # <C>
        @typing.overload
        def to(self, m: _to_0__M) -> 'Mappers.MapBySourceAndDestCollectionHolder'[_Mappers__MapSourceCollectionHolder__S, _to_0__D, _to_0__M]: ...
        @typing.overload
        def to(self, c: _to_1__C) -> 'Mappers.MapToSourceAndDestCollectionHolder'[_Mappers__MapSourceCollectionHolder__S, _to_1__D, _to_1__C]: ...
        _toListOf__D = typing.TypeVar('_toListOf__D')  # <D>
        def toListOf(self, mapper: 'Mappers.Mapper'[_Mappers__MapSourceCollectionHolder__S, _toListOf__D]) -> java.util.List[_toListOf__D]: ...
        _toSetOf__D = typing.TypeVar('_toSetOf__D')  # <D>
        def toSetOf(self, mapper: 'Mappers.Mapper'[_Mappers__MapSourceCollectionHolder__S, _toSetOf__D]) -> java.util.Set[_toSetOf__D]: ...
    class MapToSourceAndDestCollectionHolder(cern.accsoft.commons.util.Mappers.SourceCollectionHolder[_Mappers__MapToSourceAndDestCollectionHolder__S], typing.Generic[_Mappers__MapToSourceAndDestCollectionHolder__S, _Mappers__MapToSourceAndDestCollectionHolder__D, _Mappers__MapToSourceAndDestCollectionHolder__C]):
        def of(self, mapper: 'Mappers.Mapper'[_Mappers__MapToSourceAndDestCollectionHolder__S, _Mappers__MapToSourceAndDestCollectionHolder__D]) -> _Mappers__MapToSourceAndDestCollectionHolder__C: ...
    class Mapper(typing.Generic[_Mappers__Mapper__S, _Mappers__Mapper__D]):
        def map(self, s2: _Mappers__Mapper__S) -> _Mappers__Mapper__D: ...
    class SourceCollectionHolder: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util")``.

    AbstractImmutableNamed: typing.Type[AbstractImmutableNamed]
    AbstractImmutableNamedSerializable: typing.Type[AbstractImmutableNamedSerializable]
    AbstractNamed: typing.Type[AbstractNamed]
    AbstractNamedSerializable: typing.Type[AbstractNamedSerializable]
    AppLauncher: typing.Type[AppLauncher]
    ArrayUtils: typing.Type[ArrayUtils]
    Assert: typing.Type[Assert]
    BeanSupport: typing.Type[BeanSupport]
    BeanUtils: typing.Type[BeanUtils]
    ClassLoaderJarInfo: typing.Type[ClassLoaderJarInfo]
    ClassLoaderUtils: typing.Type[ClassLoaderUtils]
    ClassUtils: typing.Type[ClassUtils]
    ClasspathUtils: typing.Type[ClasspathUtils]
    Cleanable: typing.Type[Cleanable]
    CleanableUtil: typing.Type[CleanableUtil]
    CollectionUtils: typing.Type[CollectionUtils]
    ExceptionUtils: typing.Type[ExceptionUtils]
    FileCopyUtils: typing.Type[FileCopyUtils]
    FileUtils: typing.Type[FileUtils]
    Filters: typing.Type[Filters]
    JarInfo: typing.Type[JarInfo]
    JdkUtils: typing.Type[JdkUtils]
    MapUtils: typing.Type[MapUtils]
    Mappers: typing.Type[Mappers]
    MockitoUtil: typing.Type[MockitoUtil]
    Named: typing.Type[Named]
    Nameds: typing.Type[Nameds]
    NumberUtils: typing.Type[NumberUtils]
    OSUtils: typing.Type[OSUtils]
    ObjectUtils: typing.Type[ObjectUtils]
    PcropsRepositoryDownloader: typing.Type[PcropsRepositoryDownloader]
    PcropsRepositoryJnlpSearcher: typing.Type[PcropsRepositoryJnlpSearcher]
    PcropsRepositoryProductUsageSearcher: typing.Type[PcropsRepositoryProductUsageSearcher]
    ProcessUtils: typing.Type[ProcessUtils]
    ReflectionUtils: typing.Type[ReflectionUtils]
    ResourceUtils: typing.Type[ResourceUtils]
    SerializationObjectCloner: typing.Type[SerializationObjectCloner]
    StringUtils: typing.Type[StringUtils]
    SystemPropertyUtils: typing.Type[SystemPropertyUtils]
    Trace: typing.Type[Trace]
    UnitExponents: typing.Type[UnitExponents]
    annotation: cern.accsoft.commons.util.annotation.__module_protocol__
    collections: cern.accsoft.commons.util.collections.__module_protocol__
    concurrent: cern.accsoft.commons.util.concurrent.__module_protocol__
    enums: cern.accsoft.commons.util.enums.__module_protocol__
    event: cern.accsoft.commons.util.event.__module_protocol__
    executor: cern.accsoft.commons.util.executor.__module_protocol__
    format: cern.accsoft.commons.util.format.__module_protocol__
    jmx: cern.accsoft.commons.util.jmx.__module_protocol__
    mail: cern.accsoft.commons.util.mail.__module_protocol__
    marker: cern.accsoft.commons.util.marker.__module_protocol__
    metric: cern.accsoft.commons.util.metric.__module_protocol__
    proc: cern.accsoft.commons.util.proc.__module_protocol__
    rba: cern.accsoft.commons.util.rba.__module_protocol__
    reflect: cern.accsoft.commons.util.reflect.__module_protocol__
    regexp: cern.accsoft.commons.util.regexp.__module_protocol__
    remoting: cern.accsoft.commons.util.remoting.__module_protocol__
    traceid: cern.accsoft.commons.util.traceid.__module_protocol__
    trigger: cern.accsoft.commons.util.trigger.__module_protocol__
    userctx: cern.accsoft.commons.util.userctx.__module_protocol__
    userinfo: cern.accsoft.commons.util.userinfo.__module_protocol__
    value: cern.accsoft.commons.util.value.__module_protocol__
    xml: cern.accsoft.commons.util.xml.__module_protocol__
