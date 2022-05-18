import sys
import glob
import os
import stat
import copy
import shutil
import dpkt
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QSize
from moduleConfgFrames import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import QFont, QColor, QIcon
from PyQt5.QtCore import pyqtSlot
from Gui.logger.logController import LogController
from distutils.dir_util import copy_tree
from pcapfile import savefile


  






def getRteTemplateObject(arxmlInputPathList):
    packageParserObject = PackageParser(arxmlInputPathList=arxmlInputPathList, resolver=True, rapidStatus=True)
    return packageParserObject.getTemplateObject()




class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)


class AppConfigWindow(QMainWindow):
    __instance = None  # Singleton Instance

    windowFrame = Ui_MainWindow()



    def __init__(self, toolName, toolIcon):

        super(AppConfigWindow, self).__init__()

        self.windowFrame = Ui_MainWindow()
        self.windowFrame.setupUi(self)

        self.setWindowTitle(toolName)
        self.setWindowIcon(QtGui.QIcon(toolIcon))



        
        # self.parametersAndReferences.setGeometry(500, 70, 850, 500)
        self.parametersAndReferencesRows = QFormLayout()
        self.logger = LogController(self.windowFrame.log)
        self.logger.add_text("Fori_tool Logger")
        self.toolIcon = toolIcon

     
        self.showToolBar()

    @staticmethod
    def getInstance(toolName=None, toolIcon=None):
        if AppConfigWindow.__instance is None:
            AppConfigWindow.__instance = AppConfigWindow(toolName, toolIcon)
        return AppConfigWindow.__instance

    
    

    def showToolBar(self):

        self.addToolBarItem = QAction("o1", self)
        self.addToolBarItem.setIcon(QtGui.QIcon('Images/plus.png'))
        self.windowFrame.toolBar.addAction(self.addToolBarItem)
        self.addToolBarItem.triggered.connect(self.o1)

        self.deleteToolBarItem = QAction("o2", self)
        self.deleteToolBarItem.setIcon(QtGui.QIcon('Images/delete.jpg'))
        self.windowFrame.toolBar.addAction(self.deleteToolBarItem)
        self.deleteToolBarItem.triggered.connect(self.o2)

        self.saveToolBarItem = QAction("o3", self)
        self.saveToolBarItem.setIcon(QtGui.QIcon('Images/save.png'))
        self.windowFrame.toolBar.addAction(self.saveToolBarItem)
        self.saveToolBarItem.triggered.connect(self.o3)

        self.generateToolBarItem = QAction(" o4", self)
        self.generateToolBarItem.setIcon(QtGui.QIcon('Images/generate.png'))
        self.windowFrame.toolBar.addAction(self.generateToolBarItem)
        self.generateToolBarItem.triggered.connect(self.o4)

        self.loadToolBarItem = QAction("o5", self)
        self.loadToolBarItem.setIcon(QtGui.QIcon('Images/load.png'))
        self.windowFrame.toolBar.addAction(self.loadToolBarItem)
        self.loadToolBarItem.triggered.connect(self.o5)

    def clickme(self):
        self.nm2.setText("")
        if self.nm.text()=="":
            self.logger.add_warning("no file name added ")
        else:
            self.logger.add_text("searching for "+self.nm.text())
            try:
                ok=0
                for r,d,f in os.walk("/"):
                
                    for files in f:
                         if files == self.nm.text():
                              ok=1
                              print (os.path.join(r,files))
                              a=os.path.join(r,files)
                              stats = os.stat(a)
                              print(stats.st_ino )
                              self.logger.add_text(str(a)+"  "+str(stats.st_ino))
                              print(a)

                             
                
                
                if ok == 1:
                    self.logger.add_success("search completed " )
                else:
                    self.logger.add_success("search completed no file found " )
            except:
                self.logger.add_error("file not found")


    def clickme2(self):
        ok=0
        x=""
        with os.scandir("/") as itr:
                for entry in itr :
                    print(entry.name, " :", entry.inode())
        if self.nm.text()=="":
            self.logger.add_warning("no inode  added ")
        else:
            try:
                self.logger.add_text("inode "+self.nm.text())
                with os.scandir("/") as itr:
                    for entry in itr :
                        a= entry.inode()                
                        if self.nm.text()== str(a):
                            ok=1
                            x=x+entry.name+" "
                if ok==1:
                    print(x)
                    self.logger.add_success(x+" where found")
                else:
                    self.logger.add_success("not found")
                        
            except:
                self.logger.add_error("finding inode  ")
    def clickme3(self):
        if self.nm.text()=="":
            self.logger.add_warning("add a file")
        else:
            try:
                testcap = open(self.nm.text(), 'rb')
                capfile = savefile.load_savefile(testcap, verbose=True)
                self.logger.add_text(str(capfile))
                self.logger.add_success("finished reading")
            except:
                self.logger.add_error("check the extenstion or the version of the file")

        
    def dataFile(self):

        self.datafilePath = QFileDialog.getOpenFileName(self, 'choose file', 
        '/'," (*.pcap)")
        self.nm.setText(self.datafilePath[0])



 
    def o1(self):
       self.logger.add_text("Find the inode number of a file")
       self.l1 = QLabel("file name with extention ")
       self.nm = QLineEdit("")
       self.nm2 = QLineEdit("")
       self.button = QPushButton("search", self)
       self.button.clicked.connect(self.clickme)
       self.fbox = QFormLayout()
       self.fbox.addRow(self.l1,self.nm)
       self.fbox.addRow(self.button)
       self.win = QWidget()
       self.win.setLayout(self.fbox)
       self.setCentralWidget(self.win)
      

       

        

    def o2(self):
       self.logger.add_text("enter the inode number")
       self.l1 = QLabel("inode number  ")
       self.nm = QLineEdit("")
       self.button = QPushButton("search", self)
       self.button.clicked.connect(self.clickme2)
       self.fbox = QFormLayout()
       self.fbox.addRow(self.l1,self.nm)
       self.fbox.addRow(self.button)
       self.win = QWidget()
       self.win.setLayout(self.fbox)
       self.setCentralWidget(self.win)

    def o3(self):
       self.logger.add_text("Packet capture INFO")
       self.l1 = QLabel("Browse  ")
       self.nm = QLineEdit("")
       self.button = QPushButton("check the report", self)
       self.button.clicked.connect(self.clickme3)
       self.fbox = QFormLayout()
       self.fbox.addRow(self.l1,self.nm)
       self.dataButton = QtWidgets.QPushButton()
       self.dataButton.setText("Pcap File")
       self.dataButton.move(280, 105)
       self.dataButton.resize(150, 50)
       self.dataButton.setFont(QtGui.QFont("Sanserif", 10))
       self.dataButton.setIcon(QIcon("Images/folder.png"))
       self.dataButton.clicked.connect(self.dataFile)
       self.fbox.addRow(self.dataButton,self.button)
       self.win = QWidget()
       self.win.setLayout(self.fbox)
       self.setCentralWidget(self.win)

    def o4(self):
       self.logger.add_text("enter the inode number")
       self.l1 = QLabel("inode number  ")
       self.nm = QLineEdit("")
       self.button = QPushButton("search", self)
       self.button.clicked.connect(self.clickme2)
       self.fbox = QFormLayout()
       self.fbox.addRow(self.l1,self.nm)
       self.fbox.addRow(self.button)
       self.win = QWidget()
       self.win.setLayout(self.fbox)
       self.setCentralWidget(self.win)        
    def o5(self): 
         self.logger.add_text("5")

    

   


