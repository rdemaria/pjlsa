from typing import Any as _py_Any
from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import overload
import java.awt
import java.awt.geom
import java.io
import java.lang
import java.text
import java.util
import sun.font


class CharArrayIterator(java.text.CharacterIterator):
    def clone(self) -> _py_Any: ...
    def current(self) -> str: ...
    def first(self) -> str: ...
    def getBeginIndex(self) -> int: ...
    def getEndIndex(self) -> int: ...
    def getIndex(self) -> int: ...
    def last(self) -> str: ...
    def next(self) -> str: ...
    def previous(self) -> str: ...
    def setIndex(self, int: int) -> str: ...

class FontRenderContext:
    @overload
    def __init__(self, affineTransform: java.awt.geom.AffineTransform, boolean: bool, boolean2: bool): ...
    @overload
    def __init__(self, affineTransform: java.awt.geom.AffineTransform, object: _py_Any, object2: _py_Any): ...
    @overload
    def equals(self, fontRenderContext: 'FontRenderContext') -> bool: ...
    @overload
    def equals(self, object: _py_Any) -> bool: ...
    def getAntiAliasingHint(self) -> _py_Any: ...
    def getFractionalMetricsHint(self) -> _py_Any: ...
    def getTransform(self) -> java.awt.geom.AffineTransform: ...
    def getTransformType(self) -> int: ...
    def hashCode(self) -> int: ...
    def isAntiAliased(self) -> bool: ...
    def isTransformed(self) -> bool: ...
    def usesFractionalMetrics(self) -> bool: ...

class GlyphJustificationInfo:
    PRIORITY_KASHIDA: _py_ClassVar[int] = ...
    PRIORITY_WHITESPACE: _py_ClassVar[int] = ...
    PRIORITY_INTERCHAR: _py_ClassVar[int] = ...
    PRIORITY_NONE: _py_ClassVar[int] = ...
    weight: float = ...
    growPriority: int = ...
    growAbsorb: bool = ...
    growLeftLimit: float = ...
    growRightLimit: float = ...
    shrinkPriority: int = ...
    shrinkAbsorb: bool = ...
    shrinkLeftLimit: float = ...
    shrinkRightLimit: float = ...
    def __init__(self, float: float, boolean: bool, int: int, float2: float, float3: float, boolean2: bool, int2: int, float4: float, float5: float): ...

class GlyphMetrics:
    STANDARD: _py_ClassVar[int] = ...
    LIGATURE: _py_ClassVar[int] = ...
    COMBINING: _py_ClassVar[int] = ...
    COMPONENT: _py_ClassVar[int] = ...
    WHITESPACE: _py_ClassVar[int] = ...
    @overload
    def __init__(self, boolean: bool, float: float, float2: float, rectangle2D: java.awt.geom.Rectangle2D, byte: int): ...
    @overload
    def __init__(self, float: float, rectangle2D: java.awt.geom.Rectangle2D, byte: int): ...
    def getAdvance(self) -> float: ...
    def getAdvanceX(self) -> float: ...
    def getAdvanceY(self) -> float: ...
    def getBounds2D(self) -> java.awt.geom.Rectangle2D: ...
    def getLSB(self) -> float: ...
    def getRSB(self) -> float: ...
    def getType(self) -> int: ...
    def isCombining(self) -> bool: ...
    def isComponent(self) -> bool: ...
    def isLigature(self) -> bool: ...
    def isStandard(self) -> bool: ...
    def isWhitespace(self) -> bool: ...

class GlyphVector(java.lang.Cloneable):
    FLAG_HAS_TRANSFORMS: _py_ClassVar[int] = ...
    FLAG_HAS_POSITION_ADJUSTMENTS: _py_ClassVar[int] = ...
    FLAG_RUN_RTL: _py_ClassVar[int] = ...
    FLAG_COMPLEX_GLYPHS: _py_ClassVar[int] = ...
    FLAG_MASK: _py_ClassVar[int] = ...
    def __init__(self): ...
    @overload
    def equals(self, glyphVector: 'GlyphVector') -> bool: ...
    @overload
    def equals(self, object: _py_Any) -> bool: ...
    def getFont(self) -> java.awt.Font: ...
    def getFontRenderContext(self) -> FontRenderContext: ...
    def getGlyphCharIndex(self, int: int) -> int: ...
    def getGlyphCharIndices(self, int: int, int2: int, intArray: _py_List[int]) -> _py_List[int]: ...
    def getGlyphCode(self, int: int) -> int: ...
    def getGlyphCodes(self, int: int, int2: int, intArray: _py_List[int]) -> _py_List[int]: ...
    def getGlyphJustificationInfo(self, int: int) -> GlyphJustificationInfo: ...
    def getGlyphLogicalBounds(self, int: int) -> java.awt.Shape: ...
    def getGlyphMetrics(self, int: int) -> GlyphMetrics: ...
    @overload
    def getGlyphOutline(self, int: int) -> java.awt.Shape: ...
    @overload
    def getGlyphOutline(self, int: int, float: float, float2: float) -> java.awt.Shape: ...
    def getGlyphPixelBounds(self, int: int, fontRenderContext: FontRenderContext, float: float, float2: float) -> java.awt.Rectangle: ...
    def getGlyphPosition(self, int: int) -> java.awt.geom.Point2D: ...
    def getGlyphPositions(self, int: int, int2: int, floatArray: _py_List[float]) -> _py_List[float]: ...
    def getGlyphTransform(self, int: int) -> java.awt.geom.AffineTransform: ...
    def getGlyphVisualBounds(self, int: int) -> java.awt.Shape: ...
    def getLayoutFlags(self) -> int: ...
    def getLogicalBounds(self) -> java.awt.geom.Rectangle2D: ...
    def getNumGlyphs(self) -> int: ...
    @overload
    def getOutline(self) -> java.awt.Shape: ...
    @overload
    def getOutline(self, float: float, float2: float) -> java.awt.Shape: ...
    def getPixelBounds(self, fontRenderContext: FontRenderContext, float: float, float2: float) -> java.awt.Rectangle: ...
    def getVisualBounds(self) -> java.awt.geom.Rectangle2D: ...
    def performDefaultLayout(self) -> None: ...
    def setGlyphPosition(self, int: int, point2D: java.awt.geom.Point2D) -> None: ...
    def setGlyphTransform(self, int: int, affineTransform: java.awt.geom.AffineTransform) -> None: ...

class GraphicAttribute:
    TOP_ALIGNMENT: _py_ClassVar[int] = ...
    BOTTOM_ALIGNMENT: _py_ClassVar[int] = ...
    ROMAN_BASELINE: _py_ClassVar[int] = ...
    CENTER_BASELINE: _py_ClassVar[int] = ...
    HANGING_BASELINE: _py_ClassVar[int] = ...
    def draw(self, graphics2D: java.awt.Graphics2D, float: float, float2: float) -> None: ...
    def getAdvance(self) -> float: ...
    def getAlignment(self) -> int: ...
    def getAscent(self) -> float: ...
    def getBounds(self) -> java.awt.geom.Rectangle2D: ...
    def getDescent(self) -> float: ...
    def getJustificationInfo(self) -> GlyphJustificationInfo: ...
    def getOutline(self, affineTransform: java.awt.geom.AffineTransform) -> java.awt.Shape: ...

class LayoutPath:
    def __init__(self): ...
    def pathToPoint(self, point2D: java.awt.geom.Point2D, boolean: bool, point2D2: java.awt.geom.Point2D) -> None: ...
    def pointToPath(self, point2D: java.awt.geom.Point2D, point2D2: java.awt.geom.Point2D) -> bool: ...

class LineBreakMeasurer:
    @overload
    def __init__(self, attributedCharacterIterator: java.text.AttributedCharacterIterator, fontRenderContext: FontRenderContext): ...
    @overload
    def __init__(self, attributedCharacterIterator: java.text.AttributedCharacterIterator, breakIterator: java.text.BreakIterator, fontRenderContext: FontRenderContext): ...
    def deleteChar(self, attributedCharacterIterator: java.text.AttributedCharacterIterator, int: int) -> None: ...
    def getPosition(self) -> int: ...
    def insertChar(self, attributedCharacterIterator: java.text.AttributedCharacterIterator, int: int) -> None: ...
    @overload
    def nextLayout(self, float: float) -> 'TextLayout': ...
    @overload
    def nextLayout(self, float: float, int: int, boolean: bool) -> 'TextLayout': ...
    @overload
    def nextOffset(self, float: float) -> int: ...
    @overload
    def nextOffset(self, float: float, int: int, boolean: bool) -> int: ...
    def setPosition(self, int: int) -> None: ...

class LineMetrics:
    def __init__(self): ...
    def getAscent(self) -> float: ...
    def getBaselineIndex(self) -> int: ...
    def getBaselineOffsets(self) -> _py_List[float]: ...
    def getDescent(self) -> float: ...
    def getHeight(self) -> float: ...
    def getLeading(self) -> float: ...
    def getNumChars(self) -> int: ...
    def getStrikethroughOffset(self) -> float: ...
    def getStrikethroughThickness(self) -> float: ...
    def getUnderlineOffset(self) -> float: ...
    def getUnderlineThickness(self) -> float: ...

class MultipleMaster:
    @overload
    def deriveMMFont(self, floatArray: _py_List[float]) -> java.awt.Font: ...
    @overload
    def deriveMMFont(self, floatArray: _py_List[float], float2: float, float3: float, float4: float, float5: float) -> java.awt.Font: ...
    def getDesignAxisDefaults(self) -> _py_List[float]: ...
    def getDesignAxisNames(self) -> _py_List[str]: ...
    def getDesignAxisRanges(self) -> _py_List[float]: ...
    def getNumDesignAxes(self) -> int: ...

class NumericShaper(java.io.Serializable):
    EUROPEAN: _py_ClassVar[int] = ...
    ARABIC: _py_ClassVar[int] = ...
    EASTERN_ARABIC: _py_ClassVar[int] = ...
    DEVANAGARI: _py_ClassVar[int] = ...
    BENGALI: _py_ClassVar[int] = ...
    GURMUKHI: _py_ClassVar[int] = ...
    GUJARATI: _py_ClassVar[int] = ...
    ORIYA: _py_ClassVar[int] = ...
    TAMIL: _py_ClassVar[int] = ...
    TELUGU: _py_ClassVar[int] = ...
    KANNADA: _py_ClassVar[int] = ...
    MALAYALAM: _py_ClassVar[int] = ...
    THAI: _py_ClassVar[int] = ...
    LAO: _py_ClassVar[int] = ...
    TIBETAN: _py_ClassVar[int] = ...
    MYANMAR: _py_ClassVar[int] = ...
    ETHIOPIC: _py_ClassVar[int] = ...
    KHMER: _py_ClassVar[int] = ...
    MONGOLIAN: _py_ClassVar[int] = ...
    ALL_RANGES: _py_ClassVar[int] = ...
    def equals(self, object: _py_Any) -> bool: ...
    @classmethod
    @overload
    def getContextualShaper(cls, int: int) -> 'NumericShaper': ...
    @classmethod
    @overload
    def getContextualShaper(cls, int: int, int2: int) -> 'NumericShaper': ...
    @classmethod
    @overload
    def getContextualShaper(cls, set: java.util.Set['NumericShaper.Range']) -> 'NumericShaper': ...
    @classmethod
    @overload
    def getContextualShaper(cls, set: java.util.Set['NumericShaper.Range'], range: 'NumericShaper.Range') -> 'NumericShaper': ...
    def getRangeSet(self) -> java.util.Set['NumericShaper.Range']: ...
    def getRanges(self) -> int: ...
    @classmethod
    @overload
    def getShaper(cls, int: int) -> 'NumericShaper': ...
    @classmethod
    @overload
    def getShaper(cls, range: 'NumericShaper.Range') -> 'NumericShaper': ...
    def hashCode(self) -> int: ...
    def isContextual(self) -> bool: ...
    @overload
    def shape(self, charArray: _py_List[str], int: int, int2: int) -> None: ...
    @overload
    def shape(self, charArray: _py_List[str], int: int, int2: int, int3: int) -> None: ...
    @overload
    def shape(self, charArray: _py_List[str], int: int, int2: int, range: 'NumericShaper.Range') -> None: ...
    def toString(self) -> str: ...
    class Range(java.lang.Enum['NumericShaper.Range']):
        EUROPEAN: _py_ClassVar['NumericShaper.Range'] = ...
        ARABIC: _py_ClassVar['NumericShaper.Range'] = ...
        EASTERN_ARABIC: _py_ClassVar['NumericShaper.Range'] = ...
        DEVANAGARI: _py_ClassVar['NumericShaper.Range'] = ...
        BENGALI: _py_ClassVar['NumericShaper.Range'] = ...
        GURMUKHI: _py_ClassVar['NumericShaper.Range'] = ...
        GUJARATI: _py_ClassVar['NumericShaper.Range'] = ...
        ORIYA: _py_ClassVar['NumericShaper.Range'] = ...
        TAMIL: _py_ClassVar['NumericShaper.Range'] = ...
        TELUGU: _py_ClassVar['NumericShaper.Range'] = ...
        KANNADA: _py_ClassVar['NumericShaper.Range'] = ...
        MALAYALAM: _py_ClassVar['NumericShaper.Range'] = ...
        THAI: _py_ClassVar['NumericShaper.Range'] = ...
        LAO: _py_ClassVar['NumericShaper.Range'] = ...
        TIBETAN: _py_ClassVar['NumericShaper.Range'] = ...
        MYANMAR: _py_ClassVar['NumericShaper.Range'] = ...
        ETHIOPIC: _py_ClassVar['NumericShaper.Range'] = ...
        KHMER: _py_ClassVar['NumericShaper.Range'] = ...
        MONGOLIAN: _py_ClassVar['NumericShaper.Range'] = ...
        NKO: _py_ClassVar['NumericShaper.Range'] = ...
        MYANMAR_SHAN: _py_ClassVar['NumericShaper.Range'] = ...
        LIMBU: _py_ClassVar['NumericShaper.Range'] = ...
        NEW_TAI_LUE: _py_ClassVar['NumericShaper.Range'] = ...
        BALINESE: _py_ClassVar['NumericShaper.Range'] = ...
        SUNDANESE: _py_ClassVar['NumericShaper.Range'] = ...
        LEPCHA: _py_ClassVar['NumericShaper.Range'] = ...
        OL_CHIKI: _py_ClassVar['NumericShaper.Range'] = ...
        VAI: _py_ClassVar['NumericShaper.Range'] = ...
        SAURASHTRA: _py_ClassVar['NumericShaper.Range'] = ...
        KAYAH_LI: _py_ClassVar['NumericShaper.Range'] = ...
        CHAM: _py_ClassVar['NumericShaper.Range'] = ...
        TAI_THAM_HORA: _py_ClassVar['NumericShaper.Range'] = ...
        TAI_THAM_THAM: _py_ClassVar['NumericShaper.Range'] = ...
        JAVANESE: _py_ClassVar['NumericShaper.Range'] = ...
        MEETEI_MAYEK: _py_ClassVar['NumericShaper.Range'] = ...
        @classmethod
        @overload
        def valueOf(cls, string: str) -> 'NumericShaper.Range': ...
        _valueOf_1__T = _py_TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @overload
        def valueOf(cls, class_: _py_Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @classmethod
        def values(cls) -> _py_List['NumericShaper.Range']: ...

class OpenType:
    TAG_CMAP: _py_ClassVar[int] = ...
    TAG_HEAD: _py_ClassVar[int] = ...
    TAG_NAME: _py_ClassVar[int] = ...
    TAG_GLYF: _py_ClassVar[int] = ...
    TAG_MAXP: _py_ClassVar[int] = ...
    TAG_PREP: _py_ClassVar[int] = ...
    TAG_HMTX: _py_ClassVar[int] = ...
    TAG_KERN: _py_ClassVar[int] = ...
    TAG_HDMX: _py_ClassVar[int] = ...
    TAG_LOCA: _py_ClassVar[int] = ...
    TAG_POST: _py_ClassVar[int] = ...
    TAG_OS2: _py_ClassVar[int] = ...
    TAG_CVT: _py_ClassVar[int] = ...
    TAG_GASP: _py_ClassVar[int] = ...
    TAG_VDMX: _py_ClassVar[int] = ...
    TAG_VMTX: _py_ClassVar[int] = ...
    TAG_VHEA: _py_ClassVar[int] = ...
    TAG_HHEA: _py_ClassVar[int] = ...
    TAG_TYP1: _py_ClassVar[int] = ...
    TAG_BSLN: _py_ClassVar[int] = ...
    TAG_GSUB: _py_ClassVar[int] = ...
    TAG_DSIG: _py_ClassVar[int] = ...
    TAG_FPGM: _py_ClassVar[int] = ...
    TAG_FVAR: _py_ClassVar[int] = ...
    TAG_GVAR: _py_ClassVar[int] = ...
    TAG_CFF: _py_ClassVar[int] = ...
    TAG_MMSD: _py_ClassVar[int] = ...
    TAG_MMFX: _py_ClassVar[int] = ...
    TAG_BASE: _py_ClassVar[int] = ...
    TAG_GDEF: _py_ClassVar[int] = ...
    TAG_GPOS: _py_ClassVar[int] = ...
    TAG_JSTF: _py_ClassVar[int] = ...
    TAG_EBDT: _py_ClassVar[int] = ...
    TAG_EBLC: _py_ClassVar[int] = ...
    TAG_EBSC: _py_ClassVar[int] = ...
    TAG_LTSH: _py_ClassVar[int] = ...
    TAG_PCLT: _py_ClassVar[int] = ...
    TAG_ACNT: _py_ClassVar[int] = ...
    TAG_AVAR: _py_ClassVar[int] = ...
    TAG_BDAT: _py_ClassVar[int] = ...
    TAG_BLOC: _py_ClassVar[int] = ...
    TAG_CVAR: _py_ClassVar[int] = ...
    TAG_FEAT: _py_ClassVar[int] = ...
    TAG_FDSC: _py_ClassVar[int] = ...
    TAG_FMTX: _py_ClassVar[int] = ...
    TAG_JUST: _py_ClassVar[int] = ...
    TAG_LCAR: _py_ClassVar[int] = ...
    TAG_MORT: _py_ClassVar[int] = ...
    TAG_OPBD: _py_ClassVar[int] = ...
    TAG_PROP: _py_ClassVar[int] = ...
    TAG_TRAK: _py_ClassVar[int] = ...
    @overload
    def getFontTable(self, int: int) -> _py_List[int]: ...
    @overload
    def getFontTable(self, int: int, int2: int, int3: int) -> _py_List[int]: ...
    @overload
    def getFontTable(self, string: str) -> _py_List[int]: ...
    @overload
    def getFontTable(self, string: str, int: int, int2: int) -> _py_List[int]: ...
    @overload
    def getFontTableSize(self, int: int) -> int: ...
    @overload
    def getFontTableSize(self, string: str) -> int: ...
    def getVersion(self) -> int: ...

class StyledParagraph:
    def __init__(self, attributedCharacterIterator: java.text.AttributedCharacterIterator, charArray: _py_List[str]): ...
    @classmethod
    def deleteChar(cls, attributedCharacterIterator: java.text.AttributedCharacterIterator, charArray: _py_List[str], int: int, styledParagraph: 'StyledParagraph') -> 'StyledParagraph': ...
    def getDecorationAt(self, int: int) -> sun.font.Decoration: ...
    def getFontOrGraphicAt(self, int: int) -> _py_Any: ...
    def getRunLimit(self, int: int) -> int: ...
    @classmethod
    def insertChar(cls, attributedCharacterIterator: java.text.AttributedCharacterIterator, charArray: _py_List[str], int: int, styledParagraph: 'StyledParagraph') -> 'StyledParagraph': ...

class TextAttribute(java.text.AttributedCharacterIterator.Attribute):
    FAMILY: _py_ClassVar['TextAttribute'] = ...
    WEIGHT: _py_ClassVar['TextAttribute'] = ...
    WEIGHT_EXTRA_LIGHT: _py_ClassVar[float] = ...
    WEIGHT_LIGHT: _py_ClassVar[float] = ...
    WEIGHT_DEMILIGHT: _py_ClassVar[float] = ...
    WEIGHT_REGULAR: _py_ClassVar[float] = ...
    WEIGHT_SEMIBOLD: _py_ClassVar[float] = ...
    WEIGHT_MEDIUM: _py_ClassVar[float] = ...
    WEIGHT_DEMIBOLD: _py_ClassVar[float] = ...
    WEIGHT_BOLD: _py_ClassVar[float] = ...
    WEIGHT_HEAVY: _py_ClassVar[float] = ...
    WEIGHT_EXTRABOLD: _py_ClassVar[float] = ...
    WEIGHT_ULTRABOLD: _py_ClassVar[float] = ...
    WIDTH: _py_ClassVar['TextAttribute'] = ...
    WIDTH_CONDENSED: _py_ClassVar[float] = ...
    WIDTH_SEMI_CONDENSED: _py_ClassVar[float] = ...
    WIDTH_REGULAR: _py_ClassVar[float] = ...
    WIDTH_SEMI_EXTENDED: _py_ClassVar[float] = ...
    WIDTH_EXTENDED: _py_ClassVar[float] = ...
    POSTURE: _py_ClassVar['TextAttribute'] = ...
    POSTURE_REGULAR: _py_ClassVar[float] = ...
    POSTURE_OBLIQUE: _py_ClassVar[float] = ...
    SIZE: _py_ClassVar['TextAttribute'] = ...
    TRANSFORM: _py_ClassVar['TextAttribute'] = ...
    SUPERSCRIPT: _py_ClassVar['TextAttribute'] = ...
    SUPERSCRIPT_SUPER: _py_ClassVar[int] = ...
    SUPERSCRIPT_SUB: _py_ClassVar[int] = ...
    FONT: _py_ClassVar['TextAttribute'] = ...
    CHAR_REPLACEMENT: _py_ClassVar['TextAttribute'] = ...
    FOREGROUND: _py_ClassVar['TextAttribute'] = ...
    BACKGROUND: _py_ClassVar['TextAttribute'] = ...
    UNDERLINE: _py_ClassVar['TextAttribute'] = ...
    UNDERLINE_ON: _py_ClassVar[int] = ...
    STRIKETHROUGH: _py_ClassVar['TextAttribute'] = ...
    STRIKETHROUGH_ON: _py_ClassVar[bool] = ...
    RUN_DIRECTION: _py_ClassVar['TextAttribute'] = ...
    RUN_DIRECTION_LTR: _py_ClassVar[bool] = ...
    RUN_DIRECTION_RTL: _py_ClassVar[bool] = ...
    BIDI_EMBEDDING: _py_ClassVar['TextAttribute'] = ...
    JUSTIFICATION: _py_ClassVar['TextAttribute'] = ...
    JUSTIFICATION_FULL: _py_ClassVar[float] = ...
    JUSTIFICATION_NONE: _py_ClassVar[float] = ...
    INPUT_METHOD_HIGHLIGHT: _py_ClassVar['TextAttribute'] = ...
    INPUT_METHOD_UNDERLINE: _py_ClassVar['TextAttribute'] = ...
    UNDERLINE_LOW_ONE_PIXEL: _py_ClassVar[int] = ...
    UNDERLINE_LOW_TWO_PIXEL: _py_ClassVar[int] = ...
    UNDERLINE_LOW_DOTTED: _py_ClassVar[int] = ...
    UNDERLINE_LOW_GRAY: _py_ClassVar[int] = ...
    UNDERLINE_LOW_DASHED: _py_ClassVar[int] = ...
    SWAP_COLORS: _py_ClassVar['TextAttribute'] = ...
    SWAP_COLORS_ON: _py_ClassVar[bool] = ...
    NUMERIC_SHAPING: _py_ClassVar['TextAttribute'] = ...
    KERNING: _py_ClassVar['TextAttribute'] = ...
    KERNING_ON: _py_ClassVar[int] = ...
    LIGATURES: _py_ClassVar['TextAttribute'] = ...
    LIGATURES_ON: _py_ClassVar[int] = ...
    TRACKING: _py_ClassVar['TextAttribute'] = ...
    TRACKING_TIGHT: _py_ClassVar[float] = ...
    TRACKING_LOOSE: _py_ClassVar[float] = ...

class TextHitInfo:
    @classmethod
    def afterOffset(cls, int: int) -> 'TextHitInfo': ...
    @classmethod
    def beforeOffset(cls, int: int) -> 'TextHitInfo': ...
    @overload
    def equals(self, textHitInfo: 'TextHitInfo') -> bool: ...
    @overload
    def equals(self, object: _py_Any) -> bool: ...
    def getCharIndex(self) -> int: ...
    def getInsertionIndex(self) -> int: ...
    def getOffsetHit(self, int: int) -> 'TextHitInfo': ...
    def getOtherHit(self) -> 'TextHitInfo': ...
    def hashCode(self) -> int: ...
    def isLeadingEdge(self) -> bool: ...
    @classmethod
    def leading(cls, int: int) -> 'TextHitInfo': ...
    def toString(self) -> str: ...
    @classmethod
    def trailing(cls, int: int) -> 'TextHitInfo': ...

class TextJustifier:
    MAX_PRIORITY: _py_ClassVar[int] = ...
    def justify(self, float: float) -> _py_List[float]: ...

class TextLayout(java.lang.Cloneable):
    DEFAULT_CARET_POLICY: _py_ClassVar['TextLayout.CaretPolicy'] = ...
    @overload
    def __init__(self, string: str, font: java.awt.Font, fontRenderContext: FontRenderContext): ...
    @overload
    def __init__(self, string: str, map: java.util.Map[java.text.AttributedCharacterIterator.Attribute, _py_Any], fontRenderContext: FontRenderContext): ...
    @overload
    def __init__(self, attributedCharacterIterator: java.text.AttributedCharacterIterator, fontRenderContext: FontRenderContext): ...
    def draw(self, graphics2D: java.awt.Graphics2D, float: float, float2: float) -> None: ...
    @overload
    def equals(self, textLayout: 'TextLayout') -> bool: ...
    @overload
    def equals(self, object: _py_Any) -> bool: ...
    def getAdvance(self) -> float: ...
    def getAscent(self) -> float: ...
    def getBaseline(self) -> int: ...
    def getBaselineOffsets(self) -> _py_List[float]: ...
    def getBlackBoxBounds(self, int: int, int2: int) -> java.awt.Shape: ...
    def getBounds(self) -> java.awt.geom.Rectangle2D: ...
    @overload
    def getCaretInfo(self, textHitInfo: TextHitInfo) -> _py_List[float]: ...
    @overload
    def getCaretInfo(self, textHitInfo: TextHitInfo, rectangle2D: java.awt.geom.Rectangle2D) -> _py_List[float]: ...
    @overload
    def getCaretShape(self, textHitInfo: TextHitInfo) -> java.awt.Shape: ...
    @overload
    def getCaretShape(self, textHitInfo: TextHitInfo, rectangle2D: java.awt.geom.Rectangle2D) -> java.awt.Shape: ...
    @overload
    def getCaretShapes(self, int: int) -> _py_List[java.awt.Shape]: ...
    @overload
    def getCaretShapes(self, int: int, rectangle2D: java.awt.geom.Rectangle2D) -> _py_List[java.awt.Shape]: ...
    @overload
    def getCaretShapes(self, int: int, rectangle2D: java.awt.geom.Rectangle2D, caretPolicy: 'TextLayout.CaretPolicy') -> _py_List[java.awt.Shape]: ...
    def getCharacterCount(self) -> int: ...
    def getCharacterLevel(self, int: int) -> int: ...
    def getDescent(self) -> float: ...
    def getJustifiedLayout(self, float: float) -> 'TextLayout': ...
    def getLayoutPath(self) -> LayoutPath: ...
    def getLeading(self) -> float: ...
    @overload
    def getLogicalHighlightShape(self, int: int, int2: int) -> java.awt.Shape: ...
    @overload
    def getLogicalHighlightShape(self, int: int, int2: int, rectangle2D: java.awt.geom.Rectangle2D) -> java.awt.Shape: ...
    def getLogicalRangesForVisualSelection(self, textHitInfo: TextHitInfo, textHitInfo2: TextHitInfo) -> _py_List[int]: ...
    @overload
    def getNextLeftHit(self, int: int) -> TextHitInfo: ...
    @overload
    def getNextLeftHit(self, int: int, caretPolicy: 'TextLayout.CaretPolicy') -> TextHitInfo: ...
    @overload
    def getNextLeftHit(self, textHitInfo: TextHitInfo) -> TextHitInfo: ...
    @overload
    def getNextRightHit(self, int: int) -> TextHitInfo: ...
    @overload
    def getNextRightHit(self, int: int, caretPolicy: 'TextLayout.CaretPolicy') -> TextHitInfo: ...
    @overload
    def getNextRightHit(self, textHitInfo: TextHitInfo) -> TextHitInfo: ...
    def getOutline(self, affineTransform: java.awt.geom.AffineTransform) -> java.awt.Shape: ...
    def getPixelBounds(self, fontRenderContext: FontRenderContext, float: float, float2: float) -> java.awt.Rectangle: ...
    def getVisibleAdvance(self) -> float: ...
    @overload
    def getVisualHighlightShape(self, textHitInfo: TextHitInfo, textHitInfo2: TextHitInfo) -> java.awt.Shape: ...
    @overload
    def getVisualHighlightShape(self, textHitInfo: TextHitInfo, textHitInfo2: TextHitInfo, rectangle2D: java.awt.geom.Rectangle2D) -> java.awt.Shape: ...
    def getVisualOtherHit(self, textHitInfo: TextHitInfo) -> TextHitInfo: ...
    def hashCode(self) -> int: ...
    @overload
    def hitTestChar(self, float: float, float2: float) -> TextHitInfo: ...
    @overload
    def hitTestChar(self, float: float, float2: float, rectangle2D: java.awt.geom.Rectangle2D) -> TextHitInfo: ...
    def hitToPoint(self, textHitInfo: TextHitInfo, point2D: java.awt.geom.Point2D) -> None: ...
    def isLeftToRight(self) -> bool: ...
    def isVertical(self) -> bool: ...
    def toString(self) -> str: ...
    class CaretPolicy:
        def __init__(self): ...
        def getStrongCaret(self, textHitInfo: TextHitInfo, textHitInfo2: TextHitInfo, textLayout: 'TextLayout') -> TextHitInfo: ...

class TextLine:
    def __init__(self, fontRenderContext: FontRenderContext, textLineComponentArray: _py_List[sun.font.TextLineComponent], floatArray: _py_List[float], charArray: _py_List[str], int: int, int2: int, intArray: _py_List[int], byteArray: _py_List[int], boolean: bool): ...
    def caretAtOffsetIsValid(self, int: int) -> bool: ...
    def characterCount(self) -> int: ...
    @classmethod
    def createComponentsOnRun(cls, int: int, int2: int, charArray: _py_List[str], intArray: _py_List[int], byteArray: _py_List[int], textLabelFactory: sun.font.TextLabelFactory, font: java.awt.Font, coreMetrics: sun.font.CoreMetrics, fontRenderContext: FontRenderContext, decoration: sun.font.Decoration, textLineComponentArray: _py_List[sun.font.TextLineComponent], int4: int) -> _py_List[sun.font.TextLineComponent]: ...
    @classmethod
    def createLineFromText(cls, charArray: _py_List[str], styledParagraph: StyledParagraph, textLabelFactory: sun.font.TextLabelFactory, boolean: bool, floatArray: _py_List[float]) -> 'TextLine': ...
    def draw(self, graphics2D: java.awt.Graphics2D, float: float, float2: float) -> None: ...
    @classmethod
    def fastCreateTextLine(cls, fontRenderContext: FontRenderContext, charArray: _py_List[str], font2: java.awt.Font, coreMetrics: sun.font.CoreMetrics, map: java.util.Map[java.text.AttributedCharacterIterator.Attribute, _py_Any]) -> 'TextLine': ...
    @classmethod
    def getAdvanceBetween(cls, textLineComponentArray: _py_List[sun.font.TextLineComponent], int: int, int2: int) -> float: ...
    def getCharAdvance(self, int: int) -> float: ...
    def getCharAngle(self, int: int) -> float: ...
    def getCharAscent(self, int: int) -> float: ...
    def getCharBounds(self, int: int) -> java.awt.geom.Rectangle2D: ...
    def getCharDescent(self, int: int) -> float: ...
    def getCharLevel(self, int: int) -> int: ...
    @overload
    def getCharLinePosition(self, int: int) -> float: ...
    @overload
    def getCharLinePosition(self, int: int, boolean: bool) -> float: ...
    def getCharShift(self, int: int) -> float: ...
    def getCharType(self, int: int) -> int: ...
    def getCharXPosition(self, int: int) -> float: ...
    def getCharYPosition(self, int: int) -> float: ...
    @classmethod
    def getComponents(cls, styledParagraph: StyledParagraph, charArray: _py_List[str], int: int, int2: int, intArray: _py_List[int], byteArray: _py_List[int], textLabelFactory: sun.font.TextLabelFactory) -> _py_List[sun.font.TextLineComponent]: ...
    def getCoreMetricsAt(self, int: int) -> sun.font.CoreMetrics: ...
    def getItalicBounds(self) -> java.awt.geom.Rectangle2D: ...
    def getJustifiedLine(self, float: float, float2: float, int: int, int2: int) -> 'TextLine': ...
    def getMetrics(self) -> 'TextLine.TextLineMetrics': ...
    def getOutline(self, affineTransform: java.awt.geom.AffineTransform) -> java.awt.Shape: ...
    def getPixelBounds(self, fontRenderContext: FontRenderContext, float: float, float2: float) -> java.awt.Rectangle: ...
    def getVisualBounds(self) -> java.awt.geom.Rectangle2D: ...
    def hashCode(self) -> int: ...
    def isCharLTR(self, int: int) -> bool: ...
    def isCharSpace(self, int: int) -> bool: ...
    def isCharWhitespace(self, int: int) -> bool: ...
    def isDirectionLTR(self) -> bool: ...
    def logicalToVisual(self, int: int) -> int: ...
    @classmethod
    def standardCreateTextLine(cls, fontRenderContext: FontRenderContext, attributedCharacterIterator: java.text.AttributedCharacterIterator, charArray: _py_List[str], floatArray: _py_List[float]) -> 'TextLine': ...
    def toString(self) -> str: ...
    def visualToLogical(self, int: int) -> int: ...

class TextMeasurer(java.lang.Cloneable):
    def __init__(self, attributedCharacterIterator: java.text.AttributedCharacterIterator, fontRenderContext: FontRenderContext): ...
    def deleteChar(self, attributedCharacterIterator: java.text.AttributedCharacterIterator, int: int) -> None: ...
    def getAdvanceBetween(self, int: int, int2: int) -> float: ...
    def getLayout(self, int: int, int2: int) -> TextLayout: ...
    def getLineBreakIndex(self, int: int, float: float) -> int: ...
    def insertChar(self, attributedCharacterIterator: java.text.AttributedCharacterIterator, int: int) -> None: ...

class TransformAttribute(java.io.Serializable):
    IDENTITY: _py_ClassVar['TransformAttribute'] = ...
    def __init__(self, affineTransform: java.awt.geom.AffineTransform): ...
    def equals(self, object: _py_Any) -> bool: ...
    def getTransform(self) -> java.awt.geom.AffineTransform: ...
    def hashCode(self) -> int: ...
    def isIdentity(self) -> bool: ...

class ImageGraphicAttribute(GraphicAttribute):
    @overload
    def __init__(self, image: java.awt.Image, int: int): ...
    @overload
    def __init__(self, image: java.awt.Image, int: int, float: float, float2: float): ...
    def draw(self, graphics2D: java.awt.Graphics2D, float: float, float2: float) -> None: ...
    @overload
    def equals(self, imageGraphicAttribute: 'ImageGraphicAttribute') -> bool: ...
    @overload
    def equals(self, object: _py_Any) -> bool: ...
    def getAdvance(self) -> float: ...
    def getAscent(self) -> float: ...
    def getBounds(self) -> java.awt.geom.Rectangle2D: ...
    def getDescent(self) -> float: ...
    def hashCode(self) -> int: ...

class ShapeGraphicAttribute(GraphicAttribute):
    STROKE: _py_ClassVar[bool] = ...
    FILL: _py_ClassVar[bool] = ...
    def __init__(self, shape: java.awt.Shape, int: int, boolean: bool): ...
    def draw(self, graphics2D: java.awt.Graphics2D, float: float, float2: float) -> None: ...
    @overload
    def equals(self, shapeGraphicAttribute: 'ShapeGraphicAttribute') -> bool: ...
    @overload
    def equals(self, object: _py_Any) -> bool: ...
    def getAdvance(self) -> float: ...
    def getAscent(self) -> float: ...
    def getBounds(self) -> java.awt.geom.Rectangle2D: ...
    def getDescent(self) -> float: ...
    def getOutline(self, affineTransform: java.awt.geom.AffineTransform) -> java.awt.Shape: ...
    def hashCode(self) -> int: ...
