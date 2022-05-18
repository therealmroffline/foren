from PyQt5.QtWidgets import QCheckBox

class CheckBox(QCheckBox):
    def __init__(self, text=None):
        super(CheckBox, self).__init__(text)
        self.setStyleSheet("QCheckBox::indicator"
                           "{"
                           "width :20px;"
                           "height : 20px;"
                           "}"
                           "QCheckBox::indicator:checked {image: url(Images/R.png);}"
                           "QCheckBox::indicator:unchecked {image: url(Images/checkbox.png);}"
                           "QCheckBox {Font:  large 'Open Sans'; font-size:25px;padding:10px;}")
