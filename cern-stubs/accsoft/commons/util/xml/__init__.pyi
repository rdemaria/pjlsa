import java.util
import org.w3c.dom
import typing



class DomUtils:
    """
    Java class 'cern.accsoft.commons.util.xml.DomUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * DomUtils()
    
    """
    def __init__(self): ...
    @staticmethod
    def getChildElementByTagName(element: org.w3c.dom.Element, string: str) -> org.w3c.dom.Element: ...
    @staticmethod
    def getChildElementValueByTagName(element: org.w3c.dom.Element, string: str) -> str: ...
    @staticmethod
    def getChildElementsByTagName(element: org.w3c.dom.Element, string: str) -> java.util.List: ...
    @staticmethod
    def getTextValue(element: org.w3c.dom.Element) -> str: ...
    @staticmethod
    def nodeNameEquals(node: org.w3c.dom.Node, string: str) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.xml")``.

    DomUtils: typing.Type[DomUtils]
