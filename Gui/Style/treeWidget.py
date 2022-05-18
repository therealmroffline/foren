from PyQt5.QtWidgets import QStyledItemDelegate,QTreeWidget,QTreeWidgetItem
from PyQt5.QtGui import QIcon

class StyledItemDelegate(QStyledItemDelegate):
    def sizeHint(self, option, index):
        s = super(StyledItemDelegate, self).sizeHint(option, index)
        if index.parent().isValid():
            s.setHeight(25)
        else:
            s.setHeight(25)
        return s


class TreeWidget(QTreeWidget):
    def __init__(self):
        super(TreeWidget,self).__init__()
        delegate = StyledItemDelegate(self)
        self.setItemDelegate(delegate)
        self.setAlternatingRowColors(True)
        STYLESHEET = '''QTreeWidget {border:None} 
            QTreeWidget::Item{
                border-bottom:2px  black;
                color: rgba(255,255,255,255);
            }
            QTreeView{
                alternate-background-color: rgba(170,170,170,255);
                background: rgba(211,211,211,255);
            }
                QTreeView::indicator::checked {image: url(Images/R.png);}
                QTreeView::indicator::unchecked {image: url(Images/checkbox.png);}

            '''
        self.setStyleSheet(STYLESHEET)

class checked_icon(QIcon):
    __instance=None
    def __init__(self):
        self.path = "Images/R.png"
        super(checked_icon, self).__init__(self.path)

    @staticmethod
    def get_instance():
        if checked_icon.__instance is None:
            checked_icon.__instance = checked_icon()
        return checked_icon.__instance

class unchecked_icon(QIcon):
    __instance=None
    def __init__(self):
        self.path = "Images/checkbox.png"
        super(unchecked_icon, self).__init__(self.path)


    @staticmethod
    def get_instance():
        if unchecked_icon.__instance is None:
            unchecked_icon.__instance = unchecked_icon()
        return unchecked_icon.__instance

class TreeWidgetItem(QTreeWidgetItem):
    def __init__(self,Parent):
        super(TreeWidgetItem, self).__init__(Parent)
        self.Path=None
        self.checked = checked_icon.get_instance()
        self.unchecked = unchecked_icon.get_instance()

    def set_path(self,path):
        self.Path=path

    def get_path(self):
        return self.Path

    def set_checked(self):
        self.setIcon(0,self.checked)

    def set_unchecked(self):
        self.setIcon(0,self.unchecked)
