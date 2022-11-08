from asyncio.windows_events import NULL
from concurrent.futures import thread
from pickle import NONE
from main import *  # IMPORTING THE MAIN.PY FILE

from about import *

import os
import base64
from typing import List
import time
from google_apis import create_service

import sys
import threading as td

import shutil

from core_functions import *

GLOBAL_STATE = 0  # NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
# NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
GLOBAL_TITLE_BAR = True
init = False  # NECRESSERY FOR INITITTION OF THE WINDOW.

# tab_Buttons = ['bn_home', 'bn_bug', 'bn_android', 'bn_cloud'] #BUTTONS IN MAIN TAB
# android_buttons = ['bn_android_contact', 'bn_android_game', 'bn_android_clean', 'bn_android_world'] #BUTTONS IN ANDROID STACKPAGE

# THIS CLASS HOUSES ALL FUNCTION NECESSERY FOR OUR PROGRAMME TO RUN.

login_status = 0
clicked = 0

def check_path(wokring_dir, token_dir):
    global login_status
    while os.path.exists(os.path.join(wokring_dir, token_dir)):
        login_status = 1

    login_status = 0


t = td.Thread(target=check_path, args=(os.getcwd(), 'token files'))
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
            self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            init = True
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.home_after_login)
            self.ui.lab_tab.setText("Home After Login")
            self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")

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
            self.resize(self.width()+1, self.height()+1)
            self.ui.bn_max.setToolTip("Maximize")
            # CHANGE BACK TO MAXIMISE ICON
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/max.png"))
            self.ui.frame_drag.show()

    def returStatus():
        return GLOBAL_STATE

    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # ------> TOODLE MENU FUNCTION

    # def toodleMenu(self, maxWidth, clicked):

    #     #------> THIS LINE CLEARS THE BG OF PREVIOUS TABS : I.E. MAKING THEN NORMAL COLOR THAN LIGHTER COLOR.
    #     for each in self.ui.frame_bottom_west.findChildren(QFrame):
    #         each.setStyleSheet("background:rgb(51,51,51)")

    #     t = td.Thread(target=check_path, args=(os.getcwd(), 'token files'))
    #     print("f")
    #     t.start()

    #     t1 = td.Thread(target = UIFunction.check_status(self))
    #     t1.start()

    #     if clicked:
    #         currentWidth = self.ui.frame_bottom_west.width() #Reads the current width of the frame
    #         minWidth = 80 #MINIMUN WITDTH OF THE BOTTOM_WEST FRAME

    #         # if not login_status:
    #         #     self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
    #         #     self.ui.lab_tab.setText("Home")
    #         #     self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
    #         # else:
    #         #     self.ui.stackedWidget.setCurrentWidget(self.ui.home_after_login)
    #         #     self.ui.lab_tab.setText("Home After Login")
    #         #     self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")

    #         self.animation = QPropertyAnimation(self.ui.frame_bottom_west, b"minimumWidth")
    #         self.animation.setDuration(300)
    #         self.animation.setStartValue(minWidth)
    #         self.animation.setEndValue(minWidth)
    #         self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    #         self.animation.start()

    def constantFunction(self):
        def maxDoubleClick(stateMouse):
            if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(
                    250, lambda: UIFunction.maximize_restore(self))

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

        self.ui.bn_max.clicked.connect(
            lambda: UIFunction.maximize_restore(self))

        self.ui.bn_close.clicked.connect(lambda: self.close())

    def buttonPressed(self, buttonName):

        index = self.ui.stackedWidget.currentIndex()

        t = td.Thread(target=check_path, args=(os.getcwd(), 'token files'))
        t.start()

        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if buttonName == 'bn_home':
            # t = td.Thread(target=check_path, args=(os.getcwd(), 'token files'))
            # print("F")
            # t.start()
            print("F", login_status)

            # if not login_status:
            #     self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            #     self.ui.lab_tab.setText("Home")
            #     self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            # else:
            #     self.ui.stackedWidget.setCurrentWidget(self.ui.home_after_login)
            #     self.ui.lab_tab.setText("Home After Login")
            #     self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")

            UIFunction.initStackTab(self)

            # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            # elif self.ui.frame_bottom_west.width()==160  and index!=1:  # ABOUT PAGE STACKED WIDGET
            #     self.ui.stackedWidget.setCurrentWidget(self.ui.home_after_login)
            #     self.ui.lab_tab.setText("About > Home")
            #     self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName == 'bn_bug':
            if self.ui.frame_bottom_west.width() == 80 and index != 5:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_bug)
                self.ui.lab_tab.setText("Bug")
                # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)")

            elif self.ui.frame_bottom_west.width() == 160 and index != 4:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_bug)
                self.ui.lab_tab.setText("About > Bug")
                # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)")

        elif buttonName == 'bn_android':
            if(login_status==0):
                self.dialogexec("Warning", "Please Login to access this feature.", "icons/1x/errorAsset 55.png")
            else:
                if self.ui.frame_bottom_west.width() == 80 and index != 7:
                    self.ui.stackedWidget.setCurrentWidget(self.ui.page_download)
                    self.ui.lab_tab.setText("Android")
                    # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                    self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)")
                    # UIFunction.androidStackPages(self, "page_contact")

                elif self.ui.frame_bottom_west.width() == 160 and index != 3:   # ABOUT PAGE STACKED WIDGET
                    self.ui.stackedWidget.setCurrentWidget(
                        self.ui.page_about_android)
                    self.ui.lab_tab.setText("About > Android")
                    # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                    self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)")

        elif buttonName == 'bn_cloud':
            if self.ui.frame_bottom_west.width() == 80 and index != 6:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_cloud)
                self.ui.lab_tab.setText("Cloud")
                # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                self.ui.frame_cloud.setStyleSheet("background:rgb(91,90,90)")

            elif self.ui.frame_bottom_west.width() == 160 and index != 2:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(
                    self.ui.page_about_cloud)
                self.ui.lab_tab.setText("About > Cloud")
                # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                self.ui.frame_cloud.setStyleSheet("background:rgb(91,90,90)")

    # def getFilters(self):
    #     print(self.ui.email_from.text())
    #     print(self.ui.domain.text())
    #     print(self.ui.date.text())
    #     print(self.ui.unread.isChecked())

    # def isChecked(self):
    #     print(self.ui.unread.isChecked())
    # def clickChooseDirectory(self):
    #     x = choose_directory()
    #     self.ui.label_8.setText(x)
    def control(self):
        global clicked

        if(clicked==0):
            self.ui.label_13.setText(filters(
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
                self.ui.gDrive.isChecked()
            ))
            start_download(1)
            self.ui.save_attach.setText('Stop Download')
            self.ui.save_attach.setStyleSheet('background: rgb(255, 0, 0);\nfont: 10pt "MS Shell Dlg 2";')
            self.ui.save_attach.setIcon(QtGui.QIcon("icons/1x/pause.png"))
        else:
            stop_download(0)
            self.ui.save_attach.setText('Start Download')
            self.ui.save_attach.setStyleSheet('background: rgb(85, 255, 0); font: 75 10pt "MS Shell Dlg 2";')
            self.ui.save_attach.setIcon(QtGui.QIcon("icons/1x/play.png"))

        clicked =  1 - clicked

        print("clicked: ", clicked)


    def stackPage(self):

        self.ui.lab_home_main_hed.setText("About the Application")

        # self.ui.loginButton.clicked.connect(lambda: APFunction.login(self))

        # self.ui.logout.clicked.connect(lambda: APFunction.logout(self))

        self.ui.loginButton.clicked.connect(lambda: login())

        self.ui.logout.clicked.connect(lambda: logout())

        #self.ui.bn_bug_start.clicked.connect(lambda: APFunction.addNumbers(self, self.ui.comboBox_bug.currentText(), True))

        self.ui.save_attach.clicked.connect(
            lambda: UIFunction.control(self) 
            )
        

        self.ui.choose_directory.clicked.connect(
            # lambda: UIFunction.clickChooseDirectory(self)
            lambda: self.ui.label_8.setText(choose_directory())
            )

        # self.ui.applyFilters.clicked.connect(
        #     lambda: self.ui.label_9.setText(filters(
        #         self.ui.email_from.text(),
        #         self.ui.to.text(),
        #         self.ui.date_from.text(),
        #         self.ui.unread.isChecked(), 
        #         self.ui.localStorage.isChecked(), 
        #         self.ui.gDrive.isChecked()
        #     ))
        # )

        # self.ui.bn_cloud_connect.clicked.connect(
        #     lambda: APFunction.cloudConnect(self))
        # #self.ui.bn_cloud_clear.clicked.connect(lambda: self.dialogexec("Warning", "Do you want to save the file", "icons/1x/errorAsset 55.png", "Cancel", "Save"))
        # self.ui.bn_cloud_clear.clicked.connect(
        #     lambda: APFunction.cloudClear(self))

        # self.ui.bn_android_contact.clicked.connect(
        #     lambda: UIFunction.androidStackPages(self, "page_contact"))
        # self.ui.bn_android_game.clicked.connect(
        #     lambda: UIFunction.androidStackPages(self, "page_game"))
        # self.ui.bn_android_clean.clicked.connect(
        #     lambda: UIFunction.androidStackPages(self, "page_clean"))
        # self.ui.bn_android_world.clicked.connect(
        #     lambda: UIFunction.androidStackPages(self, "page_world"))

        # self.ui.new_downloads.clicked.connect(
        #     lambda: UIFunction.androidStackPages(self, "page_contact"))
        # self.ui.old_downloads.clicked.connect(
        #     lambda: UIFunction.androidStackPages(self, "page_game"))


        # self.ui.bn_android_clean.clicked.connect(
        #     lambda: UIFunction.androidStackPages(self, "page_clean"))
        # self.ui.bn_android_world.clicked.connect(
        #     lambda: UIFunction.androidStackPages(self, "page_world"))

        # self.ui.bn_android_contact_edit.clicked.connect(
        #     lambda: APFunction.editable(self))

        # self.ui.bn_android_contact_save.clicked.connect(
        #     lambda: APFunction.saveContact(self))


        

        ##########PAGE: ABOUT HOME #############
        # self.ui.text_about_home.setVerticalScrollBar(self.ui.vsb_about_home)
        # self.ui.text_about_home.setText(aboutHome)


    
    # def androidStackPages(self, page):
    #     for each in self.ui.frame_download_menu.findChildren(QFrame):
    #         each.setStyleSheet("background:rgb(51,51,51)")

    #     if page == "page_contact":
    #         self.ui.stackedWidget_android.setCurrentWidget(
    #             self.ui.page_new_download)
    #         self.ui.lab_tab.setText("Android > Contact")
    #         # self.ui.frame_android_contact.setStyleSheet(
    #         #     "background:rgb(91,90,90)")

    #     elif page == "page_game":
    #         self.ui.stackedWidget_android.setCurrentWidget(
    #             self.ui.page_android_game)
    #         self.ui.lab_tab.setText("Android > GamePad")
    #         # self.ui.frame_android_game.setStyleSheet(
    #         #     "background:rgb(91,90,90)")

    #     elif page == "page_clean":
    #         self.ui.stackedWidget_android.setCurrentWidget(
    #             self.ui.page_android_clean)
    #         self.ui.lab_tab.setText("Android > Clean")
    #         # self.ui.frame_android_clean.setStyleSheet(
    #         #     "background:rgb(91,90,90)")

    #     elif page == "page_world":
    #         self.ui.stackedWidget_android.setCurrentWidget(
    #             self.ui.page_android_world)
    #         self.ui.lab_tab.setText("Android > World")
    #         # self.ui.frame_android_world.setStyleSheet(
    #         #     "background:rgb(91,90,90)")
