from PyQt5.QtGui import QTextDocument, QFont, QColor
from PyQt5.QtCore import Qt
from logger.highlighterRule import HighlighterRule
from logger.highlighter import Highlighter


class LogHighlighter(Highlighter):
    def __init__(self, textDocument: QTextDocument):
        super(LogHighlighter, self).__init__(textDocument, [
            HighlighterRule(
                [
                    "\\bError:.*"
                ],
                # QColor(255, 115, 117, 255),
                Qt.red,
                QFont.Normal
            ),
            HighlighterRule(
                [
                    "\\bWarning:.*"
                ],
                QColor(255, 200, 117, 255),
                QFont.Normal
            ),

            HighlighterRule(
                [
                    "\\bInfo:.*"
                ],
                Qt.gray,
                QFont.Normal
            ),

            HighlighterRule(
                [
                    "\\bSuccess:.*"
                ],
                QColor(15 ,157 ,88),
                QFont.Normal
            )
        ])
