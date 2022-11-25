import sys

from PySide2 import QtCore, QtGui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

from ui_main import Ui_MainWindow 

from ui_dialog import Ui_Dialog

class GmailException(Exception):
	"""gmail base exception class"""

class NoEmailFound(GmailException):
	"""no email found"""

class dialogUi(QDialog):
    def __init__(self, parent=None):

        super(dialogUi, self).__init__(parent)
        self.d = Ui_Dialog()
        self.d.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
        self.d.bn_min.clicked.connect(lambda: self.showMinimized())

        self.d.bn_close.clicked.connect(lambda: self.close())

        
        self.dragPos = self.pos()   
        def movedialogWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.d.frame_top.mouseMoveEvent = movedialogWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def dialogConstrict(self, heading, message, icon):
        self.d.lab_heading.setText(heading)
        self.d.lab_message.setText(message)
        # self.d.bn_east.setText(btn2)
        # self.d.bn_west.setText(btn1)
        pixmap = QtGui.QPixmap(icon)
        self.d.lab_icon.setPixmap(pixmap)




class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        from ui_function import UIFunction

        applicationName = "Gmail Attachment Extractor"
        self.setWindowTitle(applicationName) 
        UIFunction.labelTitle(self, applicationName) 
        UIFunction.initStackTab(self)
        UIFunction.constantFunction(self)
        self.ui.bn_home.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_home'))
        self.ui.bn_android.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_cloud'))
        self.ui.bn_cloud.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_android'))
        UIFunction.stackPage(self)
        self.diag = dialogUi()
        # self.error = errorUi()


        self.dragPos = self.pos()
        def moveWindow(event):
            if UIFunction.returStatus() == 1: 
                UIFunction.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        
        self.ui.frame_appname.mouseMoveEvent = moveWindow  
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    def dialogexec(self, heading, message, icon):
        dialogUi.dialogConstrict(self.diag, heading, message, icon)
        self.diag.exec_()

if __name__ == '__main__':

	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	
	sys.exit(app.exec_())