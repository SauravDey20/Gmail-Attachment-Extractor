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
            if self.ui.frame_bottom_west.width() == 80 and index != 7:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_android)
                self.ui.lab_tab.setText("Android")
                # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)")
                UIFunction.androidStackPages(self, "page_contact")

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

    def stackPage(self):

        self.ui.lab_home_main_hed.setText("About the Application")

        # self.ui.loginButton.clicked.connect(lambda: APFunction.login(self))

        # self.ui.logout.clicked.connect(lambda: APFunction.logout(self))

        self.ui.loginButton.clicked.connect(lambda: login())

        self.ui.logout.clicked.connect(lambda: logout())

        #self.ui.bn_bug_start.clicked.connect(lambda: APFunction.addNumbers(self, self.ui.comboBox_bug.currentText(), True))

        self.ui.save_attach.clicked.connect(
            lambda: start_download(1))

        self.ui.stop_save_attach.clicked.connect(
            lambda: stop_download(0))

        self.ui.choose_directory.clicked.connect(
            lambda: choose_directory())

        self.ui.applyFilters.clicked.connect(
            lambda: filters(
                self.ui.email_from.text(),
                self.ui.domain.text(),
                self.ui.date.text(),
                self.ui.unread.isChecked(), 
                self.ui.localStorage.isChecked(), 
                self.ui.gDrive.isChecked()
            )
        )

        # self.ui.bn_cloud_connect.clicked.connect(
        #     lambda: APFunction.cloudConnect(self))
        # #self.ui.bn_cloud_clear.clicked.connect(lambda: self.dialogexec("Warning", "Do you want to save the file", "icons/1x/errorAsset 55.png", "Cancel", "Save"))
        # self.ui.bn_cloud_clear.clicked.connect(
        #     lambda: APFunction.cloudClear(self))

        self.ui.bn_android_contact.clicked.connect(
            lambda: UIFunction.androidStackPages(self, "page_contact"))
        self.ui.bn_android_game.clicked.connect(
            lambda: UIFunction.androidStackPages(self, "page_game"))
        self.ui.bn_android_clean.clicked.connect(
            lambda: UIFunction.androidStackPages(self, "page_clean"))
        self.ui.bn_android_world.clicked.connect(
            lambda: UIFunction.androidStackPages(self, "page_world"))

        self.ui.bn_android_contact_delete.clicked.connect(lambda: self.dialogexec(
            "Warning", "The Contact Infromtion will be Deleted, Do you want to continue.", "icons/1x/errorAsset 55.png", "Cancel", "Yes"))

        # self.ui.bn_android_contact_edit.clicked.connect(
        #     lambda: APFunction.editable(self))

        # self.ui.bn_android_contact_save.clicked.connect(
        #     lambda: APFunction.saveContact(self))

        self.ui.textEdit_gamepad.setVerticalScrollBar(
            self.ui.vsb_gamepad)   # SETTING THE TEXT FILED AREA A SCROLL BAR
        self.ui.textEdit_gamepad.setText(
            "Type Here Something, or paste something here")

        self.ui.horizontalSlider_2.valueChanged.connect(lambda: print(
            "Slider: Horizondal: ", self.ui.horizontalSlider_2.value()))  # CHECK WEATHER THE SLIDER IS MOVED OR NOT
        # WHEN THE CHECK BOX IS CHECKED IT ECECUTES THE ERROR BOX WITH MESSAGE.
        self.ui.checkBox.stateChanged.connect(lambda: self.errorexec(
            "Happy to Know you liked the UI", "icons/1x/smile2Asset 1.png", "Ok"))
        self.ui.checkBox_2.stateChanged.connect(lambda: self.errorexec(
            "Even More Happy to hear this", "icons/1x/smileAsset 1.png", "Ok"))

        ##########PAGE: ABOUT HOME #############
        # self.ui.text_about_home.setVerticalScrollBar(self.ui.vsb_about_home)
        # self.ui.text_about_home.setText(aboutHome)


    
    def androidStackPages(self, page):
        for each in self.ui.frame_android_menu.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if page == "page_contact":
            self.ui.stackedWidget_android.setCurrentWidget(
                self.ui.page_android_contact)
            self.ui.lab_tab.setText("Android > Contact")
            self.ui.frame_android_contact.setStyleSheet(
                "background:rgb(91,90,90)")

        elif page == "page_game":
            self.ui.stackedWidget_android.setCurrentWidget(
                self.ui.page_android_game)
            self.ui.lab_tab.setText("Android > GamePad")
            self.ui.frame_android_game.setStyleSheet(
                "background:rgb(91,90,90)")

        elif page == "page_clean":
            self.ui.stackedWidget_android.setCurrentWidget(
                self.ui.page_android_clean)
            self.ui.lab_tab.setText("Android > Clean")
            self.ui.frame_android_clean.setStyleSheet(
                "background:rgb(91,90,90)")

        elif page == "page_world":
            self.ui.stackedWidget_android.setCurrentWidget(
                self.ui.page_android_world)
            self.ui.lab_tab.setText("Android > World")
            self.ui.frame_android_world.setStyleSheet(
                "background:rgb(91,90,90)")



# class APFunction():

#     def __init__(self):
#         self.service = None


#     def login(self):
#         self.service = create_service('client-secret.json',
#                                  'gmail', 'v1', ['https://mail.google.com/'])

#     def logout(self):
#         shutil.rmtree(os.path.join(os.getcwd(), 'token files'))

#     def search_emails(self, query_string: str, label_ids: List = None):
#         try:
#             message_list_response = self.service.users().messages().list(
#                 userId='me',
#                 labelIds=label_ids,
#                 q=query_string
#             ).execute()

#             message_items = message_list_response.get('messages')
#             next_page_token = message_list_response.get('nextPageToken')
#             while next_page_token:
#                 message_list_response = self.service.users().messages().list(
#                     userId='me',
#                     labelIds=label_ids,
#                     q=query_string,
#                     pageToken=next_page_token
#                 ).execute()

#                 message_items.extend(message_list_response.get('messages'))
#                 next_page_token = message_list_response.get('nextPageToken')
#             return message_items
#         except Exception as e:
#             raise NoEmailFound('No emails returned')

#     def get_file_data(self, message_id, attachment_id, file_name, save_location):
#         response = self.service.users().messages().attachments().get(
#             userId='me',
#             messageId=message_id,
#             id=attachment_id
#         ).execute()

#         file_data = base64.urlsafe_b64decode(
#             response.get('data').encode('UTF-8'))
#         return file_data

#     def get_message_detail(self, message_id, msg_format='metadata', metadata_headers: List = None):
#         message_detail = self.service.users().messages().get(
#             userId='me',
#             id=message_id,
#             format=msg_format,
#             metadataHeaders=metadata_headers
#         ).execute()
#         return message_detail

#     def save_attachments(self):

#         query_string = 'is:unread has:attachment after:2022/9/7'
#         save_location = os.getcwd()
#         email_messages = APFunction.search_emails(self, query_string)

#         for email_message in email_messages:
#             messageDetail = APFunction.get_message_detail(self, 
#                 email_message['id'], msg_format='full', metadata_headers=['parts'])
#             messageDetailPayload = messageDetail.get('payload')

#             if 'parts' in messageDetailPayload:
#                 for msgPayload in messageDetailPayload['parts']:
#                     file_name = msgPayload['filename']
#                     body = msgPayload['body']
#                     if 'attachmentId' in body:
#                         attachment_id = body['attachmentId']
#                         attachment_content = APFunction.get_file_data(self, 
#                             email_message['id'], attachment_id, file_name, save_location)
#                         with open(os.path.join(save_location, file_name), 'wb') as _f:
#                             _f.write(attachment_content)
#                             print(
#                                 f'File {file_name} is saved at {save_location}')
#             time.sleep(0.5)


#     def start_download(self):
#         self.service = create_service('client-secret.json',
#                                  'gmail', 'v1', ['https://mail.google.com/'])

        
#         self.trd = td.Thread(target=self.save_attachments, args = () )
        
#         self.trd.start()
# #-----------------------------------------------------------------------------------------------------------------------

#     def addNumbers(self, number, enable):
#         if enable:
#             lastProgress = 0
#             for x in range(0, int(number), 1):
#                 progress = int((x/int(number))*100)
#                 if progress != lastProgress:
#                     self.ui.progressBar_bug.setValue(progress)
#                     lastProgress = progress
#             self.ui.progressBar_bug.setValue(100)

#     def cloudConnect(self):
#         self.ui.bn_cloud_clear.setEnabled(False)
#         textID = self.ui.line_cloud_id.text()
#         textADRESS = self.ui.line_cloud_adress.text()
#         if textID == 'asd' and textADRESS == '1234':
#             self.ui.line_cloud_adress.setText("")
#             self.ui.line_cloud_id.setText("")
#             self.ui.line_cloud_proxy.setText("Connection established")
#         else:
#             self.errorexec("Incorrect Credentials",
#                            "icons/1x/errorAsset 55.png", "Retry")

#     def cloudClear(self):
#         self.ui.line_cloud_proxy.setText("")
#         self.ui.line_cloud_adress.setText("")
#         self.ui.line_cloud_id.setText("")

#     def editable(self):
#         self.ui.line_android_name.setEnabled(True)
#         self.ui.line_android_adress.setEnabled(True)
#         self.ui.line_android_org.setEnabled(True)
#         self.ui.line_android_email.setEnabled(True)
#         self.ui.line_android_ph.setEnabled(True)

#         self.ui.bn_android_contact_save.setEnabled(True)
#         self.ui.bn_android_contact_edit.setEnabled(False)
#         self.ui.bn_android_contact_share.setEnabled(False)
#         self.ui.bn_android_contact_delete.setEnabled(False)

#     def saveContact(self):
#         self.ui.line_android_name.setEnabled(False)
#         self.ui.line_android_adress.setEnabled(False)
#         self.ui.line_android_org.setEnabled(False)
#         self.ui.line_android_email.setEnabled(False)
#         self.ui.line_android_ph.setEnabled(False)

#         self.ui.bn_android_contact_save.setEnabled(False)
#         self.ui.bn_android_contact_edit.setEnabled(True)
#         self.ui.bn_android_contact_share.setEnabled(True)
#         self.ui.bn_android_contact_delete.setEnabled(True)
