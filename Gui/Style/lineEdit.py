from PyQt5.QtGui import QRegExpValidator,QFont
from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QLineEdit



class LineEdit(QLineEdit):
    def __init__(self):
        super(LineEdit, self).__init__()
        self.setMaximumSize(550, 200)
        fnt = QFont('Arial', 10)
        self.setFont(fnt)
        validator = QRegExpValidator(QRegExp(r'[a-zA-z_]+[a-zA-z0-9_]+'))
        self.setValidator(validator)
        # self.setStyleSheet("background-color: rgba(0,0,0,0);")


class LineEdit_Num(QLineEdit):
    def __init__(self):
        super(LineEdit_Num, self).__init__()
        self.setMaximumSize(550, 200)
        fnt = QFont('Arial', 10)
        self.setFont(fnt)

