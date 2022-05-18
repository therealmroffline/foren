from PyQt5.QtGui import QSyntaxHighlighter, QTextDocument, QTextCharFormat, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRegExp


class Highlighter(QSyntaxHighlighter):
    def __init__(self, textDocument: QTextDocument, highlighterRules):
        super(Highlighter, self).__init__(textDocument)
        self._highlighterRules = highlighterRules

    def highlightBlock(self, text):
        for highlighterRule in self._highlighterRules:
            myClassFormat = QTextCharFormat()
            myClassFormat.setFontWeight(highlighterRule.getFontWeight())
            myClassFormat.setForeground(highlighterRule.getFontColor())
            pattern = ""
            if len(highlighterRule.getKeywords()) > 0:
                pattern += "("
                for keyword in highlighterRule.getKeywords():
                    pattern += (keyword + "|")
                pattern = pattern[:-1] + ")"

            expression = QRegExp(pattern)
            index = expression.indexIn(text, 0)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, myClassFormat)
                index = expression.indexIn(text, index + length)
