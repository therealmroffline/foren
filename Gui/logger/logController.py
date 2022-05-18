import threading

from PyQt5.QtCore import QObject, QTimer
from logger.log import Log
import time
from PyQt5.QtWidgets import QApplication


class LogController(QObject):
    """ Generating Log Controller
        Responsibilities:
            1. Controlling the operations done on the Log
        NOTES:
            - Singleton design pattern was used to create the class
            - Make an object in the class first time you use the class
            - Always use the 'get_instance' method to access the created object
    """
    _instance = None  # Object created with the class

    @staticmethod
    def get_instance():
        """
        @return: singleton object from the class
        @rtype: LogController
        @raise: when the function is used before creating an object from the class
        """
        if LogController._instance is None:
            raise Exception("No object was created.")
        return LogController._instance

    def __init__(self, gui: Log):
        """
        @param gui: object that will be controlled with class
        @param parent: parent class in QT qobject
        @raise: when the constructor is used after the singleton object is created
        """
        """ ----------------------------- SINGLETON PATTERN LOGIC -------------------------------------------------- """
        if LogController._instance is None:
            super(LogController, self).__init__()
            LogController._instance = self  # initializing the singleton object
            self.gui = gui  # gui object which is controlled by the controller
            self._textEditTextParts = []
            self._loadingBarTimers = {}
            self.loadingStartTime = None
        else:
            raise Exception("Controllers are singletone classes, please use the instance function")
        """----------------------------------------------------------------------------------------------------------"""

    """
    This method takes the text to be appended to the PlainTexEdit and appends it
    """

    def add_text(self, text):
        self._textEditTextParts.append(text)
        self.gui.textEdit.appendPlainText(text)
        self.gui.textEdit.verticalScrollBar().setValue(self.gui.textEdit.verticalScrollBar().maximum())
        QApplication.processEvents()

    """
       This method takes the text to be inserted to the PlainTexEdit and adds it to the end of last line
    """

    def insert_text(self, text):
        self._textEditTextParts[-1] = self._textEditTextParts[-1] + text
        self.gui.textEdit.insertPlainText(text)

    """
    This method takes the info text to be appended to the PlainTexEdit and appends it
    """

    def add_info(self, text):
        newText = "Info: " + text
        self.add_text(newText)

    """
    This method takes the error text to be appended to the PlainTexEdit and appends it
    """

    def add_error(self, text):
        newText = "Error: " + text
        self.add_text(newText)

    """
    This method takes the warning text to be appended to the PlainTexEdit and appends it
    """

    def add_warning(self, text):
        newText = "Warning: " + text
        self.add_text(newText)


    def add_success(self,text):
        newText = "Success: " + text
        self.add_text(newText)


    """
    This method add Loading bar as a text
    """

    def add_percentage_bar(self, title: str) -> int:
        self.add_text(title + ": " + " "*20 + " 0%")
        self.loadingStartTime = time.time()
        return len(self._textEditTextParts) - 1

    """
    This methode updates Percentage loading bar
    """

    def update_percentage_bar(self, loadingBarID: int, percentage: int) -> None:
        print("Percentage: ", percentage)
        if percentage == 0:
            self.loadingStartTime = time.time()
        else:
            timeTaken = time.time() - self.loadingStartTime
            timeForOnepercent = timeTaken/percentage
            secondsRemaining = int(timeForOnepercent * (100 - percentage))
            text = self._textEditTextParts[loadingBarID][0:self._textEditTextParts[loadingBarID].index(":")]
            text += ": " + "█"*int(percentage/5) + " "*(20-int(percentage/5)) + " " + str("{:.2f}".format(float(percentage))) + "%"
            if secondsRemaining != 0:
                if secondsRemaining < 60:
                    text += " | " + str(secondsRemaining) + " seconds remaining."
                else:
                    minutesRemaining = int(secondsRemaining/60)
                    if minutesRemaining < 60:
                        text += " | " + str(minutesRemaining) + " minutes remaining."
                    else:
                        hoursRemaining = int(minutesRemaining/60)
                        minutesRemaining = int(minutesRemaining - hoursRemaining*60)
                        if hoursRemaining == 1:
                            text += " | " + str(hoursRemaining) + " hour and "+ str(minutesRemaining) +\
                            " minutes remaining."
                        else:
                            text += " | " + str(hoursRemaining) + " hours and "+ str(minutesRemaining) +\
                                " minutes remaining."
            self._textEditTextParts[loadingBarID] = text
            self.show_all()

    """
    This method add Loading bar
    """

    def add_loading_bar(self, title: str, interval:int =500) -> int:
        self.add_text(title + ".")
        loadingBar_id = len(self._textEditTextParts) - 1
        self._loadingBarTimers[loadingBar_id] = QTimer()

        def update():
            self._textEditTextParts[loadingBar_id] += "."
            self.show_all()

        self._loadingBarTimers[loadingBar_id].timeout.connect(update)
        self._loadingBarTimers[loadingBar_id].start(interval)
        return loadingBar_id

    """
    This method stops the Loading bar
    """

    def stop_loading_bar(self, loadingBar_id: int) -> None:
        self._loadingBarTimers[loadingBar_id].stop()

    """
    This method takes a piece of text and shows only the messages saved in the log that contains this piece of text
    """

    def _show_specific_messages_only(self, wantedTextPart):
        self.gui.textEdit.setPlainText("")
        for textPart in self._textEditTextParts:
            if wantedTextPart in textPart:
                self.gui.textEdit.appendPlainText(textPart)

    """
    This method shows only the error parts in the log
    """

    def show_errors_only(self):
        self._show_specific_messages_only("Error:")

    """
    This method shows only the info parts in the log
    """

    def show_info_only(self):
        self._show_specific_messages_only("Info:")

    """
    This method shows only the warning error in the log
    """

    def show_warnings_only(self):
        self._show_specific_messages_only("Warning:")

    """
    This method shows only all the text in the log
    """

    def show_all(self):
        self.gui.textEdit.setPlainText("")
        for textPart in self._textEditTextParts:
            self.gui.textEdit.appendPlainText(textPart)

    def toggle_log(self):
        if self.gui.isHidden():
            self.gui.show()
        else:
            self.gui.hide()

