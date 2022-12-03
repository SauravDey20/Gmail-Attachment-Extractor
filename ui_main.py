# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1102, 818)
        MainWindow.setMinimumSize(QSize(800, 550))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background:rgb(91,90,90);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName("frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setStyleSheet("")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top_east = QFrame(self.frame_top)
        self.frame_top_east.setObjectName("frame_top_east")
        self.frame_top_east.setMaximumSize(QSize(16777215, 55))
        self.frame_top_east.setStyleSheet("background:rgb(0, 0, 0);")
        self.frame_top_east.setFrameShape(QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_appname = QFrame(self.frame_top_east)
        self.frame_appname.setObjectName("frame_appname")
        self.frame_appname.setFrameShape(QFrame.NoFrame)
        self.frame_appname.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_appname)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lab_appname = QLabel(self.frame_appname)
        self.lab_appname.setObjectName("lab_appname")
        font = QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.lab_appname.setFont(font)
        self.lab_appname.setStyleSheet("color:rgb(255,255,255);")

        self.horizontalLayout_10.addWidget(self.lab_appname)

        self.horizontalLayout_4.addWidget(self.frame_appname)

        self.frame_user = QFrame(self.frame_top_east)
        self.frame_user.setObjectName("frame_user")
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lab_user = QLabel(self.frame_user)
        self.lab_user.setObjectName("lab_user")
        self.lab_user.setFont(font)
        self.lab_user.setStyleSheet("color:rgb(255,255,255);")
        self.lab_user.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lab_user)

        self.horizontalLayout_4.addWidget(self.frame_user)

        self.frame_min = QFrame(self.frame_top_east)
        self.frame_min.setObjectName("frame_min")
        self.frame_min.setMinimumSize(QSize(55, 55))
        self.frame_min.setMaximumSize(QSize(55, 55))
        self.frame_min.setFrameShape(QFrame.NoFrame)
        self.frame_min.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_min)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bn_min = QPushButton(self.frame_min)
        self.bn_min.setObjectName("bn_min")
        self.bn_min.setMaximumSize(QSize(55, 55))
        self.bn_min.setStyleSheet(
            "QPushButton {\n"
            "	border: none;\n"
            "	background-color: rgba(0,0,0,0);\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(0,143,150);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgba(0,0,0,0);\n"
            "}"
        )
        icon = QIcon()
        icon.addFile("icons/1x/hideAsset 53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_min.setIcon(icon)
        self.bn_min.setIconSize(QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout_7.addWidget(self.bn_min)

        self.horizontalLayout_4.addWidget(self.frame_min)

        self.frame_max = QFrame(self.frame_top_east)
        self.frame_max.setObjectName("frame_max")
        self.frame_max.setMinimumSize(QSize(55, 55))
        self.frame_max.setMaximumSize(QSize(55, 55))
        self.frame_max.setFrameShape(QFrame.NoFrame)
        self.frame_max.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_max)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bn_max = QPushButton(self.frame_max)
        self.bn_max.setObjectName("bn_max")
        self.bn_max.setMaximumSize(QSize(55, 55))
        self.bn_max.setStyleSheet(
            "QPushButton {\n"
            "	border: none;\n"
            "	background-color: rgba(0,0,0,0);\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(0,143,150);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgba(0,0,0,0);\n"
            "}"
        )
        icon1 = QIcon()
        icon1.addFile("icons/1x/max.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_max.setIcon(icon1)
        self.bn_max.setIconSize(QSize(22, 22))
        self.bn_max.setFlat(True)

        self.horizontalLayout_6.addWidget(self.bn_max)

        self.horizontalLayout_4.addWidget(self.frame_max)

        self.frame_close = QFrame(self.frame_top_east)
        self.frame_close.setObjectName("frame_close")
        self.frame_close.setMinimumSize(QSize(55, 55))
        self.frame_close.setMaximumSize(QSize(55, 55))
        self.frame_close.setFrameShape(QFrame.NoFrame)
        self.frame_close.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bn_close = QPushButton(self.frame_close)
        self.bn_close.setObjectName("bn_close")
        self.bn_close.setMaximumSize(QSize(55, 55))
        self.bn_close.setStyleSheet(
            "QPushButton {\n"
            "	border: none;\n"
            "	background-color: rgba(0,0,0,0);\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(0,143,150);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgba(0,0,0,0);\n"
            "}"
        )
        icon2 = QIcon()
        icon2.addFile("icons/1x/closeAsset 43.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon2)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bn_close)

        self.horizontalLayout_4.addWidget(self.frame_close)

        self.horizontalLayout.addWidget(self.frame_top_east)

        self.verticalLayout.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName("frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_bottom)
        self.frame_bottom_west.setObjectName("frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet("background:rgb(0, 0, 0);")
        self.frame_bottom_west.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_home = QFrame(self.frame_bottom_west)
        self.frame_home.setObjectName("frame_home")
        self.frame_home.setMinimumSize(QSize(80, 55))
        self.frame_home.setMaximumSize(QSize(160, 55))
        self.frame_home.setFrameShape(QFrame.NoFrame)
        self.frame_home.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bn_home = QPushButton(self.frame_home)
        self.bn_home.setObjectName("bn_home")
        self.bn_home.setMinimumSize(QSize(80, 55))
        self.bn_home.setMaximumSize(QSize(160, 55))
        self.bn_home.setStyleSheet(
            "QPushButton {\n"
            "	border: none;\n"
            "	background-color: rgba(0,0,0,0);\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(91,90,90);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgba(0,0,0,0);\n"
            "}"
        )
        icon3 = QIcon()
        icon3.addFile("icons/1x/homeAsset 46.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_home.setIcon(icon3)
        self.bn_home.setIconSize(QSize(22, 22))
        self.bn_home.setFlat(True)

        self.horizontalLayout_15.addWidget(self.bn_home)

        self.verticalLayout_3.addWidget(self.frame_home)

        self.frame_cloud = QFrame(self.frame_bottom_west)
        self.frame_cloud.setObjectName("frame_cloud")
        self.frame_cloud.setMinimumSize(QSize(80, 55))
        self.frame_cloud.setMaximumSize(QSize(160, 55))
        self.frame_cloud.setFrameShape(QFrame.NoFrame)
        self.frame_cloud.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_cloud)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.bn_cloud = QPushButton(self.frame_cloud)
        self.bn_cloud.setObjectName("bn_cloud")
        self.bn_cloud.setMinimumSize(QSize(80, 55))
        self.bn_cloud.setMaximumSize(QSize(160, 55))
        self.bn_cloud.setStyleSheet(
            "QPushButton {\n"
            "	border: none;\n"
            "	background-color: rgba(0,0,0,0);\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(91,90,90);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgba(0,0,0,0);\n"
            "}"
        )
        icon4 = QIcon()
        icon4.addFile("icons/1x/t2t.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_cloud.setIcon(icon4)
        self.bn_cloud.setIconSize(QSize(22, 12))
        self.bn_cloud.setFlat(True)

        self.horizontalLayout_17.addWidget(self.bn_cloud)

        self.verticalLayout_3.addWidget(self.frame_cloud)

        self.frame_android = QFrame(self.frame_bottom_west)
        self.frame_android.setObjectName("frame_android")
        self.frame_android.setMinimumSize(QSize(80, 55))
        self.frame_android.setMaximumSize(QSize(160, 55))
        self.frame_android.setFrameShape(QFrame.NoFrame)
        self.frame_android.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_android)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.bn_android = QPushButton(self.frame_android)
        self.bn_android.setObjectName("bn_android")
        self.bn_android.setMinimumSize(QSize(80, 55))
        self.bn_android.setMaximumSize(QSize(160, 55))
        self.bn_android.setStyleSheet(
            "QPushButton {\n"
            "	border: none;\n"
            "	background-color: rgba(0,0,0,0);\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(91,90,90);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgba(0,0,0,0);\n"
            "}"
        )
        icon5 = QIcon()
        icon5.addFile("icons/1x/smile2Asset 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_android.setIcon(icon5)
        self.bn_android.setIconSize(QSize(20, 22))
        self.bn_android.setFlat(True)

        self.horizontalLayout_18.addWidget(self.bn_android)

        self.verticalLayout_3.addWidget(self.frame_android)

        self.frame_8 = QFrame(self.frame_bottom_west)
        self.frame_8.setObjectName("frame_8")
        self.frame_8.setStyleSheet("color:rgb(255,255,255);")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_8)

        self.horizontalLayout_2.addWidget(self.frame_bottom_west)

        self.frame_bottom_east = QFrame(self.frame_bottom)
        self.frame_bottom_east.setObjectName("frame_bottom_east")
        self.frame_bottom_east.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 55))
        self.stackedWidget.setStyleSheet("")
        self.page_home = QWidget()
        self.page_home.setObjectName("page_home")
        self.page_home.setStyleSheet("background:rgb(24, 24, 24);")
        self.horizontalLayout_19 = QHBoxLayout(self.page_home)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 5, 0, 5)
        self.frame_home_main = QFrame(self.page_home)
        self.frame_home_main.setObjectName("frame_home_main")
        self.frame_home_main.setStyleSheet("background:rgb(24, 24, 24);")
        self.frame_home_main.setFrameShape(QFrame.NoFrame)
        self.frame_home_main.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame_home_main)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.lab_home_main_hed = QLabel(self.frame_home_main)
        self.lab_home_main_hed.setObjectName("lab_home_main_hed")
        self.lab_home_main_hed.setMinimumSize(QSize(0, 55))
        self.lab_home_main_hed.setMaximumSize(QSize(16777215, 55))
        font1 = QFont()
        font1.setFamily("Arial")
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.lab_home_main_hed.setFont(font1)
        self.lab_home_main_hed.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 75 18pt "Arial";'
        )
        self.lab_home_main_hed.setTextFormat(Qt.RichText)

        self.verticalLayout_5.addWidget(self.lab_home_main_hed)

        self.lab_home_main_disc = QLabel(self.frame_home_main)
        self.lab_home_main_disc.setObjectName("lab_home_main_disc")
        self.lab_home_main_disc.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lab_home_main_disc.sizePolicy().hasHeightForWidth()
        )
        self.lab_home_main_disc.setSizePolicy(sizePolicy)
        self.lab_home_main_disc.setFont(font1)
        self.lab_home_main_disc.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 75 18pt "Arial";'
        )
        self.lab_home_main_disc.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop
        )
        self.lab_home_main_disc.setWordWrap(True)
        self.lab_home_main_disc.setMargin(5)

        self.verticalLayout_5.addWidget(self.lab_home_main_disc)

        self.loginButton = QPushButton(self.frame_home_main)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 181, 251, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color: rgb(0, 0, 0);\n"
            'font: 75 10pt "Arial";'
        )
        self.loginButton.setIconSize(QSize(40, 30))

        self.verticalLayout_5.addWidget(self.loginButton)

        self.horizontalLayout_19.addWidget(self.frame_home_main)

        self.vert_divide = QFrame(self.page_home)
        self.vert_divide.setObjectName("vert_divide")
        self.vert_divide.setStyleSheet("")
        self.vert_divide.setFrameShape(QFrame.VLine)
        self.vert_divide.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.vert_divide)

        self.stackedWidget.addWidget(self.page_home)
        self.home_after_login = QWidget()
        self.home_after_login.setObjectName("home_after_login")
        self.home_after_login.setStyleSheet("background:rgb(24, 24, 24);")
        self.verticalLayout_13 = QVBoxLayout(self.home_after_login)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.lab_about_home = QLabel(self.home_after_login)
        self.lab_about_home.setObjectName("lab_about_home")
        self.lab_about_home.setMinimumSize(QSize(0, 55))
        self.lab_about_home.setMaximumSize(QSize(16777215, 55))
        self.lab_about_home.setFont(font1)
        self.lab_about_home.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 75 18pt "Arial";'
        )

        self.verticalLayout_13.addWidget(self.lab_about_home)

        self.frame_4 = QFrame(self.home_after_login)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.logout = QPushButton(self.frame_4)
        self.logout.setObjectName("logout")
        self.logout.setGeometry(QRect(400, 440, 221, 51))
        self.logout.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:1, y1:0.023, x2:1, y2:0, stop:0 rgba(220, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color: rgb(0, 0, 0);\n"
            'font: 75 10pt "Arial";'
        )

        self.verticalLayout_13.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.home_after_login)
        self.page_about_cloud = QWidget()
        self.page_about_cloud.setObjectName("page_about_cloud")
        self.page_about_cloud.setStyleSheet("background:rgb(91,90,90);")
        self.horizontalLayout_29 = QHBoxLayout(self.page_about_cloud)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.stackedWidget.addWidget(self.page_about_cloud)
        self.page_about_android = QWidget()
        self.page_about_android.setObjectName("page_about_android")
        self.page_about_android.setStyleSheet("background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_android)
        self.page_about_bug = QWidget()
        self.page_about_bug.setObjectName("page_about_bug")
        self.page_about_bug.setStyleSheet("background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_bug)
        self.page_bug_ = QWidget()
        self.page_bug_.setObjectName("page_bug_")
        self.page_bug_.setStyleSheet("background:rgb(74, 200, 175)")
        self.verticalLayout_7 = QVBoxLayout(self.page_bug_)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget.addWidget(self.page_bug_)
        self.page_cloud = QWidget()
        self.page_cloud.setObjectName("page_cloud")
        self.page_cloud.setStyleSheet("background:rgb(91,90,90);")
        self.verticalLayout_8 = QVBoxLayout(self.page_cloud)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.frame_2 = QFrame(self.page_cloud)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setStyleSheet("background:rgb(24, 24, 24);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.download_table = QTableWidget(self.frame_2)
        if self.download_table.columnCount() < 3:
            self.download_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.download_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.download_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.download_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.download_table.setObjectName("download_table")
        self.download_table.setGeometry(QRect(0, 0, 1011, 731))
        self.download_table.setStyleSheet("color: rgb(1, 175, 255);")

        self.verticalLayout_8.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_cloud)
        self.page_download = QWidget()
        self.page_download.setObjectName("page_download")
        self.page_download.setStyleSheet("background:rgb(91,90,90);")
        self.verticalLayout_9 = QVBoxLayout(self.page_download)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_android = QStackedWidget(self.page_download)
        self.stackedWidget_android.setObjectName("stackedWidget_android")
        self.stackedWidget_android.setStyleSheet("background:rgb(91,90,90);")
        self.page_new_download = QWidget()
        self.page_new_download.setObjectName("page_new_download")
        self.page_new_download.setStyleSheet("background:rgb(24, 24, 24);")
        self.verticalLayout_10 = QVBoxLayout(self.page_new_download)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.frame_3 = QFrame(self.page_new_download)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet("background:rgb(24, 24, 24);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gDrive = QCheckBox(self.frame_3)
        self.gDrive.setObjectName("gDrive")
        self.gDrive.setGeometry(QRect(510, 390, 201, 20))
        self.gDrive.setStyleSheet("color: rgb(255, 255, 255);\n" 'font: 10pt "Arial";')
        self.unread = QCheckBox(self.frame_3)
        self.unread.setObjectName("unread")
        self.unread.setGeometry(QRect(520, 80, 191, 31))
        self.unread.setStyleSheet("color: rgb(255, 255, 255);\n" 'font: 10pt "Arial";')
        self.lab_Bug = QLabel(self.frame_3)
        self.lab_Bug.setObjectName("lab_Bug")
        self.lab_Bug.setEnabled(True)
        self.lab_Bug.setGeometry(QRect(0, 0, 401, 55))
        self.lab_Bug.setMinimumSize(QSize(0, 55))
        self.lab_Bug.setMaximumSize(QSize(16777215, 55))
        self.lab_Bug.setFont(font1)
        self.lab_Bug.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 75 18pt "Arial";'
        )
        self.choose_directory = QPushButton(self.frame_3)
        self.choose_directory.setObjectName("choose_directory")
        self.choose_directory.setGeometry(QRect(320, 460, 211, 41))
        self.choose_directory.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            'font: 10pt "Arial";\n'
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(141, 0, 131, 255), stop:1 rgba(255, 255, 255, 255))"
        )
        self.save_attach = QPushButton(self.frame_3)
        self.save_attach.setObjectName("save_attach")
        self.save_attach.setEnabled(False)
        self.save_attach.setGeometry(QRect(310, 580, 231, 81))
        self.save_attach.setAutoFillBackground(False)
        self.save_attach.setStyleSheet(
            "background: rgb(85, 255, 0);\n" 'font: 75 10pt "MS Shell Dlg 2";'
        )
        icon6 = QIcon()
        icon6.addFile("icons/1x/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_attach.setIcon(icon6)
        self.localStorage = QCheckBox(self.frame_3)
        self.localStorage.setObjectName("localStorage")
        self.localStorage.setGeometry(QRect(200, 390, 231, 20))
        self.localStorage.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 10pt "Arial";'
        )
        self.email_from = QLineEdit(self.frame_3)
        self.email_from.setObjectName("email_from")
        self.email_from.setEnabled(True)
        self.email_from.setGeometry(QRect(120, 70, 341, 41))
        self.email_from.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 9pt "Arial";'
        )
        self.to = QLineEdit(self.frame_3)
        self.to.setObjectName("to")
        self.to.setGeometry(QRect(120, 130, 341, 41))
        self.to.setStyleSheet("color: rgb(255, 255, 255);\n" 'font: 9pt "Arial";')
        self.label = QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 80, 51, 21))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n" 'font: 10pt "Arial";')
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(10, 140, 31, 21))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n" 'font: 10pt "Arial";')
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(520, 240, 51, 21))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n" 'font: 10pt "Arial";')
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(520, 290, 71, 21))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n" 'font: 10pt "Arial";')
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(320, 520, 461, 31))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n" 'font: 9pt "Arial";')
        self.date_from = QDateTimeEdit(self.frame_3)
        self.date_from.setObjectName("date_from")
        self.date_from.setGeometry(QRect(590, 230, 201, 41))
        self.date_from.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 9pt "Arial";'
        )
        self.date_from.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.date_upto = QDateTimeEdit(self.frame_3)
        self.date_upto.setObjectName("date_upto")
        self.date_upto.setGeometry(QRect(590, 280, 201, 41))
        self.date_upto.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 9pt "Arial";'
        )
        self.date_upto.setDateTime(QDateTime(QDate(2022, 12, 31), QTime(0, 0, 0)))
        self.date_upto.setMaximumDateTime(
            QDateTime(QDate(2100, 12, 31), QTime(23, 59, 59))
        )
        self.date_upto.setMaximumDate(QDate(2100, 12, 31))
        self.date_upto.setMinimumDate(QDate(2000, 9, 14))
        self.read = QCheckBox(self.frame_3)
        self.read.setObjectName("read")
        self.read.setGeometry(QRect(740, 80, 161, 31))
        self.read.setStyleSheet("color: rgb(255, 255, 255);\n" 'font: 10pt "Arial";')
        self.subject = QLineEdit(self.frame_3)
        self.subject.setObjectName("subject")
        self.subject.setGeometry(QRect(120, 180, 341, 41))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.subject.sizePolicy().hasHeightForWidth())
        self.subject.setSizePolicy(sizePolicy1)
        self.subject.setStyleSheet("color: rgb(255, 255, 255);\n" 'font: 9pt "Arial";')
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(10, 190, 81, 21))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n" 'font: 10pt "Arial";')
        self.has_words = QLineEdit(self.frame_3)
        self.has_words.setObjectName("has_words")
        self.has_words.setGeometry(QRect(120, 240, 341, 41))
        sizePolicy1.setHeightForWidth(self.has_words.sizePolicy().hasHeightForWidth())
        self.has_words.setSizePolicy(sizePolicy1)
        self.has_words.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 9pt "Arial";'
        )
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QRect(10, 250, 81, 21))
        self.label_11.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 10pt "Arial";'
        )
        self.doesnt_have = QLineEdit(self.frame_3)
        self.doesnt_have.setObjectName("doesnt_have")
        self.doesnt_have.setGeometry(QRect(120, 300, 341, 41))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.doesnt_have.sizePolicy().hasHeightForWidth())
        self.doesnt_have.setSizePolicy(sizePolicy2)
        self.doesnt_have.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 9pt "Arial";'
        )
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName("label_12")
        self.label_12.setGeometry(QRect(10, 300, 101, 31))
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 10pt "Arial";'
        )
        self.upcoming = QRadioButton(self.frame_3)
        self.upcoming.setObjectName("upcoming")
        self.upcoming.setGeometry(QRect(610, 160, 151, 20))
        self.upcoming.setStyleSheet(
            "color: rgb(255, 255, 255);\n" 'font: 10pt "Arial";'
        )

        self.verticalLayout_10.addWidget(self.frame_3)

        self.stackedWidget_android.addWidget(self.page_new_download)
        self.page_android_game = QWidget()
        self.page_android_game.setObjectName("page_android_game")
        self.page_android_game.setStyleSheet("background:rgb(91,90,90);")
        self.verticalLayout_11 = QVBoxLayout(self.page_android_game)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.lab_gamepad = QLabel(self.page_android_game)
        self.lab_gamepad.setObjectName("lab_gamepad")
        self.lab_gamepad.setMinimumSize(QSize(0, 55))
        self.lab_gamepad.setMaximumSize(QSize(16777215, 55))
        font2 = QFont()
        font2.setFamily("Segoe UI")
        font2.setPointSize(24)
        self.lab_gamepad.setFont(font2)
        self.lab_gamepad.setStyleSheet("color:rgb(255,255,255);")

        self.verticalLayout_11.addWidget(self.lab_gamepad)

        self.frame_textbar = QFrame(self.page_android_game)
        self.frame_textbar.setObjectName("frame_textbar")
        self.frame_textbar.setStyleSheet("background:rgb(91,90,90);")
        self.frame_textbar.setFrameShape(QFrame.StyledPanel)
        self.frame_textbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_textbar)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 0, 0, 0)
        self.textEdit_gamepad = QTextEdit(self.frame_textbar)
        self.textEdit_gamepad.setObjectName("textEdit_gamepad")
        font3 = QFont()
        font3.setFamily("Segoe UI")
        font3.setPointSize(12)
        self.textEdit_gamepad.setFont(font3)
        self.textEdit_gamepad.setStyleSheet("color:rgb(255,255,255);")
        self.textEdit_gamepad.setFrameShape(QFrame.NoFrame)
        self.textEdit_gamepad.setFrameShadow(QFrame.Plain)
        self.textEdit_gamepad.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit_gamepad.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_26.addWidget(self.textEdit_gamepad)

        self.verticalLayout_11.addWidget(self.frame_textbar)

        self.stackedWidget_android.addWidget(self.page_android_game)
        self.page_android_clean = QWidget()
        self.page_android_clean.setObjectName("page_android_clean")
        self.page_android_clean.setStyleSheet("background:rgb(91,90,90);")
        self.gridLayout_5 = QGridLayout(self.page_android_clean)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget_android.addWidget(self.page_android_clean)
        self.page_android_world = QWidget()
        self.page_android_world.setObjectName("page_android_world")
        self.page_android_world.setStyleSheet("background:rgb(91,90,90);")
        self.horizontalLayout_27 = QHBoxLayout(self.page_android_world)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.stackedWidget_android.addWidget(self.page_android_world)

        self.verticalLayout_9.addWidget(self.stackedWidget_android)

        self.stackedWidget.addWidget(self.page_download)

        self.horizontalLayout_14.addWidget(self.stackedWidget)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_low = QFrame(self.frame_bottom_east)
        self.frame_low.setObjectName("frame_low")
        self.frame_low.setMinimumSize(QSize(0, 20))
        self.frame_low.setMaximumSize(QSize(16777215, 20))
        self.frame_low.setStyleSheet("")
        self.frame_low.setFrameShape(QFrame.NoFrame)
        self.frame_low.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_tab = QFrame(self.frame_low)
        self.frame_tab.setObjectName("frame_tab")
        font4 = QFont()
        font4.setFamily("Segoe UI")
        self.frame_tab.setFont(font4)
        self.frame_tab.setStyleSheet("background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lab_tab = QLabel(self.frame_tab)
        self.lab_tab.setObjectName("lab_tab")
        font5 = QFont()
        font5.setFamily("Segoe UI Light")
        font5.setPointSize(10)
        self.lab_tab.setFont(font5)
        self.lab_tab.setStyleSheet("background:rgb(24, 24, 24);")

        self.horizontalLayout_12.addWidget(self.lab_tab)

        self.horizontalLayout_11.addWidget(self.frame_tab)

        self.frame_drag = QFrame(self.frame_low)
        self.frame_drag.setObjectName("frame_drag")
        self.frame_drag.setMinimumSize(QSize(20, 20))
        self.frame_drag.setMaximumSize(QSize(20, 20))
        self.frame_drag.setStyleSheet("background:rgb(24, 24, 24);")
        self.frame_drag.setFrameShape(QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.frame_drag)

        self.verticalLayout_2.addWidget(self.frame_low)

        self.horizontalLayout_2.addWidget(self.frame_bottom_east)

        self.verticalLayout.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(7)
        self.stackedWidget_android.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.lab_appname.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        self.lab_user.setText(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>010-035-803</p></body></html>",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.bn_min.setToolTip(
            QCoreApplication.translate("MainWindow", "Minimize", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.bn_min.setText("")
        # if QT_CONFIG(tooltip)
        self.bn_max.setToolTip(
            QCoreApplication.translate("MainWindow", "Maximize", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.bn_max.setText("")
        # if QT_CONFIG(tooltip)
        self.bn_close.setToolTip(
            QCoreApplication.translate("MainWindow", "Close", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.bn_close.setText("")
        # if QT_CONFIG(tooltip)
        self.bn_home.setToolTip(QCoreApplication.translate("MainWindow", "Home", None))
        # endif // QT_CONFIG(tooltip)
        self.bn_home.setText("")
        # if QT_CONFIG(tooltip)
        self.bn_cloud.setToolTip(
            QCoreApplication.translate("MainWindow", "Filters", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.bn_cloud.setText("")
        # if QT_CONFIG(tooltip)
        self.bn_android.setToolTip(
            QCoreApplication.translate("MainWindow", "Live Downloads", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.bn_android.setText("")
        self.lab_home_main_hed.setText(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>About the Application</p></body></html>",
                None,
            )
        )
        self.lab_home_main_disc.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Segoe UI\'; font-size:10pt;">This App will download G-Mail Attachments for you. But first, you need to login through your google account</span></p>\n'
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:10pt;\"><br /></p></body></html>",
                None,
            )
        )
        self.loginButton.setText(
            QCoreApplication.translate("MainWindow", "Google Login", None)
        )
        self.lab_about_home.setText(
            QCoreApplication.translate("MainWindow", "Home", None)
        )
        self.logout.setText(
            QCoreApplication.translate("MainWindow", "Click to Logout", None)
        )
        ___qtablewidgetitem = self.download_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", "From", None)
        )
        ___qtablewidgetitem1 = self.download_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", "File Name", None)
        )
        ___qtablewidgetitem2 = self.download_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", "Download Location", None)
        )
        self.gDrive.setText(
            QCoreApplication.translate("MainWindow", "Upload to Google Drive", None)
        )
        self.unread.setText(
            QCoreApplication.translate("MainWindow", "Only Unread Mails", None)
        )
        self.lab_Bug.setText(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>Extract Attachments</p></body></html>",
                None,
            )
        )
        self.choose_directory.setText(
            QCoreApplication.translate("MainWindow", "Select Download Directory", None)
        )
        self.save_attach.setText(
            QCoreApplication.translate("MainWindow", "Start", None)
        )
        self.localStorage.setText(
            QCoreApplication.translate("MainWindow", "Download To Local Storage", None)
        )
        self.label.setText(QCoreApplication.translate("MainWindow", "FROM:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", "TO:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "From:", None))
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", "Up Until:", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", "No directory chosen", None)
        )
        self.date_from.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "dd-MM-yyyy HH:mm:ss", None)
        )
        self.date_upto.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "dd-MM-yyyy HH:mm:ss", None)
        )
        self.read.setText(
            QCoreApplication.translate("MainWindow", "Only Read Mails", None)
        )
        self.label_9.setText(QCoreApplication.translate("MainWindow", "SUBJECT:", None))
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", "Has Words:", None)
        )
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", "Doesn't Have:", None)
        )
        self.upcoming.setText(
            QCoreApplication.translate("MainWindow", "Upcoming Mails", None)
        )
        self.lab_gamepad.setText(
            QCoreApplication.translate("MainWindow", "GamePad", None)
        )
        self.lab_tab.setText(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(
            QCoreApplication.translate("MainWindow", "Drag", None)
        )


# endif // QT_CONFIG(tooltip)
# retranslateUi
