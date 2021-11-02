import java.util
import org.w3c.dom
import typing



class DomUtils:
    """
    public abstract class DomUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Convenience methods for working with the DOM API, in particular for working with DOM Nodes and DOM Elements.
    
        Since:
            1.2
    
        Also see:
            `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/org/w3c/dom/Node.html?is-external=true>`, `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/org/w3c/dom/Element.html?is-external=true>`
    """
    def __init__(self): ...
    @staticmethod
    def getChildElementByTagName(element: org.w3c.dom.Element, string: str) -> org.w3c.dom.Element:
        """
            Utility method that returns the first child element identified by its name.
        
            Parameters:
                ele (`Element <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/org/w3c/dom/Element.html?is-external=true>`): the DOM element to analyze
                childEleName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the child element name to look for
        
            Returns:
                the :code:`org.w3c.dom.Element` instance, or :code:`null` if none found
        
        
        """
        ...
    @staticmethod
    def getChildElementValueByTagName(element: org.w3c.dom.Element, string: str) -> str:
        """
            Utility method that returns the first child element value identified by its name.
        
            Parameters:
                ele (`Element <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/org/w3c/dom/Element.html?is-external=true>`): the DOM element to analyze
                childEleName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the child element name to look for
        
            Returns:
                the extracted text value, or :code:`null` if no child element found
        
        
        """
        ...
    @staticmethod
    def getChildElementsByTagName(element: org.w3c.dom.Element, string: str) -> java.util.List:
        """
            Retrieve all child elements of the given DOM element that match the given element name. Only look at the direct child
            level of the given element; do not go into further depth (in contrast to the DOM API's :code:`getElementsByTagName`
            method).
        
            Parameters:
                ele (`Element <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/org/w3c/dom/Element.html?is-external=true>`): the DOM element to analyze
                childEleName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the child element name to look for
        
            Returns:
                a List of child :code:`org.w3c.dom.Element` instances
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/org/w3c/dom/Element.html?is-external=true>`, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/org/w3c/dom/Element.html?is-external=true#getElementsByTagName(java.lang.String)>`
        
        
        """
        ...
    @staticmethod
    def getTextValue(element: org.w3c.dom.Element) -> str:
        """
            Extract the text value from the given DOM element, ignoring XML comments.
        
            Appends all CharacterData nodes and EntityReference nodes into a single String value, excluding Comment nodes.
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/org/w3c/dom/CharacterData.html?is-external=true>`, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/org/w3c/dom/EntityReference.html?is-external=true>`, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/org/w3c/dom/Comment.html?is-external=true>`
        
        
        """
        ...
    @staticmethod
    def nodeNameEquals(node: org.w3c.dom.Node, string: str) -> bool:
        """
            Namespace-aware equals comparison. Returns :code:`true` if either `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/org/w3c/dom/Node.html?is-external=true#getLocalName()>` or `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/org/w3c/dom/Node.html?is-external=true#getNodeName()>` equals
            :code:`desiredName`, otherwise returns :code:`false`.
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.xml")``.

    DomUtils: typing.Type[DomUtils]
