from asyncio.windows_events import NULL
from concurrent.futures import thread
from pickle import NONE
from main import *
import os
import threading as td
from core_functions import *
from PyQt5 import QtWidgets
import PySide2

GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True
init = False

login_status = 0
clicked = 0
downloading = 0
arr = []


def check_path(wokring_dir, token_dir):
    global login_status
    while os.path.exists(os.path.join(wokring_dir, token_dir)):
        login_status = 1

    login_status = 0


t = td.Thread(target=check_path, args=(os.getcwd(), "token files"))
if not t.is_alive():
    t.start()


class UIFunction(MainWindow):
    def __init__(self):
        self.trd = None

    def initStackTab(self):
        print("hello")

        global init

        if not login_status:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.lab_tab.setText("Home")
            self.ui.frame_home.setStyleSheet("background:rgb(1, 175, 255);")
            init = True
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.home_after_login)
            self.ui.lab_tab.setText("Home After Login")
            self.ui.frame_home.setStyleSheet("background:rgb(1, 175, 255);")

    def labelTitle(self, appName):
        self.ui.lab_appname.setText(appName)

    # ----> MAXIMISE/RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.bn_max.setToolTip("Restore")
            # CHANGE THE MAXIMISE ICON TO RESTOR ICON
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/restore.png"))
            self.ui.frame_drag.hide()  # HIDE DRAG AS NOT NECESSERY
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.bn_max.setToolTip("Maximize")
            # CHANGE BACK TO MAXIMISE ICON
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/max.png"))
            self.ui.frame_drag.show()

    def returStatus():
        return GLOBAL_STATE

    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    def constantFunction(self):
        def maxDoubleClick(stateMouse):
            if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunction.maximize_restore(self))

        if True:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_appname.mouseDoubleClickEvent = maxDoubleClick
        else:
            self.ui.frame_close.hide()
            self.ui.frame_max.hide()
            self.ui.frame_min.hide()
            self.ui.frame_drag.hide()

        self.ui.bn_min.clicked.connect(lambda: self.showMinimized())

        self.ui.bn_max.clicked.connect(lambda: UIFunction.maximize_restore(self))

        self.ui.bn_close.clicked.connect(lambda: self.close())

    def buttonPressed(self, buttonName):

        index = self.ui.stackedWidget.currentIndex()

        t = td.Thread(target=check_path, args=(os.getcwd(), "token files"))
        t.start()

        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if buttonName == "bn_home":
            print("F", login_status)
            UIFunction.initStackTab(self)

        elif buttonName == "bn_android":
            if login_status == 0:
                self.dialogexec(
                    "Warning",
                    "Please Login to access this feature.",
                    "icons/1x/errorAsset 55.png",
                )
            else:
                if self.ui.frame_bottom_west.width() == 80 and index != 7:
                    self.ui.stackedWidget.setCurrentWidget(self.ui.page_download)
                    self.ui.lab_tab.setText("Live Downloads")
                    # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                    self.ui.frame_cloud.setStyleSheet("background:rgb(1, 175, 255);")
                    # UIFunction.androidStackPages(self, "page_contact")

                elif (
                    self.ui.frame_bottom_west.width() == 160 and index != 3
                ):  # ABOUT PAGE STACKED WIDGET
                    self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_android)
                    self.ui.lab_tab.setText("About > Live Downloads")
                    # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                    self.ui.frame_cloud.setStyleSheet("background:rgb(1, 175, 255);")

        elif buttonName == "bn_cloud":
            if self.ui.frame_bottom_west.width() == 80 and index != 6:
                print("In cloud")
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_cloud)
                self.ui.download_table.setColumnWidth(0, 350)
                self.ui.download_table.setColumnWidth(1, 350)
                self.ui.download_table.setColumnWidth(2, 350)

                # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                self.ui.frame_android.setStyleSheet("background:rgb(1, 175, 255);")

            elif (
                self.ui.frame_bottom_west.width() == 160 and index != 2
            ):  # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_cloud)
                self.ui.lab_tab.setText("About > Cloud")
                # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                self.ui.frame_android.setStyleSheet("background:rgb(1, 175, 255);")

    def loaddata(self):
        global arr
        # arr.append(get_data())
        global downloading
        while downloading == 1:
            arr = get_data()
            row = 0
            self.ui.download_table.setRowCount(len(arr))
            for item in arr:
                self.ui.download_table.setItem(
                    row, 0, PySide2.QtWidgets.QTableWidgetItem(item[2])
                )
                self.ui.download_table.setItem(
                    row, 1, PySide2.QtWidgets.QTableWidgetItem(str(item[0]))
                )
                self.ui.download_table.setItem(
                    row, 2, PySide2.QtWidgets.QTableWidgetItem(str(item[1]))
                )
                row = row + 1
            time.sleep(1)

    def control(self):
        global clicked
        global downloading
        if clicked == 0:
            filters(
                self.ui.email_from.text(),
                self.ui.to.text(),
                self.ui.date_from.text(),
                self.ui.date_upto.text(),
                self.ui.subject.text(),
                self.ui.has_words.text(),
                self.ui.doesnt_have.text(),
                self.ui.upcoming.isChecked(),
                self.ui.read.isChecked(),
                self.ui.unread.isChecked(),
                self.ui.localStorage.isChecked(),
                self.ui.gDrive.isChecked(),
            )
            start_download(1, self.ui.upcoming.isChecked())
            downloading = 1
            trd1 = td.Thread(target=UIFunction.loaddata, args=(self,))
            trd1.start()
            self.ui.save_attach.setText("Stop Download")
            self.ui.save_attach.setStyleSheet(
                'background: rgb(255, 0, 0);\nfont: 10pt "MS Shell Dlg 2";'
            )
            self.ui.save_attach.setIcon(QtGui.QIcon("icons/1x/pause.png"))
        else:
            stop_download(0)
            downloading = 0
            self.ui.save_attach.setText("Start Download")
            self.ui.save_attach.setStyleSheet(
                'background: rgb(85, 255, 0); font: 75 10pt "MS Shell Dlg 2";'
            )
            self.ui.save_attach.setIcon(QtGui.QIcon("icons/1x/play.png"))

        clicked = 1 - clicked

        print("clicked: ", clicked)

    def logout_(self):
        logout()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home),
        self.ui.lab_tab.setText("Home"),
        self.ui.frame_home.setStyleSheet("background:rgb(1, 175, 255);")

    def login_(self):
        x = login()

    def directory(self):
        self.ui.label_8.setText(choose_directory())
        if self.ui.label_8.text() != "" or self.ui.gDrive.isChecked():
            self.ui.save_attach.setEnabled(1)

    def stackPage(self):

        self.ui.lab_home_main_hed.setText("About the Application")
        self.ui.loginButton.clicked.connect(lambda: UIFunction.login_(self))

        self.ui.logout.clicked.connect(lambda: UIFunction.logout_(self))

        self.ui.save_attach.clicked.connect(lambda: UIFunction.control(self))

        self.ui.choose_directory.clicked.connect(
            # lambda: UIFunction.clickChooseDirectory(self)
            lambda: UIFunction.directory(self)
        )
