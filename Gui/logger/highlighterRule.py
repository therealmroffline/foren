from PyQt5.QtGui import QColor, QFont


class HighlighterRule:
    def __init__(self, keywords: list, fontColor: QColor, fontWeight: QFont.Weight):
        self._keywords = keywords
        self._fontWeight = fontWeight
        self._fontColor = fontColor

    def getFontColor(self) -> QColor:
        return self._fontColor

    def getFontWeight(self) -> QFont.Weight:
        return self._fontWeight

    def getKeywords(self) -> list:
        return self._keywords
