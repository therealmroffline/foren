from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
class Label(QLabel):
    def __init__(self, text):
        super(Label, self).__init__(text)
        fnt = QFont('Arial', 12)
        self.setFont(fnt)
        self.setText(self.text().title())
