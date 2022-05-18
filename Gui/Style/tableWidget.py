from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QHeaderView
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
class TableWidget(QTableWidget):
    def __init__(self,columnCount, rowCount, tableList):
        super(TableWidget, self).__init__()
        self.tableList = tableList
        self.setColumnCount(columnCount)  # set table columns size
        self.setRowCount(rowCount)  # set table rows size
        self.verticalHeader().setVisible(False)  # remove table index for each column
        self.horizontalHeader().setVisible(False)  # remove table index for each row
        self.setStyleSheet("""QTableWidget::item {border-bottom: 1px solid}""")

        header = self.horizontalHeader()

        # Make Cells stretch with the data size
        for i in range(columnCount):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

    def adjust_item(self, config):  # update short name
        if self.currentRow() != 0:  # if it is not the labels row

            if self.currentColumn() == 0:  # short name
                self.tableList[self.currentRow() - 1].shortName.setText(self.currentItem().text())

    def adjust_combobox(self, config, combo_box):
        index = self.currentRow() - 1
        self.tableList[index].ref_comboBox.setCurrentText(combo_box[index].currentText())
        self.tableList[index].update_values()

class HeaderTableWidgetItem(QTableWidgetItem):
    def __init__(self, text):
        super(HeaderTableWidgetItem, self).__init__()
        self.setText(text)
        self.setFlags(Qt.ItemIsEnabled)  # not editable
        self.setFont(QFont('Arial', 11))
