import PyQt5
from PyQt5.QtWidgets import QWidget, QPlainTextEdit, QHBoxLayout, QAction
from PyQt5.QtGui import QFont
from logger.logHighlighter import LogHighlighter

"""
This class represents the Log that can be put in the status bar
"""

class _log_plain_text_area(QPlainTextEdit):
    def __init__(self, *args, **kwargs):
        super(_log_plain_text_area, self).__init__(*args, **kwargs)

    def contextMenuEvent(self, e:PyQt5.QtGui.QContextMenuEvent):
        menu = self.createStandardContextMenu()
        menu.addSeparator()
        clrAct = menu.addAction("Clear")
        action = menu.exec_(self.mapToGlobal(e.pos()))
        if action == clrAct:
            self.clear()

class Log(QWidget):
    # The variable is used to keep the singleton object
    _instance = None

    """
    Don't call the constructor directly. Instead, call the Log.getInstance() method
    """

    def __init__(self, parent):
        super(Log, self).__init__(parent)
        self.textEdit = _log_plain_text_area()
        self.textEdit.setObjectName("log-text")
        self.logHighlighter = LogHighlighter(self.textEdit.document())
        self.setObjectName("log")
        self._draw()

    """
    This method enforces the singleton pattern
    This method should be called instead of the constructor directly
    This method makes sure that there is always only one instance of this class and it only should be used
    """

    @staticmethod
    def getInstance(parent=None):
        if Log._instance is None:
            Log._instance = Log(parent)
        return Log._instance

    """
    Create the GUI of the Log
    """

    def _draw(self):
        # self.setContentsMargins(80, 0, 0, 0)
        # self.setContentsMargins(5, 5, 5, 5)
        self._layout = QHBoxLayout()
        self.textEdit.setReadOnly(True)
        self.textEdit.setContentsMargins(0, 0, 0, 0)
        self._layout.addWidget(self.textEdit)
        self.setLayout(self._layout)
        self.layout().setContentsMargins(0, 0, 0, 0)
        f = QFont("monospace")
        f.setStyleHint(QFont.Monospace)
        self.textEdit.setFont(f)