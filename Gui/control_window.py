import sys
sys.path.append('../')
import time
from Gui.app_configure import AppConfigWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel

class Controller:

    def __init__(self):

        toolName = "Fori Tool"
        toolIcon = 'Images/tool icon.png'

  
        self.appConfigureWindow = AppConfigWindow.getInstance(toolName, toolIcon)

    def show_appConfigure_window(self):

    
        self.appConfigureWindow.showMaximized()


    

    def show_main(self):

        self.show_appConfigure_window()



def main():

    app = QtWidgets.QApplication(sys.argv)
    flagX = 100


    while flagX == 100:

        controller = Controller()
        controller.show_main()

        flagX = app.exec_()

    sys.exit(flagX)


if __name__ == '__main__':
    main()

