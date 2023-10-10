# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LED_Zappelin.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
import resources_rc
import resources_rc
import resources_rc
import resources_rc
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 760)
        MainWindow.setMinimumSize(QSize(20, 20))
        MainWindow.setStyleSheet(u"/* --- General Settings --- */\n"
"*{\n"
"	border:none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin:0;\n"
"	color: rgb(147,161,161);    \n"
"}\n"
"#centralwidget{\n"
"	background-color:  rgb(0, 43, 54);\n"
"}\n"
"\n"
"\n"
"/* --- Top Frame --- */\n"
"\n"
"#TopMainFrame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#AppName_Frame QPushButton:hover{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"\n"
"\n"
"/* --- Bottom Frame --- */\n"
"\n"
"#BottomMainFrame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"\n"
"/* --- Menu Frame --- */\n"
"\n"
"#Menu_Frame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#Menu_Frame QPushButton{\n"
"	text-align: left;\n"
"	padding: 10px 5px;\n"
"	border-top-left-radius:15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#Menu_Frame QPushButton:hover{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"#HideSubMenu_Frame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"\n"
""
                        "/* --- LED Zappelin' --- */\n"
"\n"
"#LEDZap_frame Line{\n"
" border: 1px solid rgb(147,161,161);\n"
"}\n"
"#LEDZap_Frame QPushButton{\n"
"	background-color: rgb(7, 54, 66);\n"
"    border: 1px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"    padding: 0px 10px;\n"
"}\n"
"\n"
"#LEDZap_Frame QPushButton:hover{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"\n"
"#LED_Zap_Display_Frame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"\n"
"/* --- Chrolis --- */\n"
"\n"
"#Chrolis_Frame QPushButton{\n"
"	background-color: rgb(7, 54, 66);\n"
"    border: 1px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"    padding: 0px 10px;\n"
"}\n"
"#Chrolis_Frame QPushButton:hover{\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"\n"
"#Chrolis_Display_Frame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"\n"
"/* --- Spectra --- */\n"
"\n"
"#Spectra_RightMenu_container QPushButton:hover{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"#Spectra_RightMenu_container QPushButton{\n"
"	text-align: l"
                        "eft;\n"
"	padding: 20px 0px;\n"
"	border-top-right-radius:20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	background-color: rgb(0, 43, 54);\n"
"}\n"
"#Spectra_RightMenu_container{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"#Spectra_CenterMenu_Hide_frame{\n"
"	background-color: rgb(0, 30, 38);\n"
"}\n"
"\n"
"#OpsinSpectra_frame QPushButton{\n"
"	background-color: rgb(0, 43, 54);\n"
"	border: 2px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"}\n"
"#LEDSpectra_frame QPushButton{\n"
"	background-color: rgb(0, 43, 54);\n"
"	border: 2px solid rgb(147,161,161);\n"
"	border-radius: 10px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TopMainFrame = QFrame(self.centralwidget)
        self.TopMainFrame.setObjectName(u"TopMainFrame")
        self.TopMainFrame.setMinimumSize(QSize(0, 40))
        self.TopMainFrame.setMaximumSize(QSize(16777215, 40))
        self.TopMainFrame.setFrameShape(QFrame.StyledPanel)
        self.TopMainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.TopMainFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Header_Frame = QFrame(self.TopMainFrame)
        self.Header_Frame.setObjectName(u"Header_Frame")
        self.Header_Frame.setFrameShape(QFrame.StyledPanel)
        self.Header_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Header_Frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.AppName_Frame = QFrame(self.Header_Frame)
        self.AppName_Frame.setObjectName(u"AppName_Frame")
        self.AppName_Frame.setFrameShape(QFrame.StyledPanel)
        self.AppName_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.AppName_Frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 0, 0, 0)
        self.AppName_pushButton = QPushButton(self.AppName_Frame)
        self.AppName_pushButton.setObjectName(u"AppName_pushButton")
        font = QFont()
        font.setPointSize(16)
        self.AppName_pushButton.setFont(font)

        self.horizontalLayout_4.addWidget(self.AppName_pushButton)


        self.horizontalLayout.addWidget(self.AppName_Frame, 0, Qt.AlignLeft)

        self.AppButton_Frame = QFrame(self.Header_Frame)
        self.AppButton_Frame.setObjectName(u"AppButton_Frame")
        self.AppButton_Frame.setFrameShape(QFrame.StyledPanel)
        self.AppButton_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.AppButton_Frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Reduce_pushButton = QPushButton(self.AppButton_Frame)
        self.Reduce_pushButton.setObjectName(u"Reduce_pushButton")
        icon = QIcon()
        icon.addFile(u":/resources/resources/Artboard 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Reduce_pushButton.setIcon(icon)
        self.Reduce_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.Reduce_pushButton)

        self.Expand_pushButton = QPushButton(self.AppButton_Frame)
        self.Expand_pushButton.setObjectName(u"Expand_pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/resources/resources/Expand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Expand_pushButton.setIcon(icon1)
        self.Expand_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.Expand_pushButton)

        self.Exit_pushButton = QPushButton(self.AppButton_Frame)
        self.Exit_pushButton.setObjectName(u"Exit_pushButton")
        icon2 = QIcon()
        icon2.addFile(u":/resources/resources/Exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Exit_pushButton.setIcon(icon2)
        self.Exit_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.Exit_pushButton)


        self.horizontalLayout.addWidget(self.AppButton_Frame, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.Header_Frame)


        self.verticalLayout.addWidget(self.TopMainFrame)

        self.CenterMainFrame = QFrame(self.centralwidget)
        self.CenterMainFrame.setObjectName(u"CenterMainFrame")
        self.CenterMainFrame.setFrameShape(QFrame.StyledPanel)
        self.CenterMainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.CenterMainFrame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Menu_Frame = QFrame(self.CenterMainFrame)
        self.Menu_Frame.setObjectName(u"Menu_Frame")
        self.Menu_Frame.setMaximumSize(QSize(40, 16777215))
        self.Menu_Frame.setFrameShape(QFrame.StyledPanel)
        self.Menu_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Menu_Frame)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 15)
        self.DropMenu_Frame = QFrame(self.Menu_Frame)
        self.DropMenu_Frame.setObjectName(u"DropMenu_Frame")
        self.DropMenu_Frame.setFrameShape(QFrame.StyledPanel)
        self.DropMenu_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.DropMenu_Frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.DropMenu_pushButton = QPushButton(self.DropMenu_Frame)
        self.DropMenu_pushButton.setObjectName(u"DropMenu_pushButton")
        font1 = QFont()
        font1.setPointSize(12)
        self.DropMenu_pushButton.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/resources/resources/MenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DropMenu_pushButton.setIcon(icon3)
        self.DropMenu_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.DropMenu_pushButton)


        self.verticalLayout_2.addWidget(self.DropMenu_Frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.Menus_Frame = QFrame(self.Menu_Frame)
        self.Menus_Frame.setObjectName(u"Menus_Frame")
        self.Menus_Frame.setFrameShape(QFrame.StyledPanel)
        self.Menus_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Menus_Frame)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.LEDZappelin_pushButton = QPushButton(self.Menus_Frame)
        self.LEDZappelin_pushButton.setObjectName(u"LEDZappelin_pushButton")
        self.LEDZappelin_pushButton.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/resources/resources/LEDZap.png", QSize(), QIcon.Normal, QIcon.Off)
        self.LEDZappelin_pushButton.setIcon(icon4)
        self.LEDZappelin_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.LEDZappelin_pushButton)

        self.Chrolis_pushButton = QPushButton(self.Menus_Frame)
        self.Chrolis_pushButton.setObjectName(u"Chrolis_pushButton")
        self.Chrolis_pushButton.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/resources/resources/Chrolis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Chrolis_pushButton.setIcon(icon5)
        self.Chrolis_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.Chrolis_pushButton)

        self.Stimulus_pushButton = QPushButton(self.Menus_Frame)
        self.Stimulus_pushButton.setObjectName(u"Stimulus_pushButton")
        self.Stimulus_pushButton.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/resources/resources/Stimulus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stimulus_pushButton.setIcon(icon6)
        self.Stimulus_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.Stimulus_pushButton)

        self.Spectra_pushButton = QPushButton(self.Menus_Frame)
        self.Spectra_pushButton.setObjectName(u"Spectra_pushButton")
        self.Spectra_pushButton.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u":/resources/resources/Spectra.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Spectra_pushButton.setIcon(icon7)
        self.Spectra_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.Spectra_pushButton)


        self.verticalLayout_2.addWidget(self.Menus_Frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.Options_Frame = QFrame(self.Menu_Frame)
        self.Options_Frame.setObjectName(u"Options_Frame")
        self.Options_Frame.setFrameShape(QFrame.StyledPanel)
        self.Options_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Options_Frame)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Settings_pushButton = QPushButton(self.Options_Frame)
        self.Settings_pushButton.setObjectName(u"Settings_pushButton")
        self.Settings_pushButton.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u":/resources/resources/Settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Settings_pushButton.setIcon(icon8)
        self.Settings_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.Settings_pushButton)

        self.About_pushButton = QPushButton(self.Options_Frame)
        self.About_pushButton.setObjectName(u"About_pushButton")
        self.About_pushButton.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u":/resources/resources/About.png", QSize(), QIcon.Normal, QIcon.Off)
        self.About_pushButton.setIcon(icon9)
        self.About_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.About_pushButton)

        self.Help_pushButton = QPushButton(self.Options_Frame)
        self.Help_pushButton.setObjectName(u"Help_pushButton")
        self.Help_pushButton.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/resources/resources/Help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Help_pushButton.setIcon(icon10)
        self.Help_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.Help_pushButton)

        self.GitHub_pushButton = QPushButton(self.Options_Frame)
        self.GitHub_pushButton.setObjectName(u"GitHub_pushButton")
        self.GitHub_pushButton.setFont(font1)
        icon11 = QIcon()
        icon11.addFile(u":/resources/resources/GitHub.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GitHub_pushButton.setIcon(icon11)
        self.GitHub_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.GitHub_pushButton)


        self.verticalLayout_2.addWidget(self.Options_Frame)


        self.horizontalLayout_10.addWidget(self.Menu_Frame)

        self.SubMenu_Frame = QFrame(self.CenterMainFrame)
        self.SubMenu_Frame.setObjectName(u"SubMenu_Frame")
        self.SubMenu_Frame.setMinimumSize(QSize(200, 0))
        self.SubMenu_Frame.setMaximumSize(QSize(200, 16777215))
        self.SubMenu_Frame.setFrameShape(QFrame.StyledPanel)
        self.SubMenu_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.SubMenu_Frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.HideSubMenu_Frame = QFrame(self.SubMenu_Frame)
        self.HideSubMenu_Frame.setObjectName(u"HideSubMenu_Frame")
        self.HideSubMenu_Frame.setFrameShape(QFrame.StyledPanel)
        self.HideSubMenu_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.HideSubMenu_Frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.HideSubFrame_pushButton = QPushButton(self.HideSubMenu_Frame)
        self.HideSubFrame_pushButton.setObjectName(u"HideSubFrame_pushButton")
        self.HideSubFrame_pushButton.setMinimumSize(QSize(0, 30))
        self.HideSubFrame_pushButton.setFont(font1)
        self.HideSubFrame_pushButton.setLayoutDirection(Qt.RightToLeft)
        icon12 = QIcon()
        icon12.addFile(u":/resources/resources/DropMenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HideSubFrame_pushButton.setIcon(icon12)
        self.HideSubFrame_pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.HideSubFrame_pushButton, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.HideSubMenu_Frame)

        self.stackedWidget = QStackedWidget(self.SubMenu_Frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(200, 0))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_10.addWidget(self.SubMenu_Frame)

        self.MainContent_Frame = QFrame(self.CenterMainFrame)
        self.MainContent_Frame.setObjectName(u"MainContent_Frame")
        self.MainContent_Frame.setFrameShape(QFrame.StyledPanel)
        self.MainContent_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.MainContent_Frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Main_stackedWidget = QStackedWidget(self.MainContent_Frame)
        self.Main_stackedWidget.setObjectName(u"Main_stackedWidget")
        self.Main_stackedWidget.setFont(font1)
        self.Home_Page = QWidget()
        self.Home_Page.setObjectName(u"Home_Page")
        self.verticalLayout_36 = QVBoxLayout(self.Home_Page)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.Home_Header_Frame = QFrame(self.Home_Page)
        self.Home_Header_Frame.setObjectName(u"Home_Header_Frame")
        self.Home_Header_Frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Header_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.Home_Header_Frame)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(10, 0, 10, 0)
        self.Home_Logo_frame = QFrame(self.Home_Header_Frame)
        self.Home_Logo_frame.setObjectName(u"Home_Logo_frame")
        self.Home_Logo_frame.setMinimumSize(QSize(200, 125))
        self.Home_Logo_frame.setMaximumSize(QSize(200, 125))
        self.Home_Logo_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Logo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_113 = QHBoxLayout(self.Home_Logo_frame)
        self.horizontalLayout_113.setSpacing(0)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.Home_Logo = QLabel(self.Home_Logo_frame)
        self.Home_Logo.setObjectName(u"Home_Logo")
        self.Home_Logo.setPixmap(QPixmap(u":/resources/resources/SpikyLogo.png"))
        self.Home_Logo.setScaledContents(True)

        self.horizontalLayout_113.addWidget(self.Home_Logo)


        self.horizontalLayout_35.addWidget(self.Home_Logo_frame)

        self.Home_Title_frame = QFrame(self.Home_Header_Frame)
        self.Home_Title_frame.setObjectName(u"Home_Title_frame")
        self.Home_Title_frame.setMinimumSize(QSize(0, 200))
        self.Home_Title_frame.setMaximumSize(QSize(16777215, 200))
        self.Home_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_114 = QHBoxLayout(self.Home_Title_frame)
        self.horizontalLayout_114.setSpacing(0)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.Home_Title = QLabel(self.Home_Title_frame)
        self.Home_Title.setObjectName(u"Home_Title")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Home_Title.sizePolicy().hasHeightForWidth())
        self.Home_Title.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setBold(False)
        self.Home_Title.setFont(font2)
        self.Home_Title.setStyleSheet(u"")

        self.horizontalLayout_114.addWidget(self.Home_Title)


        self.horizontalLayout_35.addWidget(self.Home_Title_frame)


        self.verticalLayout_36.addWidget(self.Home_Header_Frame, 0, Qt.AlignTop)

        self.Home_Main_Frame = QFrame(self.Home_Page)
        self.Home_Main_Frame.setObjectName(u"Home_Main_Frame")
        self.Home_Main_Frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Main_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_115 = QHBoxLayout(self.Home_Main_Frame)
        self.horizontalLayout_115.setSpacing(10)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(10, 0, 10, 10)
        self.Home_Main_Text_frame = QFrame(self.Home_Main_Frame)
        self.Home_Main_Text_frame.setObjectName(u"Home_Main_Text_frame")
        self.Home_Main_Text_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Main_Text_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.Home_Main_Text_frame)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.Home_Main_Text = QLabel(self.Home_Main_Text_frame)
        self.Home_Main_Text.setObjectName(u"Home_Main_Text")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Home_Main_Text.sizePolicy().hasHeightForWidth())
        self.Home_Main_Text.setSizePolicy(sizePolicy1)
        self.Home_Main_Text.setAlignment(Qt.AlignCenter)
        self.Home_Main_Text.setWordWrap(True)

        self.verticalLayout_38.addWidget(self.Home_Main_Text)


        self.horizontalLayout_115.addWidget(self.Home_Main_Text_frame)

        self.Home_Main_Illustration_frame = QFrame(self.Home_Main_Frame)
        self.Home_Main_Illustration_frame.setObjectName(u"Home_Main_Illustration_frame")
        self.Home_Main_Illustration_frame.setMinimumSize(QSize(500, 0))
        self.Home_Main_Illustration_frame.setMaximumSize(QSize(500, 16777215))
        self.Home_Main_Illustration_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Main_Illustration_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.Home_Main_Illustration_frame)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 50)
        self.Home_Main_Illustration_Title_frame = QFrame(self.Home_Main_Illustration_frame)
        self.Home_Main_Illustration_Title_frame.setObjectName(u"Home_Main_Illustration_Title_frame")
        self.Home_Main_Illustration_Title_frame.setMinimumSize(QSize(500, 40))
        self.Home_Main_Illustration_Title_frame.setMaximumSize(QSize(500, 40))
        self.Home_Main_Illustration_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Main_Illustration_Title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.Home_Main_Illustration_Title_frame)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.Home_Main_Illustration_Title = QLabel(self.Home_Main_Illustration_Title_frame)
        self.Home_Main_Illustration_Title.setObjectName(u"Home_Main_Illustration_Title")
        self.Home_Main_Illustration_Title.setMinimumSize(QSize(0, 40))
        self.Home_Main_Illustration_Title.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setItalic(True)
        self.Home_Main_Illustration_Title.setFont(font3)

        self.verticalLayout_40.addWidget(self.Home_Main_Illustration_Title, 0, Qt.AlignHCenter)


        self.verticalLayout_39.addWidget(self.Home_Main_Illustration_Title_frame, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.Home_Main_Illustration_Image_frame = QFrame(self.Home_Main_Illustration_frame)
        self.Home_Main_Illustration_Image_frame.setObjectName(u"Home_Main_Illustration_Image_frame")
        self.Home_Main_Illustration_Image_frame.setMaximumSize(QSize(500, 350))
        self.Home_Main_Illustration_Image_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Main_Illustration_Image_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_116 = QHBoxLayout(self.Home_Main_Illustration_Image_frame)
        self.horizontalLayout_116.setSpacing(0)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.Home_Main_Illustration_Image = QLabel(self.Home_Main_Illustration_Image_frame)
        self.Home_Main_Illustration_Image.setObjectName(u"Home_Main_Illustration_Image")
        self.Home_Main_Illustration_Image.setMaximumSize(QSize(500, 350))
        self.Home_Main_Illustration_Image.setStyleSheet(u"")
        self.Home_Main_Illustration_Image.setFrameShape(QFrame.NoFrame)
        self.Home_Main_Illustration_Image.setFrameShadow(QFrame.Plain)
        self.Home_Main_Illustration_Image.setLineWidth(1)
        self.Home_Main_Illustration_Image.setPixmap(QPixmap(u":/resources/resources/DarkSideOfTheRetina.png"))
        self.Home_Main_Illustration_Image.setScaledContents(True)

        self.horizontalLayout_116.addWidget(self.Home_Main_Illustration_Image)


        self.verticalLayout_39.addWidget(self.Home_Main_Illustration_Image_frame)


        self.horizontalLayout_115.addWidget(self.Home_Main_Illustration_frame)


        self.verticalLayout_36.addWidget(self.Home_Main_Frame)

        self.Main_stackedWidget.addWidget(self.Home_Page)
        self.LEDZap_Page = QWidget()
        self.LEDZap_Page.setObjectName(u"LEDZap_Page")
        self.verticalLayout_7 = QVBoxLayout(self.LEDZap_Page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Frame = QFrame(self.LEDZap_Page)
        self.LEDZap_Frame.setObjectName(u"LEDZap_Frame")
        self.LEDZap_Frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.LEDZap_Frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_MainContent_Frame = QFrame(self.LEDZap_Frame)
        self.LEDZap_MainContent_Frame.setObjectName(u"LEDZap_MainContent_Frame")
        self.LEDZap_MainContent_Frame.setMinimumSize(QSize(0, 0))
        self.LEDZap_MainContent_Frame.setMaximumSize(QSize(16777215, 16777215))
        self.LEDZap_MainContent_Frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_MainContent_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.LEDZap_MainContent_Frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Connect_Frame = QFrame(self.LEDZap_MainContent_Frame)
        self.LEDZap_Connect_Frame.setObjectName(u"LEDZap_Connect_Frame")
        self.LEDZap_Connect_Frame.setMinimumSize(QSize(0, 50))
        self.LEDZap_Connect_Frame.setMaximumSize(QSize(16777215, 50))
        self.LEDZap_Connect_Frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Connect_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.LEDZap_Connect_Frame)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.LEDZap_SelectPortLabel = QLabel(self.LEDZap_Connect_Frame)
        self.LEDZap_SelectPortLabel.setObjectName(u"LEDZap_SelectPortLabel")
        self.LEDZap_SelectPortLabel.setFont(font1)

        self.horizontalLayout_14.addWidget(self.LEDZap_SelectPortLabel, 0, Qt.AlignHCenter)

        self.LEDZap_SelectPortComboBox = QComboBox(self.LEDZap_Connect_Frame)
        self.LEDZap_SelectPortComboBox.addItem("")
        self.LEDZap_SelectPortComboBox.setObjectName(u"LEDZap_SelectPortComboBox")

        self.horizontalLayout_14.addWidget(self.LEDZap_SelectPortComboBox)

        self.LEDZap_ConnectButton = QPushButton(self.LEDZap_Connect_Frame)
        self.LEDZap_ConnectButton.setObjectName(u"LEDZap_ConnectButton")
        self.LEDZap_ConnectButton.setEnabled(True)
        self.LEDZap_ConnectButton.setFont(font1)
        self.LEDZap_ConnectButton.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.LEDZap_ConnectButton)


        self.verticalLayout_8.addWidget(self.LEDZap_Connect_Frame)

        self.LEDZap_ProxyLED_frame = QFrame(self.LEDZap_MainContent_Frame)
        self.LEDZap_ProxyLED_frame.setObjectName(u"LEDZap_ProxyLED_frame")
        self.LEDZap_ProxyLED_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_ProxyLED_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.LEDZap_ProxyLED_frame)
        self.horizontalLayout_137.setSpacing(5)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_ProxyLED_empty_frame = QFrame(self.LEDZap_ProxyLED_frame)
        self.LEDZap_ProxyLED_empty_frame.setObjectName(u"LEDZap_ProxyLED_empty_frame")
        self.LEDZap_ProxyLED_empty_frame.setMinimumSize(QSize(300, 0))
        self.LEDZap_ProxyLED_empty_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_ProxyLED_empty_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_137.addWidget(self.LEDZap_ProxyLED_empty_frame)

        self.LEDZap_ProxyLED_label = QLabel(self.LEDZap_ProxyLED_frame)
        self.LEDZap_ProxyLED_label.setObjectName(u"LEDZap_ProxyLED_label")
        font4 = QFont()
        font4.setPointSize(10)
        self.LEDZap_ProxyLED_label.setFont(font4)

        self.horizontalLayout_137.addWidget(self.LEDZap_ProxyLED_label, 0, Qt.AlignTop)

        self.LEDZap_ProxyLED_Slider = QSlider(self.LEDZap_ProxyLED_frame)
        self.LEDZap_ProxyLED_Slider.setObjectName(u"LEDZap_ProxyLED_Slider")
        self.LEDZap_ProxyLED_Slider.setMaximum(255)
        self.LEDZap_ProxyLED_Slider.setPageStep(25)
        self.LEDZap_ProxyLED_Slider.setValue(100)
        self.LEDZap_ProxyLED_Slider.setOrientation(Qt.Horizontal)
        self.LEDZap_ProxyLED_Slider.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_137.addWidget(self.LEDZap_ProxyLED_Slider)

        self.LEDZap_ProxyLED_value = QLabel(self.LEDZap_ProxyLED_frame)
        self.LEDZap_ProxyLED_value.setObjectName(u"LEDZap_ProxyLED_value")
        self.LEDZap_ProxyLED_value.setMinimumSize(QSize(50, 0))
        self.LEDZap_ProxyLED_value.setFont(font1)
        self.LEDZap_ProxyLED_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_137.addWidget(self.LEDZap_ProxyLED_value, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.LEDZap_ProxyLED_frame)

        self.LED_Zap_Display_Frame = QFrame(self.LEDZap_MainContent_Frame)
        self.LED_Zap_Display_Frame.setObjectName(u"LED_Zap_Display_Frame")
        self.LED_Zap_Display_Frame.setMinimumSize(QSize(0, 100))
        self.LED_Zap_Display_Frame.setFrameShape(QFrame.StyledPanel)
        self.LED_Zap_Display_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.LED_Zap_Display_Frame)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.LED_Zap_Display_stackedWidget = QStackedWidget(self.LED_Zap_Display_Frame)
        self.LED_Zap_Display_stackedWidget.setObjectName(u"LED_Zap_Display_stackedWidget")
        self.LED_Zap_Display_page1 = QWidget()
        self.LED_Zap_Display_page1.setObjectName(u"LED_Zap_Display_page1")
        self.verticalLayout_30 = QVBoxLayout(self.LED_Zap_Display_page1)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 2, 0, 0)
        self.LED_Zap_Display1_pushButton_frame = QFrame(self.LED_Zap_Display_page1)
        self.LED_Zap_Display1_pushButton_frame.setObjectName(u"LED_Zap_Display1_pushButton_frame")
        self.LED_Zap_Display1_pushButton_frame.setMinimumSize(QSize(0, 20))
        self.LED_Zap_Display1_pushButton_frame.setMaximumSize(QSize(16777215, 20))
        self.LED_Zap_Display1_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.LED_Zap_Display1_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.LED_Zap_Display1_pushButton_frame)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 5, 0)
        self.LED_Zap_Display1_pushButton = QPushButton(self.LED_Zap_Display1_pushButton_frame)
        self.LED_Zap_Display1_pushButton.setObjectName(u"LED_Zap_Display1_pushButton")
        self.LED_Zap_Display1_pushButton.setMinimumSize(QSize(150, 20))
        self.LED_Zap_Display1_pushButton.setMaximumSize(QSize(150, 20))

        self.verticalLayout_34.addWidget(self.LED_Zap_Display1_pushButton, 0, Qt.AlignRight)


        self.verticalLayout_30.addWidget(self.LED_Zap_Display1_pushButton_frame)

        self.LED_Zap_Display1 = PlotWidget(self.LED_Zap_Display_page1)
        self.LED_Zap_Display1.setObjectName(u"LED_Zap_Display1")
        self.LED_Zap_Display1.setMinimumSize(QSize(0, 0))
        self.LEDZap_Display1_Layout = QVBoxLayout(self.LED_Zap_Display1)
        self.LEDZap_Display1_Layout.setSpacing(0)
        self.LEDZap_Display1_Layout.setObjectName(u"LEDZap_Display1_Layout")
        self.LEDZap_Display1_Layout.setContentsMargins(0, 2, 0, 0)

        self.verticalLayout_30.addWidget(self.LED_Zap_Display1)

        self.LED_Zap_Display_stackedWidget.addWidget(self.LED_Zap_Display_page1)
        self.LED_Zap_Display_page2 = QWidget()
        self.LED_Zap_Display_page2.setObjectName(u"LED_Zap_Display_page2")
        self.aaa = QVBoxLayout(self.LED_Zap_Display_page2)
        self.aaa.setSpacing(0)
        self.aaa.setObjectName(u"aaa")
        self.aaa.setContentsMargins(0, 2, 0, 0)
        self.LED_Zap_Display2_pushButton_frame = QFrame(self.LED_Zap_Display_page2)
        self.LED_Zap_Display2_pushButton_frame.setObjectName(u"LED_Zap_Display2_pushButton_frame")
        self.LED_Zap_Display2_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.LED_Zap_Display2_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.LED_Zap_Display2_pushButton_frame)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 5, 0)
        self.LED_Zap_Display2_pushButton = QPushButton(self.LED_Zap_Display2_pushButton_frame)
        self.LED_Zap_Display2_pushButton.setObjectName(u"LED_Zap_Display2_pushButton")
        self.LED_Zap_Display2_pushButton.setMinimumSize(QSize(150, 20))
        self.LED_Zap_Display2_pushButton.setMaximumSize(QSize(150, 20))

        self.verticalLayout_33.addWidget(self.LED_Zap_Display2_pushButton, 0, Qt.AlignRight)


        self.aaa.addWidget(self.LED_Zap_Display2_pushButton_frame, 0, Qt.AlignTop)

        self.LED_Zap_Display2 = QFrame(self.LED_Zap_Display_page2)
        self.LED_Zap_Display2.setObjectName(u"LED_Zap_Display2")
        self.LED_Zap_Display2.setFrameShape(QFrame.StyledPanel)
        self.LED_Zap_Display2.setFrameShadow(QFrame.Raised)
        self.LEDZap_Display2_Layout = QVBoxLayout(self.LED_Zap_Display2)
        self.LEDZap_Display2_Layout.setSpacing(0)
        self.LEDZap_Display2_Layout.setObjectName(u"LEDZap_Display2_Layout")
        self.LEDZap_Display2_Layout.setContentsMargins(0, 2, 0, 0)

        self.aaa.addWidget(self.LED_Zap_Display2)

        self.LED_Zap_Display_stackedWidget.addWidget(self.LED_Zap_Display_page2)

        self.verticalLayout_25.addWidget(self.LED_Zap_Display_stackedWidget)


        self.verticalLayout_8.addWidget(self.LED_Zap_Display_Frame)

        self.LED_Zap_Serial_Frame = QFrame(self.LEDZap_MainContent_Frame)
        self.LED_Zap_Serial_Frame.setObjectName(u"LED_Zap_Serial_Frame")
        self.LED_Zap_Serial_Frame.setMinimumSize(QSize(0, 60))
        self.LED_Zap_Serial_Frame.setMaximumSize(QSize(16777215, 60))
        self.LED_Zap_Serial_Frame.setFrameShape(QFrame.StyledPanel)
        self.LED_Zap_Serial_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.LED_Zap_Serial_Frame)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.LED_Zap_Serial = QWidget(self.LED_Zap_Serial_Frame)
        self.LED_Zap_Serial.setObjectName(u"LED_Zap_Serial")
        self.LED_Zap_Serial.setMinimumSize(QSize(0, 0))
        self.LED_Zap_Serial.setMaximumSize(QSize(16777215, 16777215))
        self.LED_Zap_Serial.setStyleSheet(u"background-color: rgb(0,12,15);")
        self.verticalLayout_27 = QVBoxLayout(self.LED_Zap_Serial)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(10, 0, 10, 0)
        self.LED_Zap_Serial_label = QLabel(self.LED_Zap_Serial)
        self.LED_Zap_Serial_label.setObjectName(u"LED_Zap_Serial_label")
        self.LED_Zap_Serial_label.setFont(font1)
        self.LED_Zap_Serial_label.setWordWrap(True)

        self.verticalLayout_27.addWidget(self.LED_Zap_Serial_label)


        self.verticalLayout_26.addWidget(self.LED_Zap_Serial)


        self.verticalLayout_8.addWidget(self.LED_Zap_Serial_Frame, 0, Qt.AlignBottom)


        self.horizontalLayout_13.addWidget(self.LEDZap_MainContent_Frame)

        self.line_2 = QFrame(self.LEDZap_Frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_2)

        self.LEDZap_Stimulus_frame = QFrame(self.LEDZap_Frame)
        self.LEDZap_Stimulus_frame.setObjectName(u"LEDZap_Stimulus_frame")
        self.LEDZap_Stimulus_frame.setMaximumSize(QSize(400, 16777215))
        self.LEDZap_Stimulus_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Stimulus_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.LEDZap_Stimulus_frame)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 5)
        self.LEDZap_StimulusControl_frame = QFrame(self.LEDZap_Stimulus_frame)
        self.LEDZap_StimulusControl_frame.setObjectName(u"LEDZap_StimulusControl_frame")
        self.LEDZap_StimulusControl_frame.setMinimumSize(QSize(0, 100))
        self.LEDZap_StimulusControl_frame.setMaximumSize(QSize(16777215, 16777215))
        self.LEDZap_StimulusControl_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_StimulusControl_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.LEDZap_StimulusControl_frame)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 5, 5, 0)
        self.LEDZap_Load_frame = QFrame(self.LEDZap_StimulusControl_frame)
        self.LEDZap_Load_frame.setObjectName(u"LEDZap_Load_frame")
        self.LEDZap_Load_frame.setFont(font1)
        self.LEDZap_Load_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Load_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.LEDZap_Load_frame)
        self.horizontalLayout_59.setSpacing(10)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Load_pushButton_frame = QFrame(self.LEDZap_Load_frame)
        self.LEDZap_Load_pushButton_frame.setObjectName(u"LEDZap_Load_pushButton_frame")
        self.LEDZap_Load_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.LEDZap_Load_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Load_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.LEDZap_Load_pushButton_frame)
        self.horizontalLayout_80.setSpacing(0)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Load_pushButton = QPushButton(self.LEDZap_Load_pushButton_frame)
        self.LEDZap_Load_pushButton.setObjectName(u"LEDZap_Load_pushButton")
        self.LEDZap_Load_pushButton.setMinimumSize(QSize(100, 0))
        self.LEDZap_Load_pushButton.setMaximumSize(QSize(100, 16777215))
        self.LEDZap_Load_pushButton.setFont(font1)
        self.LEDZap_Load_pushButton.setCheckable(True)

        self.horizontalLayout_80.addWidget(self.LEDZap_Load_pushButton)


        self.horizontalLayout_59.addWidget(self.LEDZap_Load_pushButton_frame)

        self.LEDZap_Stimulus_Label_frame = QFrame(self.LEDZap_Load_frame)
        self.LEDZap_Stimulus_Label_frame.setObjectName(u"LEDZap_Stimulus_Label_frame")
        self.LEDZap_Stimulus_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Stimulus_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.LEDZap_Stimulus_Label_frame)
        self.horizontalLayout_79.setSpacing(0)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Stimulus_Label = QLabel(self.LEDZap_Stimulus_Label_frame)
        self.LEDZap_Stimulus_Label.setObjectName(u"LEDZap_Stimulus_Label")
        self.LEDZap_Stimulus_Label.setMinimumSize(QSize(0, 25))
        self.LEDZap_Stimulus_Label.setMaximumSize(QSize(275, 25))
        font5 = QFont()
        font5.setPointSize(8)
        self.LEDZap_Stimulus_Label.setFont(font5)
        self.LEDZap_Stimulus_Label.setScaledContents(True)
        self.LEDZap_Stimulus_Label.setWordWrap(True)

        self.horizontalLayout_79.addWidget(self.LEDZap_Stimulus_Label)


        self.horizontalLayout_59.addWidget(self.LEDZap_Stimulus_Label_frame)


        self.verticalLayout_16.addWidget(self.LEDZap_Load_frame)

        self.LEDZap_StimulusMain_frame = QFrame(self.LEDZap_StimulusControl_frame)
        self.LEDZap_StimulusMain_frame.setObjectName(u"LEDZap_StimulusMain_frame")
        self.LEDZap_StimulusMain_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_StimulusMain_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_141 = QHBoxLayout(self.LEDZap_StimulusMain_frame)
        self.horizontalLayout_141.setSpacing(0)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Stimulus_Left_frame = QFrame(self.LEDZap_StimulusMain_frame)
        self.LEDZap_Stimulus_Left_frame.setObjectName(u"LEDZap_Stimulus_Left_frame")
        self.LEDZap_Stimulus_Left_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Stimulus_Left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.LEDZap_Stimulus_Left_frame)
        self.verticalLayout_96.setSpacing(10)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Display_pushButton_frame = QFrame(self.LEDZap_Stimulus_Left_frame)
        self.LEDZap_Display_pushButton_frame.setObjectName(u"LEDZap_Display_pushButton_frame")
        self.LEDZap_Display_pushButton_frame.setMinimumSize(QSize(125, 0))
        self.LEDZap_Display_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.LEDZap_Display_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Display_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.LEDZap_Display_pushButton_frame)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Display_pushButton = QPushButton(self.LEDZap_Display_pushButton_frame)
        self.LEDZap_Display_pushButton.setObjectName(u"LEDZap_Display_pushButton")
        self.LEDZap_Display_pushButton.setMinimumSize(QSize(100, 0))
        self.LEDZap_Display_pushButton.setMaximumSize(QSize(100, 16777215))
        self.LEDZap_Display_pushButton.setFont(font1)
        self.LEDZap_Display_pushButton.setCheckable(True)

        self.horizontalLayout_83.addWidget(self.LEDZap_Display_pushButton)


        self.verticalLayout_96.addWidget(self.LEDZap_Display_pushButton_frame)

        self.LEDZap_Test_pushButton_frame = QFrame(self.LEDZap_Stimulus_Left_frame)
        self.LEDZap_Test_pushButton_frame.setObjectName(u"LEDZap_Test_pushButton_frame")
        self.LEDZap_Test_pushButton_frame.setMinimumSize(QSize(125, 0))
        self.LEDZap_Test_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.LEDZap_Test_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Test_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.LEDZap_Test_pushButton_frame)
        self.horizontalLayout_139.setSpacing(0)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Test_pushButton = QPushButton(self.LEDZap_Test_pushButton_frame)
        self.LEDZap_Test_pushButton.setObjectName(u"LEDZap_Test_pushButton")
        self.LEDZap_Test_pushButton.setMinimumSize(QSize(100, 0))
        self.LEDZap_Test_pushButton.setMaximumSize(QSize(100, 16777215))
        self.LEDZap_Test_pushButton.setFont(font1)

        self.horizontalLayout_139.addWidget(self.LEDZap_Test_pushButton)


        self.verticalLayout_96.addWidget(self.LEDZap_Test_pushButton_frame)


        self.horizontalLayout_141.addWidget(self.LEDZap_Stimulus_Left_frame)

        self.LEDZap_Stimulus_Right_frame = QFrame(self.LEDZap_StimulusMain_frame)
        self.LEDZap_Stimulus_Right_frame.setObjectName(u"LEDZap_Stimulus_Right_frame")
        self.LEDZap_Stimulus_Right_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Stimulus_Right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.LEDZap_Stimulus_Right_frame)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Stimulus_Play_frame = QFrame(self.LEDZap_Stimulus_Right_frame)
        self.LEDZap_Stimulus_Play_frame.setObjectName(u"LEDZap_Stimulus_Play_frame")
        self.LEDZap_Stimulus_Play_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Stimulus_Play_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.LEDZap_Stimulus_Play_frame)
        self.horizontalLayout_46.setSpacing(10)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Start_pushButton_frame = QFrame(self.LEDZap_Stimulus_Play_frame)
        self.LEDZap_Start_pushButton_frame.setObjectName(u"LEDZap_Start_pushButton_frame")
        self.LEDZap_Start_pushButton_frame.setMinimumSize(QSize(125, 0))
        self.LEDZap_Start_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.LEDZap_Start_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Start_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.LEDZap_Start_pushButton_frame)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Start_pushButton = QPushButton(self.LEDZap_Start_pushButton_frame)
        self.LEDZap_Start_pushButton.setObjectName(u"LEDZap_Start_pushButton")
        self.LEDZap_Start_pushButton.setMinimumSize(QSize(125, 0))
        self.LEDZap_Start_pushButton.setMaximumSize(QSize(125, 16777215))
        self.LEDZap_Start_pushButton.setFont(font1)
        self.LEDZap_Start_pushButton.setCheckable(True)

        self.horizontalLayout_81.addWidget(self.LEDZap_Start_pushButton)


        self.horizontalLayout_46.addWidget(self.LEDZap_Start_pushButton_frame)

        self.LEDZap_Stop_pushButton_frame = QFrame(self.LEDZap_Stimulus_Play_frame)
        self.LEDZap_Stop_pushButton_frame.setObjectName(u"LEDZap_Stop_pushButton_frame")
        self.LEDZap_Stop_pushButton_frame.setMinimumSize(QSize(125, 0))
        self.LEDZap_Stop_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.LEDZap_Stop_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Stop_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.LEDZap_Stop_pushButton_frame)
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Stop_pushButton = QPushButton(self.LEDZap_Stop_pushButton_frame)
        self.LEDZap_Stop_pushButton.setObjectName(u"LEDZap_Stop_pushButton")
        self.LEDZap_Stop_pushButton.setMinimumSize(QSize(125, 0))
        self.LEDZap_Stop_pushButton.setMaximumSize(QSize(125, 16777215))
        self.LEDZap_Stop_pushButton.setFont(font1)
        self.LEDZap_Stop_pushButton.setCheckable(True)

        self.horizontalLayout_82.addWidget(self.LEDZap_Stop_pushButton)


        self.horizontalLayout_46.addWidget(self.LEDZap_Stop_pushButton_frame)


        self.verticalLayout_97.addWidget(self.LEDZap_Stimulus_Play_frame)

        self.LEDZap_NumbeofLoop_frame = QFrame(self.LEDZap_Stimulus_Right_frame)
        self.LEDZap_NumbeofLoop_frame.setObjectName(u"LEDZap_NumbeofLoop_frame")
        self.LEDZap_NumbeofLoop_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_NumbeofLoop_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.LEDZap_NumbeofLoop_frame)
        self.horizontalLayout_140.setSpacing(0)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_NumbeofLoop_Label_frame = QFrame(self.LEDZap_NumbeofLoop_frame)
        self.LEDZap_NumbeofLoop_Label_frame.setObjectName(u"LEDZap_NumbeofLoop_Label_frame")
        self.LEDZap_NumbeofLoop_Label_frame.setMinimumSize(QSize(125, 0))
        self.LEDZap_NumbeofLoop_Label_frame.setMaximumSize(QSize(125, 16777215))
        self.LEDZap_NumbeofLoop_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_NumbeofLoop_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.LEDZap_NumbeofLoop_Label_frame)
        self.horizontalLayout_142.setSpacing(0)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_NumbeofLoop_Label = QLabel(self.LEDZap_NumbeofLoop_Label_frame)
        self.LEDZap_NumbeofLoop_Label.setObjectName(u"LEDZap_NumbeofLoop_Label")
        self.LEDZap_NumbeofLoop_Label.setMaximumSize(QSize(1752, 16777215))
        self.LEDZap_NumbeofLoop_Label.setFont(font4)

        self.horizontalLayout_142.addWidget(self.LEDZap_NumbeofLoop_Label, 0, Qt.AlignRight)


        self.horizontalLayout_140.addWidget(self.LEDZap_NumbeofLoop_Label_frame, 0, Qt.AlignHCenter)

        self.LEDZap_NumbeofLoop_lineEdit_frame = QFrame(self.LEDZap_NumbeofLoop_frame)
        self.LEDZap_NumbeofLoop_lineEdit_frame.setObjectName(u"LEDZap_NumbeofLoop_lineEdit_frame")
        self.LEDZap_NumbeofLoop_lineEdit_frame.setMinimumSize(QSize(125, 0))
        self.LEDZap_NumbeofLoop_lineEdit_frame.setMaximumSize(QSize(125, 16777215))
        self.LEDZap_NumbeofLoop_lineEdit_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_NumbeofLoop_lineEdit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.LEDZap_NumbeofLoop_lineEdit_frame)
        self.horizontalLayout_143.setSpacing(0)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_NumbeofLoop = QLineEdit(self.LEDZap_NumbeofLoop_lineEdit_frame)
        self.LEDZap_NumbeofLoop.setObjectName(u"LEDZap_NumbeofLoop")
        self.LEDZap_NumbeofLoop.setMinimumSize(QSize(100, 0))
        self.LEDZap_NumbeofLoop.setMaximumSize(QSize(100, 16777215))
        self.LEDZap_NumbeofLoop.setFont(font1)
        self.LEDZap_NumbeofLoop.setStyleSheet(u" border: 1px solid rgb(147,161,161);\n"
"background-color: rgb(7, 54, 66);")
        self.LEDZap_NumbeofLoop.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_143.addWidget(self.LEDZap_NumbeofLoop)


        self.horizontalLayout_140.addWidget(self.LEDZap_NumbeofLoop_lineEdit_frame, 0, Qt.AlignHCenter)


        self.verticalLayout_97.addWidget(self.LEDZap_NumbeofLoop_frame)


        self.horizontalLayout_141.addWidget(self.LEDZap_Stimulus_Right_frame)


        self.verticalLayout_16.addWidget(self.LEDZap_StimulusMain_frame)


        self.verticalLayout_9.addWidget(self.LEDZap_StimulusControl_frame)

        self.line = QFrame(self.LEDZap_Stimulus_frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line)

        self.LEDZap_LED_frame = QFrame(self.LEDZap_Stimulus_frame)
        self.LEDZap_LED_frame.setObjectName(u"LEDZap_LED_frame")
        self.LEDZap_LED_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_LED_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.LEDZap_LED_frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 0, 5, 5)
        self.LEDZap_All_LED_frame = QFrame(self.LEDZap_LED_frame)
        self.LEDZap_All_LED_frame.setObjectName(u"LEDZap_All_LED_frame")
        self.LEDZap_All_LED_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_All_LED_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.LEDZap_All_LED_frame)
        self.horizontalLayout_31.setSpacing(5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.All_LED_Display_frame = QFrame(self.LEDZap_All_LED_frame)
        self.All_LED_Display_frame.setObjectName(u"All_LED_Display_frame")
        self.All_LED_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.All_LED_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.All_LED_Display_frame.setFrameShadow(QFrame.Raised)
        self.All_toggleButton_layout = QHBoxLayout(self.All_LED_Display_frame)
        self.All_toggleButton_layout.setSpacing(0)
        self.All_toggleButton_layout.setObjectName(u"All_toggleButton_layout")
        self.All_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.All_LED_label = QLabel(self.All_LED_Display_frame)
        self.All_LED_label.setObjectName(u"All_LED_label")
        self.All_LED_label.setMaximumSize(QSize(125, 16777215))
        self.All_LED_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.All_toggleButton_layout.addWidget(self.All_LED_label)


        self.horizontalLayout_31.addWidget(self.All_LED_Display_frame)

        self.All_LED_Slider_frame = QFrame(self.LEDZap_All_LED_frame)
        self.All_LED_Slider_frame.setObjectName(u"All_LED_Slider_frame")
        self.All_LED_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.All_LED_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.All_LED_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.All_LED_Slider_frame)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.All_LED_Slider = QSlider(self.All_LED_Slider_frame)
        self.All_LED_Slider.setObjectName(u"All_LED_Slider")
        self.All_LED_Slider.setMaximum(100)
        self.All_LED_Slider.setSliderPosition(100)
        self.All_LED_Slider.setOrientation(Qt.Horizontal)
        self.All_LED_Slider.setTickPosition(QSlider.TicksBelow)
        self.All_LED_Slider.setTickInterval(10)

        self.horizontalLayout_33.addWidget(self.All_LED_Slider)


        self.horizontalLayout_31.addWidget(self.All_LED_Slider_frame)

        self.All_LED_Light_frame = QFrame(self.LEDZap_All_LED_frame)
        self.All_LED_Light_frame.setObjectName(u"All_LED_Light_frame")
        self.All_LED_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.All_LED_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.All_LED_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.All_LED_Light_frame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.All_LED_value = QLabel(self.All_LED_Light_frame)
        self.All_LED_value.setObjectName(u"All_LED_value")
        self.All_LED_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.All_LED_value)


        self.horizontalLayout_31.addWidget(self.All_LED_Light_frame)


        self.verticalLayout_11.addWidget(self.LEDZap_All_LED_frame)

        self.LEDZap_Preselect_frame = QFrame(self.LEDZap_LED_frame)
        self.LEDZap_Preselect_frame.setObjectName(u"LEDZap_Preselect_frame")
        self.LEDZap_Preselect_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Preselect_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.LEDZap_Preselect_frame)
        self.horizontalLayout_136.setSpacing(0)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(0, 10, 0, 10)
        self.Preselect_Button_frame = QFrame(self.LEDZap_Preselect_frame)
        self.Preselect_Button_frame.setObjectName(u"Preselect_Button_frame")
        self.Preselect_Button_frame.setMaximumSize(QSize(125, 16777215))
        self.Preselect_Button_frame.setFrameShape(QFrame.StyledPanel)
        self.Preselect_Button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.Preselect_Button_frame)
        self.verticalLayout_93.setSpacing(5)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(5, 0, 0, 0)
        self.Preselect_Load_frame = QFrame(self.Preselect_Button_frame)
        self.Preselect_Load_frame.setObjectName(u"Preselect_Load_frame")
        self.Preselect_Load_frame.setMinimumSize(QSize(0, 0))
        self.Preselect_Load_frame.setMaximumSize(QSize(125, 16777215))
        self.Preselect_Load_frame.setFrameShape(QFrame.StyledPanel)
        self.Preselect_Load_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.Preselect_Load_frame)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(5, 0, 0, 0)
        self.Preselect_Load_frame_pushButton = QPushButton(self.Preselect_Load_frame)
        self.Preselect_Load_frame_pushButton.setObjectName(u"Preselect_Load_frame_pushButton")
        self.Preselect_Load_frame_pushButton.setMaximumSize(QSize(100, 16777215))
        self.Preselect_Load_frame_pushButton.setFont(font1)

        self.verticalLayout_89.addWidget(self.Preselect_Load_frame_pushButton)


        self.verticalLayout_93.addWidget(self.Preselect_Load_frame)

        self.Preselect_Apply_frame = QFrame(self.Preselect_Button_frame)
        self.Preselect_Apply_frame.setObjectName(u"Preselect_Apply_frame")
        self.Preselect_Apply_frame.setMaximumSize(QSize(125, 16777215))
        self.Preselect_Apply_frame.setFrameShape(QFrame.StyledPanel)
        self.Preselect_Apply_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.Preselect_Apply_frame)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(5, 0, 0, 0)
        self.Preselect_Apply_pushButton = QPushButton(self.Preselect_Apply_frame)
        self.Preselect_Apply_pushButton.setObjectName(u"Preselect_Apply_pushButton")
        self.Preselect_Apply_pushButton.setMaximumSize(QSize(100, 16777215))
        self.Preselect_Apply_pushButton.setFont(font1)

        self.verticalLayout_94.addWidget(self.Preselect_Apply_pushButton)


        self.verticalLayout_93.addWidget(self.Preselect_Apply_frame)


        self.horizontalLayout_136.addWidget(self.Preselect_Button_frame)

        self.Preselect_Label_frame = QFrame(self.LEDZap_Preselect_frame)
        self.Preselect_Label_frame.setObjectName(u"Preselect_Label_frame")
        self.Preselect_Label_frame.setMaximumSize(QSize(275, 16777215))
        self.Preselect_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Preselect_Label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.Preselect_Label_frame)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(5, 0, 5, 0)
        self.Preselect_Label = QLabel(self.Preselect_Label_frame)
        self.Preselect_Label.setObjectName(u"Preselect_Label")
        self.Preselect_Label.setMaximumSize(QSize(275, 16777215))
        self.Preselect_Label.setAutoFillBackground(False)
        self.Preselect_Label.setScaledContents(True)
        self.Preselect_Label.setWordWrap(True)

        self.verticalLayout_88.addWidget(self.Preselect_Label)


        self.horizontalLayout_136.addWidget(self.Preselect_Label_frame)


        self.verticalLayout_11.addWidget(self.LEDZap_Preselect_frame)

        self.LEDZap_stackedWidget = QStackedWidget(self.LEDZap_LED_frame)
        self.LEDZap_stackedWidget.setObjectName(u"LEDZap_stackedWidget")
        self.LEDZap_page1 = QWidget()
        self.LEDZap_page1.setObjectName(u"LEDZap_page1")
        self.verticalLayout_20 = QVBoxLayout(self.LEDZap_page1)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.LED01_frame = QFrame(self.LEDZap_page1)
        self.LED01_frame.setObjectName(u"LED01_frame")
        self.LED01_frame.setFrameShape(QFrame.StyledPanel)
        self.LED01_frame.setFrameShadow(QFrame.Raised)
        self.aa = QHBoxLayout(self.LED01_frame)
        self.aa.setSpacing(5)
        self.aa.setObjectName(u"aa")
        self.aa.setContentsMargins(0, 0, 0, 0)
        self.LED01_Display_frame = QFrame(self.LED01_frame)
        self.LED01_Display_frame.setObjectName(u"LED01_Display_frame")
        self.LED01_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED01_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED01_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED01_toggleButton_layout = QHBoxLayout(self.LED01_Display_frame)
        self.LED01_toggleButton_layout.setSpacing(0)
        self.LED01_toggleButton_layout.setObjectName(u"LED01_toggleButton_layout")
        self.LED01_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED01_Display_lineEdit = QLineEdit(self.LED01_Display_frame)
        self.LED01_Display_lineEdit.setObjectName(u"LED01_Display_lineEdit")
        self.LED01_Display_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.LED01_toggleButton_layout.addWidget(self.LED01_Display_lineEdit)

        self.LED01_Display_label = QLabel(self.LED01_Display_frame)
        self.LED01_Display_label.setObjectName(u"LED01_Display_label")
        self.LED01_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED01_toggleButton_layout.addWidget(self.LED01_Display_label)


        self.aa.addWidget(self.LED01_Display_frame)

        self.LED01_Slider_frame = QFrame(self.LED01_frame)
        self.LED01_Slider_frame.setObjectName(u"LED01_Slider_frame")
        self.LED01_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED01_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED01_Slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.LED01_Slider_frame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.LED01_Slider = QSlider(self.LED01_Slider_frame)
        self.LED01_Slider.setObjectName(u"LED01_Slider")
        self.LED01_Slider.setMaximum(100)
        self.LED01_Slider.setSliderPosition(100)
        self.LED01_Slider.setOrientation(Qt.Horizontal)
        self.LED01_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED01_Slider.setTickInterval(10)

        self.verticalLayout_12.addWidget(self.LED01_Slider)


        self.aa.addWidget(self.LED01_Slider_frame)

        self.LED01_Light_frame = QFrame(self.LED01_frame)
        self.LED01_Light_frame.setObjectName(u"LED01_Light_frame")
        self.LED01_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED01_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED01_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.LED01_Light_frame)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.LED01_Value = QLabel(self.LED01_Light_frame)
        self.LED01_Value.setObjectName(u"LED01_Value")
        self.LED01_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.LED01_Value)


        self.aa.addWidget(self.LED01_Light_frame)


        self.verticalLayout_20.addWidget(self.LED01_frame)

        self.LED02_frame = QFrame(self.LEDZap_page1)
        self.LED02_frame.setObjectName(u"LED02_frame")
        self.LED02_frame.setFrameShape(QFrame.StyledPanel)
        self.LED02_frame.setFrameShadow(QFrame.Raised)
        self.aa_2 = QHBoxLayout(self.LED02_frame)
        self.aa_2.setSpacing(5)
        self.aa_2.setObjectName(u"aa_2")
        self.aa_2.setContentsMargins(0, 0, 0, 0)
        self.LED02_Display_frame = QFrame(self.LED02_frame)
        self.LED02_Display_frame.setObjectName(u"LED02_Display_frame")
        self.LED02_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED02_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED02_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED02_toggleButton_layout = QHBoxLayout(self.LED02_Display_frame)
        self.LED02_toggleButton_layout.setSpacing(0)
        self.LED02_toggleButton_layout.setObjectName(u"LED02_toggleButton_layout")
        self.LED02_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED02_Display_lineEdit = QLineEdit(self.LED02_Display_frame)
        self.LED02_Display_lineEdit.setObjectName(u"LED02_Display_lineEdit")
        self.LED02_Display_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.LED02_toggleButton_layout.addWidget(self.LED02_Display_lineEdit)

        self.LED02_Display_label = QLabel(self.LED02_Display_frame)
        self.LED02_Display_label.setObjectName(u"LED02_Display_label")
        self.LED02_Display_label.setMaximumSize(QSize(16777215, 16777215))
        self.LED02_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED02_toggleButton_layout.addWidget(self.LED02_Display_label)


        self.aa_2.addWidget(self.LED02_Display_frame)

        self.LED02_Slider_frame = QFrame(self.LED02_frame)
        self.LED02_Slider_frame.setObjectName(u"LED02_Slider_frame")
        self.LED02_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED02_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED02_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.LED02_Slider_frame)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.LED02_Slider = QSlider(self.LED02_Slider_frame)
        self.LED02_Slider.setObjectName(u"LED02_Slider")
        self.LED02_Slider.setMaximumSize(QSize(16777215, 16777215))
        self.LED02_Slider.setMaximum(100)
        self.LED02_Slider.setSliderPosition(100)
        self.LED02_Slider.setOrientation(Qt.Horizontal)
        self.LED02_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED02_Slider.setTickInterval(10)

        self.horizontalLayout_20.addWidget(self.LED02_Slider)


        self.aa_2.addWidget(self.LED02_Slider_frame)

        self.LED02_Light_frame = QFrame(self.LED02_frame)
        self.LED02_Light_frame.setObjectName(u"LED02_Light_frame")
        self.LED02_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED02_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED02_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.LED02_Light_frame)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.LED02_Value = QLabel(self.LED02_Light_frame)
        self.LED02_Value.setObjectName(u"LED02_Value")
        self.LED02_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.LED02_Value)


        self.aa_2.addWidget(self.LED02_Light_frame)


        self.verticalLayout_20.addWidget(self.LED02_frame)

        self.LED03_frame = QFrame(self.LEDZap_page1)
        self.LED03_frame.setObjectName(u"LED03_frame")
        self.LED03_frame.setFrameShape(QFrame.StyledPanel)
        self.LED03_frame.setFrameShadow(QFrame.Raised)
        self.aa_3 = QHBoxLayout(self.LED03_frame)
        self.aa_3.setSpacing(5)
        self.aa_3.setObjectName(u"aa_3")
        self.aa_3.setContentsMargins(0, 0, 0, 0)
        self.LED03_Display_frame = QFrame(self.LED03_frame)
        self.LED03_Display_frame.setObjectName(u"LED03_Display_frame")
        self.LED03_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED03_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED03_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED03_toggleButton_layout = QHBoxLayout(self.LED03_Display_frame)
        self.LED03_toggleButton_layout.setSpacing(0)
        self.LED03_toggleButton_layout.setObjectName(u"LED03_toggleButton_layout")
        self.LED03_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED03_Display_lineEdit = QLineEdit(self.LED03_Display_frame)
        self.LED03_Display_lineEdit.setObjectName(u"LED03_Display_lineEdit")
        self.LED03_Display_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.LED03_toggleButton_layout.addWidget(self.LED03_Display_lineEdit)

        self.LED03_Display_label = QLabel(self.LED03_Display_frame)
        self.LED03_Display_label.setObjectName(u"LED03_Display_label")
        self.LED03_Display_label.setMaximumSize(QSize(16777215, 16777215))
        self.LED03_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED03_toggleButton_layout.addWidget(self.LED03_Display_label)


        self.aa_3.addWidget(self.LED03_Display_frame)

        self.LED03_Slider_frame = QFrame(self.LED03_frame)
        self.LED03_Slider_frame.setObjectName(u"LED03_Slider_frame")
        self.LED03_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED03_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED03_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.LED03_Slider_frame)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.LED03_Slider = QSlider(self.LED03_Slider_frame)
        self.LED03_Slider.setObjectName(u"LED03_Slider")
        self.LED03_Slider.setMaximum(100)
        self.LED03_Slider.setSliderPosition(100)
        self.LED03_Slider.setOrientation(Qt.Horizontal)
        self.LED03_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED03_Slider.setTickInterval(10)

        self.horizontalLayout_21.addWidget(self.LED03_Slider)


        self.aa_3.addWidget(self.LED03_Slider_frame)

        self.LED03_Light_frame = QFrame(self.LED03_frame)
        self.LED03_Light_frame.setObjectName(u"LED03_Light_frame")
        self.LED03_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED03_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED03_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.LED03_Light_frame)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.LED03_Value = QLabel(self.LED03_Light_frame)
        self.LED03_Value.setObjectName(u"LED03_Value")
        self.LED03_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.LED03_Value)


        self.aa_3.addWidget(self.LED03_Light_frame)


        self.verticalLayout_20.addWidget(self.LED03_frame)

        self.LED04_frame = QFrame(self.LEDZap_page1)
        self.LED04_frame.setObjectName(u"LED04_frame")
        self.LED04_frame.setFrameShape(QFrame.StyledPanel)
        self.LED04_frame.setFrameShadow(QFrame.Raised)
        self.aa_4 = QHBoxLayout(self.LED04_frame)
        self.aa_4.setSpacing(5)
        self.aa_4.setObjectName(u"aa_4")
        self.aa_4.setContentsMargins(0, 0, 0, 0)
        self.LED04_Display_frame = QFrame(self.LED04_frame)
        self.LED04_Display_frame.setObjectName(u"LED04_Display_frame")
        self.LED04_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED04_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED04_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED04_toggleButton_layout = QHBoxLayout(self.LED04_Display_frame)
        self.LED04_toggleButton_layout.setSpacing(0)
        self.LED04_toggleButton_layout.setObjectName(u"LED04_toggleButton_layout")
        self.LED04_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED04_Display_lineEdit = QLineEdit(self.LED04_Display_frame)
        self.LED04_Display_lineEdit.setObjectName(u"LED04_Display_lineEdit")
        self.LED04_Display_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.LED04_toggleButton_layout.addWidget(self.LED04_Display_lineEdit)

        self.LED04_Display_label = QLabel(self.LED04_Display_frame)
        self.LED04_Display_label.setObjectName(u"LED04_Display_label")
        self.LED04_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED04_toggleButton_layout.addWidget(self.LED04_Display_label)


        self.aa_4.addWidget(self.LED04_Display_frame)

        self.LED04_Slider_frame = QFrame(self.LED04_frame)
        self.LED04_Slider_frame.setObjectName(u"LED04_Slider_frame")
        self.LED04_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED04_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED04_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.LED04_Slider_frame)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.LED04_Slider = QSlider(self.LED04_Slider_frame)
        self.LED04_Slider.setObjectName(u"LED04_Slider")
        self.LED04_Slider.setMaximum(100)
        self.LED04_Slider.setSliderPosition(100)
        self.LED04_Slider.setOrientation(Qt.Horizontal)
        self.LED04_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED04_Slider.setTickInterval(10)

        self.horizontalLayout_22.addWidget(self.LED04_Slider)


        self.aa_4.addWidget(self.LED04_Slider_frame)

        self.LED04_Light_frame = QFrame(self.LED04_frame)
        self.LED04_Light_frame.setObjectName(u"LED04_Light_frame")
        self.LED04_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED04_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED04_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.LED04_Light_frame)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.LED04_Value = QLabel(self.LED04_Light_frame)
        self.LED04_Value.setObjectName(u"LED04_Value")
        self.LED04_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.LED04_Value)


        self.aa_4.addWidget(self.LED04_Light_frame)


        self.verticalLayout_20.addWidget(self.LED04_frame)

        self.LED05_frame = QFrame(self.LEDZap_page1)
        self.LED05_frame.setObjectName(u"LED05_frame")
        self.LED05_frame.setFrameShape(QFrame.StyledPanel)
        self.LED05_frame.setFrameShadow(QFrame.Raised)
        self.aa_5 = QHBoxLayout(self.LED05_frame)
        self.aa_5.setSpacing(5)
        self.aa_5.setObjectName(u"aa_5")
        self.aa_5.setContentsMargins(0, 0, 0, 0)
        self.LED05_Display_frame = QFrame(self.LED05_frame)
        self.LED05_Display_frame.setObjectName(u"LED05_Display_frame")
        self.LED05_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED05_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED05_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED05_toggleButton_layout = QHBoxLayout(self.LED05_Display_frame)
        self.LED05_toggleButton_layout.setSpacing(0)
        self.LED05_toggleButton_layout.setObjectName(u"LED05_toggleButton_layout")
        self.LED05_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED05_Display_lineEdit = QLineEdit(self.LED05_Display_frame)
        self.LED05_Display_lineEdit.setObjectName(u"LED05_Display_lineEdit")
        self.LED05_Display_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.LED05_toggleButton_layout.addWidget(self.LED05_Display_lineEdit)

        self.LED05_Display_label = QLabel(self.LED05_Display_frame)
        self.LED05_Display_label.setObjectName(u"LED05_Display_label")
        self.LED05_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED05_toggleButton_layout.addWidget(self.LED05_Display_label)


        self.aa_5.addWidget(self.LED05_Display_frame)

        self.LED05_Slider_frame = QFrame(self.LED05_frame)
        self.LED05_Slider_frame.setObjectName(u"LED05_Slider_frame")
        self.LED05_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED05_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED05_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.LED05_Slider_frame)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.LED05_Slider = QSlider(self.LED05_Slider_frame)
        self.LED05_Slider.setObjectName(u"LED05_Slider")
        self.LED05_Slider.setEnabled(True)
        self.LED05_Slider.setMaximum(100)
        self.LED05_Slider.setSliderPosition(0)
        self.LED05_Slider.setOrientation(Qt.Horizontal)
        self.LED05_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED05_Slider.setTickInterval(10)

        self.horizontalLayout_23.addWidget(self.LED05_Slider)


        self.aa_5.addWidget(self.LED05_Slider_frame)

        self.LED05_Light_frame = QFrame(self.LED05_frame)
        self.LED05_Light_frame.setObjectName(u"LED05_Light_frame")
        self.LED05_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED05_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED05_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.LED05_Light_frame)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.LED05_Value = QLabel(self.LED05_Light_frame)
        self.LED05_Value.setObjectName(u"LED05_Value")
        self.LED05_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.LED05_Value)


        self.aa_5.addWidget(self.LED05_Light_frame)


        self.verticalLayout_20.addWidget(self.LED05_frame)

        self.LED06_frame = QFrame(self.LEDZap_page1)
        self.LED06_frame.setObjectName(u"LED06_frame")
        self.LED06_frame.setFrameShape(QFrame.StyledPanel)
        self.LED06_frame.setFrameShadow(QFrame.Raised)
        self.aa_6 = QHBoxLayout(self.LED06_frame)
        self.aa_6.setSpacing(5)
        self.aa_6.setObjectName(u"aa_6")
        self.aa_6.setContentsMargins(0, 0, 0, 0)
        self.LED06_Display_frame = QFrame(self.LED06_frame)
        self.LED06_Display_frame.setObjectName(u"LED06_Display_frame")
        self.LED06_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED06_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED06_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED06_toggleButton_layout = QHBoxLayout(self.LED06_Display_frame)
        self.LED06_toggleButton_layout.setSpacing(0)
        self.LED06_toggleButton_layout.setObjectName(u"LED06_toggleButton_layout")
        self.LED06_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED06_Display_lineEdit = QLineEdit(self.LED06_Display_frame)
        self.LED06_Display_lineEdit.setObjectName(u"LED06_Display_lineEdit")
        self.LED06_Display_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.LED06_toggleButton_layout.addWidget(self.LED06_Display_lineEdit)

        self.LED06_Display_label = QLabel(self.LED06_Display_frame)
        self.LED06_Display_label.setObjectName(u"LED06_Display_label")
        self.LED06_Display_label.setMaximumSize(QSize(200, 16777215))
        self.LED06_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED06_toggleButton_layout.addWidget(self.LED06_Display_label)


        self.aa_6.addWidget(self.LED06_Display_frame)

        self.LED06_Slider_frame = QFrame(self.LED06_frame)
        self.LED06_Slider_frame.setObjectName(u"LED06_Slider_frame")
        self.LED06_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED06_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED06_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.LED06_Slider_frame)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.LED06_Slider = QSlider(self.LED06_Slider_frame)
        self.LED06_Slider.setObjectName(u"LED06_Slider")
        self.LED06_Slider.setMaximum(100)
        self.LED06_Slider.setSliderPosition(0)
        self.LED06_Slider.setOrientation(Qt.Horizontal)
        self.LED06_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED06_Slider.setTickInterval(10)

        self.horizontalLayout_24.addWidget(self.LED06_Slider)


        self.aa_6.addWidget(self.LED06_Slider_frame)

        self.LED06_Light_frame = QFrame(self.LED06_frame)
        self.LED06_Light_frame.setObjectName(u"LED06_Light_frame")
        self.LED06_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED06_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED06_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.LED06_Light_frame)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.LED06_Value = QLabel(self.LED06_Light_frame)
        self.LED06_Value.setObjectName(u"LED06_Value")
        self.LED06_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.LED06_Value)


        self.aa_6.addWidget(self.LED06_Light_frame)


        self.verticalLayout_20.addWidget(self.LED06_frame)

        self.LED07_frame = QFrame(self.LEDZap_page1)
        self.LED07_frame.setObjectName(u"LED07_frame")
        self.LED07_frame.setFrameShape(QFrame.StyledPanel)
        self.LED07_frame.setFrameShadow(QFrame.Raised)
        self.aa_7 = QHBoxLayout(self.LED07_frame)
        self.aa_7.setSpacing(5)
        self.aa_7.setObjectName(u"aa_7")
        self.aa_7.setContentsMargins(0, 0, 0, 0)
        self.LED07_Display_frame = QFrame(self.LED07_frame)
        self.LED07_Display_frame.setObjectName(u"LED07_Display_frame")
        self.LED07_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED07_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED07_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED07_toggleButton_layout = QHBoxLayout(self.LED07_Display_frame)
        self.LED07_toggleButton_layout.setSpacing(0)
        self.LED07_toggleButton_layout.setObjectName(u"LED07_toggleButton_layout")
        self.LED07_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED07_Display_lineEdit = QLineEdit(self.LED07_Display_frame)
        self.LED07_Display_lineEdit.setObjectName(u"LED07_Display_lineEdit")
        self.LED07_Display_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.LED07_toggleButton_layout.addWidget(self.LED07_Display_lineEdit)

        self.LED07_Display_label = QLabel(self.LED07_Display_frame)
        self.LED07_Display_label.setObjectName(u"LED07_Display_label")
        self.LED07_Display_label.setMaximumSize(QSize(16777215, 16777215))
        self.LED07_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED07_toggleButton_layout.addWidget(self.LED07_Display_label)


        self.aa_7.addWidget(self.LED07_Display_frame)

        self.LED07_Slider_frame = QFrame(self.LED07_frame)
        self.LED07_Slider_frame.setObjectName(u"LED07_Slider_frame")
        self.LED07_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED07_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED07_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.LED07_Slider_frame)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.LED07_Slider = QSlider(self.LED07_Slider_frame)
        self.LED07_Slider.setObjectName(u"LED07_Slider")
        self.LED07_Slider.setMaximum(100)
        self.LED07_Slider.setSliderPosition(0)
        self.LED07_Slider.setOrientation(Qt.Horizontal)
        self.LED07_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED07_Slider.setTickInterval(10)

        self.horizontalLayout_25.addWidget(self.LED07_Slider)


        self.aa_7.addWidget(self.LED07_Slider_frame)

        self.LED07_Light_frame = QFrame(self.LED07_frame)
        self.LED07_Light_frame.setObjectName(u"LED07_Light_frame")
        self.LED07_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED07_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED07_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.LED07_Light_frame)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.LED07_Value = QLabel(self.LED07_Light_frame)
        self.LED07_Value.setObjectName(u"LED07_Value")
        self.LED07_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.LED07_Value)


        self.aa_7.addWidget(self.LED07_Light_frame)


        self.verticalLayout_20.addWidget(self.LED07_frame)

        self.LED08_frame = QFrame(self.LEDZap_page1)
        self.LED08_frame.setObjectName(u"LED08_frame")
        self.LED08_frame.setFrameShape(QFrame.StyledPanel)
        self.LED08_frame.setFrameShadow(QFrame.Raised)
        self.aa_8 = QHBoxLayout(self.LED08_frame)
        self.aa_8.setSpacing(5)
        self.aa_8.setObjectName(u"aa_8")
        self.aa_8.setContentsMargins(0, 0, 0, 0)
        self.LED08_Display_frame = QFrame(self.LED08_frame)
        self.LED08_Display_frame.setObjectName(u"LED08_Display_frame")
        self.LED08_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED08_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED08_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED08_toggleButton_layout = QHBoxLayout(self.LED08_Display_frame)
        self.LED08_toggleButton_layout.setSpacing(0)
        self.LED08_toggleButton_layout.setObjectName(u"LED08_toggleButton_layout")
        self.LED08_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED08_Display_lineEdit = QLineEdit(self.LED08_Display_frame)
        self.LED08_Display_lineEdit.setObjectName(u"LED08_Display_lineEdit")
        self.LED08_Display_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.LED08_toggleButton_layout.addWidget(self.LED08_Display_lineEdit)

        self.LED08_Display_label = QLabel(self.LED08_Display_frame)
        self.LED08_Display_label.setObjectName(u"LED08_Display_label")
        self.LED08_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED08_toggleButton_layout.addWidget(self.LED08_Display_label)


        self.aa_8.addWidget(self.LED08_Display_frame)

        self.LED08_Slider_frame = QFrame(self.LED08_frame)
        self.LED08_Slider_frame.setObjectName(u"LED08_Slider_frame")
        self.LED08_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED08_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED08_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.LED08_Slider_frame)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.LED08_Slider = QSlider(self.LED08_Slider_frame)
        self.LED08_Slider.setObjectName(u"LED08_Slider")
        self.LED08_Slider.setMaximum(100)
        self.LED08_Slider.setSliderPosition(0)
        self.LED08_Slider.setOrientation(Qt.Horizontal)
        self.LED08_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED08_Slider.setTickInterval(10)

        self.horizontalLayout_26.addWidget(self.LED08_Slider)


        self.aa_8.addWidget(self.LED08_Slider_frame)

        self.LED08_Light_frame = QFrame(self.LED08_frame)
        self.LED08_Light_frame.setObjectName(u"LED08_Light_frame")
        self.LED08_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED08_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED08_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.LED08_Light_frame)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.LED08_Value = QLabel(self.LED08_Light_frame)
        self.LED08_Value.setObjectName(u"LED08_Value")
        self.LED08_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.LED08_Value)


        self.aa_8.addWidget(self.LED08_Light_frame)


        self.verticalLayout_20.addWidget(self.LED08_frame)

        self.LED09_frame = QFrame(self.LEDZap_page1)
        self.LED09_frame.setObjectName(u"LED09_frame")
        self.LED09_frame.setFrameShape(QFrame.StyledPanel)
        self.LED09_frame.setFrameShadow(QFrame.Raised)
        self.aa_9 = QHBoxLayout(self.LED09_frame)
        self.aa_9.setSpacing(5)
        self.aa_9.setObjectName(u"aa_9")
        self.aa_9.setContentsMargins(0, 0, 0, 0)
        self.LED09_Display_frame = QFrame(self.LED09_frame)
        self.LED09_Display_frame.setObjectName(u"LED09_Display_frame")
        self.LED09_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED09_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED09_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED09_toggleButton_layout = QHBoxLayout(self.LED09_Display_frame)
        self.LED09_toggleButton_layout.setSpacing(0)
        self.LED09_toggleButton_layout.setObjectName(u"LED09_toggleButton_layout")
        self.LED09_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED09_Display_lineEdit = QLineEdit(self.LED09_Display_frame)
        self.LED09_Display_lineEdit.setObjectName(u"LED09_Display_lineEdit")
        self.LED09_Display_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.LED09_toggleButton_layout.addWidget(self.LED09_Display_lineEdit)

        self.LED09_Display_label = QLabel(self.LED09_Display_frame)
        self.LED09_Display_label.setObjectName(u"LED09_Display_label")
        self.LED09_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED09_toggleButton_layout.addWidget(self.LED09_Display_label)


        self.aa_9.addWidget(self.LED09_Display_frame)

        self.LED09_Slider_frame = QFrame(self.LED09_frame)
        self.LED09_Slider_frame.setObjectName(u"LED09_Slider_frame")
        self.LED09_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED09_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED09_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.LED09_Slider_frame)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.LED09_Slider = QSlider(self.LED09_Slider_frame)
        self.LED09_Slider.setObjectName(u"LED09_Slider")
        self.LED09_Slider.setMaximum(100)
        self.LED09_Slider.setSliderPosition(0)
        self.LED09_Slider.setOrientation(Qt.Horizontal)
        self.LED09_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED09_Slider.setTickInterval(10)

        self.horizontalLayout_27.addWidget(self.LED09_Slider)


        self.aa_9.addWidget(self.LED09_Slider_frame)

        self.LED09_Light_frame = QFrame(self.LED09_frame)
        self.LED09_Light_frame.setObjectName(u"LED09_Light_frame")
        self.LED09_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED09_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED09_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.LED09_Light_frame)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.LED09_Value = QLabel(self.LED09_Light_frame)
        self.LED09_Value.setObjectName(u"LED09_Value")
        self.LED09_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.LED09_Value)


        self.aa_9.addWidget(self.LED09_Light_frame)


        self.verticalLayout_20.addWidget(self.LED09_frame)

        self.LED10_frame = QFrame(self.LEDZap_page1)
        self.LED10_frame.setObjectName(u"LED10_frame")
        self.LED10_frame.setFrameShape(QFrame.StyledPanel)
        self.LED10_frame.setFrameShadow(QFrame.Raised)
        self.aa_10 = QHBoxLayout(self.LED10_frame)
        self.aa_10.setSpacing(5)
        self.aa_10.setObjectName(u"aa_10")
        self.aa_10.setContentsMargins(0, 0, 0, 0)
        self.LED10_Display_frame = QFrame(self.LED10_frame)
        self.LED10_Display_frame.setObjectName(u"LED10_Display_frame")
        self.LED10_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED10_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED10_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED10_toggleButton_layout = QHBoxLayout(self.LED10_Display_frame)
        self.LED10_toggleButton_layout.setSpacing(0)
        self.LED10_toggleButton_layout.setObjectName(u"LED10_toggleButton_layout")
        self.LED10_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED10_Display_lineEdit = QLineEdit(self.LED10_Display_frame)
        self.LED10_Display_lineEdit.setObjectName(u"LED10_Display_lineEdit")
        self.LED10_Display_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.LED10_toggleButton_layout.addWidget(self.LED10_Display_lineEdit)

        self.LED10_Display_label = QLabel(self.LED10_Display_frame)
        self.LED10_Display_label.setObjectName(u"LED10_Display_label")
        self.LED10_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED10_toggleButton_layout.addWidget(self.LED10_Display_label)


        self.aa_10.addWidget(self.LED10_Display_frame)

        self.LED10_Slider_frame = QFrame(self.LED10_frame)
        self.LED10_Slider_frame.setObjectName(u"LED10_Slider_frame")
        self.LED10_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED10_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED10_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.LED10_Slider_frame)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.LED10_Slider = QSlider(self.LED10_Slider_frame)
        self.LED10_Slider.setObjectName(u"LED10_Slider")
        self.LED10_Slider.setMaximum(100)
        self.LED10_Slider.setSliderPosition(0)
        self.LED10_Slider.setOrientation(Qt.Horizontal)
        self.LED10_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED10_Slider.setTickInterval(10)

        self.horizontalLayout_28.addWidget(self.LED10_Slider)


        self.aa_10.addWidget(self.LED10_Slider_frame)

        self.LED10_Light_frame = QFrame(self.LED10_frame)
        self.LED10_Light_frame.setObjectName(u"LED10_Light_frame")
        self.LED10_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED10_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED10_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.LED10_Light_frame)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.LED10_Value = QLabel(self.LED10_Light_frame)
        self.LED10_Value.setObjectName(u"LED10_Value")
        self.LED10_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_55.addWidget(self.LED10_Value)


        self.aa_10.addWidget(self.LED10_Light_frame)


        self.verticalLayout_20.addWidget(self.LED10_frame)

        self.LED11_frame = QFrame(self.LEDZap_page1)
        self.LED11_frame.setObjectName(u"LED11_frame")
        self.LED11_frame.setFrameShape(QFrame.StyledPanel)
        self.LED11_frame.setFrameShadow(QFrame.Raised)
        self.aa_11 = QHBoxLayout(self.LED11_frame)
        self.aa_11.setSpacing(5)
        self.aa_11.setObjectName(u"aa_11")
        self.aa_11.setContentsMargins(0, 0, 0, 0)
        self.LED11_Display_frame = QFrame(self.LED11_frame)
        self.LED11_Display_frame.setObjectName(u"LED11_Display_frame")
        self.LED11_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED11_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED11_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED11_toggleButton_layout = QHBoxLayout(self.LED11_Display_frame)
        self.LED11_toggleButton_layout.setSpacing(0)
        self.LED11_toggleButton_layout.setObjectName(u"LED11_toggleButton_layout")
        self.LED11_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED11_Display_lineEdit = QLineEdit(self.LED11_Display_frame)
        self.LED11_Display_lineEdit.setObjectName(u"LED11_Display_lineEdit")
        self.LED11_Display_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.LED11_toggleButton_layout.addWidget(self.LED11_Display_lineEdit)

        self.LED11_Display_label = QLabel(self.LED11_Display_frame)
        self.LED11_Display_label.setObjectName(u"LED11_Display_label")
        self.LED11_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED11_toggleButton_layout.addWidget(self.LED11_Display_label)


        self.aa_11.addWidget(self.LED11_Display_frame)

        self.LED11_Slider_frame = QFrame(self.LED11_frame)
        self.LED11_Slider_frame.setObjectName(u"LED11_Slider_frame")
        self.LED11_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED11_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED11_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.LED11_Slider_frame)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.LED11_Slider = QSlider(self.LED11_Slider_frame)
        self.LED11_Slider.setObjectName(u"LED11_Slider")
        self.LED11_Slider.setMaximum(100)
        self.LED11_Slider.setSliderPosition(0)
        self.LED11_Slider.setOrientation(Qt.Horizontal)
        self.LED11_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED11_Slider.setTickInterval(10)

        self.horizontalLayout_29.addWidget(self.LED11_Slider)


        self.aa_11.addWidget(self.LED11_Slider_frame)

        self.LED11_Light_frame = QFrame(self.LED11_frame)
        self.LED11_Light_frame.setObjectName(u"LED11_Light_frame")
        self.LED11_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED11_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED11_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.LED11_Light_frame)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.LED11_Value = QLabel(self.LED11_Light_frame)
        self.LED11_Value.setObjectName(u"LED11_Value")
        self.LED11_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.LED11_Value)


        self.aa_11.addWidget(self.LED11_Light_frame)


        self.verticalLayout_20.addWidget(self.LED11_frame)

        self.LED12_frame = QFrame(self.LEDZap_page1)
        self.LED12_frame.setObjectName(u"LED12_frame")
        self.LED12_frame.setFrameShape(QFrame.StyledPanel)
        self.LED12_frame.setFrameShadow(QFrame.Raised)
        self.aa_12 = QHBoxLayout(self.LED12_frame)
        self.aa_12.setSpacing(5)
        self.aa_12.setObjectName(u"aa_12")
        self.aa_12.setContentsMargins(0, 0, 0, 0)
        self.LED12_Display_frame = QFrame(self.LED12_frame)
        self.LED12_Display_frame.setObjectName(u"LED12_Display_frame")
        self.LED12_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED12_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED12_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED12_toggleButton_layout = QHBoxLayout(self.LED12_Display_frame)
        self.LED12_toggleButton_layout.setSpacing(0)
        self.LED12_toggleButton_layout.setObjectName(u"LED12_toggleButton_layout")
        self.LED12_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED12_Display_lineEdit = QLineEdit(self.LED12_Display_frame)
        self.LED12_Display_lineEdit.setObjectName(u"LED12_Display_lineEdit")
        self.LED12_Display_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.LED12_toggleButton_layout.addWidget(self.LED12_Display_lineEdit)

        self.LED12_Display_label = QLabel(self.LED12_Display_frame)
        self.LED12_Display_label.setObjectName(u"LED12_Display_label")
        self.LED12_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED12_toggleButton_layout.addWidget(self.LED12_Display_label)


        self.aa_12.addWidget(self.LED12_Display_frame)

        self.LED12_Slider_frame = QFrame(self.LED12_frame)
        self.LED12_Slider_frame.setObjectName(u"LED12_Slider_frame")
        self.LED12_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED12_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED12_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.LED12_Slider_frame)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.LED12_Slider = QSlider(self.LED12_Slider_frame)
        self.LED12_Slider.setObjectName(u"LED12_Slider")
        self.LED12_Slider.setMaximum(100)
        self.LED12_Slider.setSliderPosition(0)
        self.LED12_Slider.setOrientation(Qt.Horizontal)
        self.LED12_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED12_Slider.setTickInterval(10)

        self.horizontalLayout_30.addWidget(self.LED12_Slider)


        self.aa_12.addWidget(self.LED12_Slider_frame)

        self.LED12_Light_frame = QFrame(self.LED12_frame)
        self.LED12_Light_frame.setObjectName(u"LED12_Light_frame")
        self.LED12_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED12_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED12_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.LED12_Light_frame)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.LED12_Value = QLabel(self.LED12_Light_frame)
        self.LED12_Value.setObjectName(u"LED12_Value")
        self.LED12_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.LED12_Value)


        self.aa_12.addWidget(self.LED12_Light_frame)


        self.verticalLayout_20.addWidget(self.LED12_frame)

        self.LEDZap_stackedWidget.addWidget(self.LEDZap_page1)
        self.LEDZap_page2 = QWidget()
        self.LEDZap_page2.setObjectName(u"LEDZap_page2")
        self.verticalLayout_22 = QVBoxLayout(self.LEDZap_page2)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.LEDZap_page2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_3)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.LED13_frame = QFrame(self.frame_3)
        self.LED13_frame.setObjectName(u"LED13_frame")
        self.LED13_frame.setFrameShape(QFrame.StyledPanel)
        self.LED13_frame.setFrameShadow(QFrame.Raised)
        self.aa_32 = QHBoxLayout(self.LED13_frame)
        self.aa_32.setSpacing(5)
        self.aa_32.setObjectName(u"aa_32")
        self.aa_32.setContentsMargins(0, 0, 0, 0)
        self.LED13_Display_frame = QFrame(self.LED13_frame)
        self.LED13_Display_frame.setObjectName(u"LED13_Display_frame")
        self.LED13_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED13_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED13_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED13_toggleButton_layout = QHBoxLayout(self.LED13_Display_frame)
        self.LED13_toggleButton_layout.setSpacing(0)
        self.LED13_toggleButton_layout.setObjectName(u"LED13_toggleButton_layout")
        self.LED13_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED13_Display_label = QLabel(self.LED13_Display_frame)
        self.LED13_Display_label.setObjectName(u"LED13_Display_label")
        self.LED13_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED13_toggleButton_layout.addWidget(self.LED13_Display_label)


        self.aa_32.addWidget(self.LED13_Display_frame)

        self.LED13_Slider_frame = QFrame(self.LED13_frame)
        self.LED13_Slider_frame.setObjectName(u"LED13_Slider_frame")
        self.LED13_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED13_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED13_Slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.LED13_Slider_frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.LED13_Slider = QSlider(self.LED13_Slider_frame)
        self.LED13_Slider.setObjectName(u"LED13_Slider")
        self.LED13_Slider.setStyleSheet(u"")
        self.LED13_Slider.setMaximum(100)
        self.LED13_Slider.setSliderPosition(0)
        self.LED13_Slider.setOrientation(Qt.Horizontal)
        self.LED13_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED13_Slider.setTickInterval(10)

        self.verticalLayout_21.addWidget(self.LED13_Slider)


        self.aa_32.addWidget(self.LED13_Slider_frame)

        self.LED13_Light_frame = QFrame(self.LED13_frame)
        self.LED13_Light_frame.setObjectName(u"LED13_Light_frame")
        self.LED13_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED13_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED13_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.LED13_Light_frame)
        self.horizontalLayout_101.setSpacing(0)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.LED13_Value = QLabel(self.LED13_Light_frame)
        self.LED13_Value.setObjectName(u"LED13_Value")
        self.LED13_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_101.addWidget(self.LED13_Value)


        self.aa_32.addWidget(self.LED13_Light_frame)


        self.verticalLayout_23.addWidget(self.LED13_frame)

        self.LED14_frame = QFrame(self.frame_3)
        self.LED14_frame.setObjectName(u"LED14_frame")
        self.LED14_frame.setFrameShape(QFrame.StyledPanel)
        self.LED14_frame.setFrameShadow(QFrame.Raised)
        self.aa_31 = QHBoxLayout(self.LED14_frame)
        self.aa_31.setSpacing(5)
        self.aa_31.setObjectName(u"aa_31")
        self.aa_31.setContentsMargins(0, 0, 0, 0)
        self.LED14_Display_frame = QFrame(self.LED14_frame)
        self.LED14_Display_frame.setObjectName(u"LED14_Display_frame")
        self.LED14_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED14_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED14_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED14_toggleButton_layout = QHBoxLayout(self.LED14_Display_frame)
        self.LED14_toggleButton_layout.setSpacing(0)
        self.LED14_toggleButton_layout.setObjectName(u"LED14_toggleButton_layout")
        self.LED14_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED14_Display_label = QLabel(self.LED14_Display_frame)
        self.LED14_Display_label.setObjectName(u"LED14_Display_label")
        self.LED14_Display_label.setMaximumSize(QSize(16777215, 16777215))
        self.LED14_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED14_toggleButton_layout.addWidget(self.LED14_Display_label)


        self.aa_31.addWidget(self.LED14_Display_frame)

        self.LED14_Slider_frame = QFrame(self.LED14_frame)
        self.LED14_Slider_frame.setObjectName(u"LED14_Slider_frame")
        self.LED14_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED14_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED14_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.LED14_Slider_frame)
        self.horizontalLayout_99.setSpacing(0)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.LED14_Slider = QSlider(self.LED14_Slider_frame)
        self.LED14_Slider.setObjectName(u"LED14_Slider")
        self.LED14_Slider.setMaximumSize(QSize(16777215, 16777215))
        self.LED14_Slider.setMaximum(100)
        self.LED14_Slider.setSliderPosition(0)
        self.LED14_Slider.setOrientation(Qt.Horizontal)
        self.LED14_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED14_Slider.setTickInterval(10)

        self.horizontalLayout_99.addWidget(self.LED14_Slider)


        self.aa_31.addWidget(self.LED14_Slider_frame)

        self.LED14_Light_frame = QFrame(self.LED14_frame)
        self.LED14_Light_frame.setObjectName(u"LED14_Light_frame")
        self.LED14_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED14_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED14_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.LED14_Light_frame)
        self.horizontalLayout_100.setSpacing(0)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.LED14_Value = QLabel(self.LED14_Light_frame)
        self.LED14_Value.setObjectName(u"LED14_Value")
        self.LED14_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_100.addWidget(self.LED14_Value)


        self.aa_31.addWidget(self.LED14_Light_frame)


        self.verticalLayout_23.addWidget(self.LED14_frame)

        self.LED15_frame = QFrame(self.frame_3)
        self.LED15_frame.setObjectName(u"LED15_frame")
        self.LED15_frame.setFrameShape(QFrame.StyledPanel)
        self.LED15_frame.setFrameShadow(QFrame.Raised)
        self.aa_30 = QHBoxLayout(self.LED15_frame)
        self.aa_30.setSpacing(5)
        self.aa_30.setObjectName(u"aa_30")
        self.aa_30.setContentsMargins(0, 0, 0, 0)
        self.LED15_Display_frame = QFrame(self.LED15_frame)
        self.LED15_Display_frame.setObjectName(u"LED15_Display_frame")
        self.LED15_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED15_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED15_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED15_toggleButton_layout = QHBoxLayout(self.LED15_Display_frame)
        self.LED15_toggleButton_layout.setSpacing(0)
        self.LED15_toggleButton_layout.setObjectName(u"LED15_toggleButton_layout")
        self.LED15_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED15_Display_label = QLabel(self.LED15_Display_frame)
        self.LED15_Display_label.setObjectName(u"LED15_Display_label")
        self.LED15_Display_label.setMaximumSize(QSize(16777215, 16777215))
        self.LED15_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED15_toggleButton_layout.addWidget(self.LED15_Display_label)


        self.aa_30.addWidget(self.LED15_Display_frame)

        self.LED15_Slider_frame = QFrame(self.LED15_frame)
        self.LED15_Slider_frame.setObjectName(u"LED15_Slider_frame")
        self.LED15_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED15_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED15_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.LED15_Slider_frame)
        self.horizontalLayout_97.setSpacing(0)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.LED15_Slider = QSlider(self.LED15_Slider_frame)
        self.LED15_Slider.setObjectName(u"LED15_Slider")
        self.LED15_Slider.setMaximum(100)
        self.LED15_Slider.setSliderPosition(0)
        self.LED15_Slider.setOrientation(Qt.Horizontal)
        self.LED15_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED15_Slider.setTickInterval(10)

        self.horizontalLayout_97.addWidget(self.LED15_Slider)


        self.aa_30.addWidget(self.LED15_Slider_frame)

        self.LED15_Light_frame = QFrame(self.LED15_frame)
        self.LED15_Light_frame.setObjectName(u"LED15_Light_frame")
        self.LED15_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED15_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED15_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.LED15_Light_frame)
        self.horizontalLayout_98.setSpacing(0)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.LED15_Value = QLabel(self.LED15_Light_frame)
        self.LED15_Value.setObjectName(u"LED15_Value")
        self.LED15_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_98.addWidget(self.LED15_Value)


        self.aa_30.addWidget(self.LED15_Light_frame)


        self.verticalLayout_23.addWidget(self.LED15_frame)

        self.LED16_frame = QFrame(self.frame_3)
        self.LED16_frame.setObjectName(u"LED16_frame")
        self.LED16_frame.setFrameShape(QFrame.StyledPanel)
        self.LED16_frame.setFrameShadow(QFrame.Raised)
        self.aa_29 = QHBoxLayout(self.LED16_frame)
        self.aa_29.setSpacing(5)
        self.aa_29.setObjectName(u"aa_29")
        self.aa_29.setContentsMargins(0, 0, 0, 0)
        self.LED16_Display_frame = QFrame(self.LED16_frame)
        self.LED16_Display_frame.setObjectName(u"LED16_Display_frame")
        self.LED16_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED16_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED16_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED16_toggleButton_layout = QHBoxLayout(self.LED16_Display_frame)
        self.LED16_toggleButton_layout.setSpacing(0)
        self.LED16_toggleButton_layout.setObjectName(u"LED16_toggleButton_layout")
        self.LED16_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED16_Display_label = QLabel(self.LED16_Display_frame)
        self.LED16_Display_label.setObjectName(u"LED16_Display_label")
        self.LED16_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED16_toggleButton_layout.addWidget(self.LED16_Display_label)


        self.aa_29.addWidget(self.LED16_Display_frame)

        self.LED16_Slider_frame = QFrame(self.LED16_frame)
        self.LED16_Slider_frame.setObjectName(u"LED16_Slider_frame")
        self.LED16_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED16_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED16_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.LED16_Slider_frame)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.LED16_Slider = QSlider(self.LED16_Slider_frame)
        self.LED16_Slider.setObjectName(u"LED16_Slider")
        self.LED16_Slider.setMaximum(100)
        self.LED16_Slider.setSliderPosition(0)
        self.LED16_Slider.setOrientation(Qt.Horizontal)
        self.LED16_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED16_Slider.setTickInterval(10)

        self.horizontalLayout_95.addWidget(self.LED16_Slider)


        self.aa_29.addWidget(self.LED16_Slider_frame)

        self.LED16_Light_frame = QFrame(self.LED16_frame)
        self.LED16_Light_frame.setObjectName(u"LED16_Light_frame")
        self.LED16_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED16_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED16_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.LED16_Light_frame)
        self.horizontalLayout_96.setSpacing(0)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.LED16_Value = QLabel(self.LED16_Light_frame)
        self.LED16_Value.setObjectName(u"LED16_Value")
        self.LED16_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_96.addWidget(self.LED16_Value)


        self.aa_29.addWidget(self.LED16_Light_frame)


        self.verticalLayout_23.addWidget(self.LED16_frame)

        self.LED17_frame = QFrame(self.frame_3)
        self.LED17_frame.setObjectName(u"LED17_frame")
        self.LED17_frame.setFrameShape(QFrame.StyledPanel)
        self.LED17_frame.setFrameShadow(QFrame.Raised)
        self.aa_27 = QHBoxLayout(self.LED17_frame)
        self.aa_27.setSpacing(5)
        self.aa_27.setObjectName(u"aa_27")
        self.aa_27.setContentsMargins(0, 0, 0, 0)
        self.LED17_Display_frame = QFrame(self.LED17_frame)
        self.LED17_Display_frame.setObjectName(u"LED17_Display_frame")
        self.LED17_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED17_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED17_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED17_toggleButton_layout = QHBoxLayout(self.LED17_Display_frame)
        self.LED17_toggleButton_layout.setSpacing(0)
        self.LED17_toggleButton_layout.setObjectName(u"LED17_toggleButton_layout")
        self.LED17_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED17_Display_label = QLabel(self.LED17_Display_frame)
        self.LED17_Display_label.setObjectName(u"LED17_Display_label")
        self.LED17_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED17_toggleButton_layout.addWidget(self.LED17_Display_label)


        self.aa_27.addWidget(self.LED17_Display_frame)

        self.LED17_Slider_frame = QFrame(self.LED17_frame)
        self.LED17_Slider_frame.setObjectName(u"LED17_Slider_frame")
        self.LED17_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED17_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED17_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.LED17_Slider_frame)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.LED17_Slider = QSlider(self.LED17_Slider_frame)
        self.LED17_Slider.setObjectName(u"LED17_Slider")
        self.LED17_Slider.setEnabled(True)
        self.LED17_Slider.setMaximum(100)
        self.LED17_Slider.setSliderPosition(0)
        self.LED17_Slider.setOrientation(Qt.Horizontal)
        self.LED17_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED17_Slider.setTickInterval(10)

        self.horizontalLayout_91.addWidget(self.LED17_Slider)


        self.aa_27.addWidget(self.LED17_Slider_frame)

        self.LED17_Light_frame = QFrame(self.LED17_frame)
        self.LED17_Light_frame.setObjectName(u"LED17_Light_frame")
        self.LED17_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED17_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED17_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.LED17_Light_frame)
        self.horizontalLayout_92.setSpacing(0)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.LED17_Value = QLabel(self.LED17_Light_frame)
        self.LED17_Value.setObjectName(u"LED17_Value")
        self.LED17_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_92.addWidget(self.LED17_Value)


        self.aa_27.addWidget(self.LED17_Light_frame)


        self.verticalLayout_23.addWidget(self.LED17_frame)

        self.LED18_frame = QFrame(self.frame_3)
        self.LED18_frame.setObjectName(u"LED18_frame")
        self.LED18_frame.setFrameShape(QFrame.StyledPanel)
        self.LED18_frame.setFrameShadow(QFrame.Raised)
        self.aa_25 = QHBoxLayout(self.LED18_frame)
        self.aa_25.setSpacing(5)
        self.aa_25.setObjectName(u"aa_25")
        self.aa_25.setContentsMargins(0, 0, 0, 0)
        self.LED18_Display_frame = QFrame(self.LED18_frame)
        self.LED18_Display_frame.setObjectName(u"LED18_Display_frame")
        self.LED18_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED18_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED18_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED18_toggleButton_layout = QHBoxLayout(self.LED18_Display_frame)
        self.LED18_toggleButton_layout.setSpacing(0)
        self.LED18_toggleButton_layout.setObjectName(u"LED18_toggleButton_layout")
        self.LED18_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED18_Display_label = QLabel(self.LED18_Display_frame)
        self.LED18_Display_label.setObjectName(u"LED18_Display_label")
        self.LED18_Display_label.setMaximumSize(QSize(200, 16777215))
        self.LED18_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED18_toggleButton_layout.addWidget(self.LED18_Display_label)


        self.aa_25.addWidget(self.LED18_Display_frame)

        self.LED18_Slider_frame = QFrame(self.LED18_frame)
        self.LED18_Slider_frame.setObjectName(u"LED18_Slider_frame")
        self.LED18_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED18_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED18_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.LED18_Slider_frame)
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.LED18_Slider = QSlider(self.LED18_Slider_frame)
        self.LED18_Slider.setObjectName(u"LED18_Slider")
        self.LED18_Slider.setMaximum(100)
        self.LED18_Slider.setSliderPosition(0)
        self.LED18_Slider.setOrientation(Qt.Horizontal)
        self.LED18_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED18_Slider.setTickInterval(10)

        self.horizontalLayout_87.addWidget(self.LED18_Slider)


        self.aa_25.addWidget(self.LED18_Slider_frame)

        self.LED18_Light_frame = QFrame(self.LED18_frame)
        self.LED18_Light_frame.setObjectName(u"LED18_Light_frame")
        self.LED18_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED18_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED18_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.LED18_Light_frame)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.LED18_Value = QLabel(self.LED18_Light_frame)
        self.LED18_Value.setObjectName(u"LED18_Value")
        self.LED18_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_88.addWidget(self.LED18_Value)


        self.aa_25.addWidget(self.LED18_Light_frame)


        self.verticalLayout_23.addWidget(self.LED18_frame)

        self.LED19_frame = QFrame(self.frame_3)
        self.LED19_frame.setObjectName(u"LED19_frame")
        self.LED19_frame.setFrameShape(QFrame.StyledPanel)
        self.LED19_frame.setFrameShadow(QFrame.Raised)
        self.aa_36 = QHBoxLayout(self.LED19_frame)
        self.aa_36.setSpacing(5)
        self.aa_36.setObjectName(u"aa_36")
        self.aa_36.setContentsMargins(0, 0, 0, 0)
        self.LED19_Display_frame = QFrame(self.LED19_frame)
        self.LED19_Display_frame.setObjectName(u"LED19_Display_frame")
        self.LED19_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED19_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED19_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED19_toggleButton_layout = QHBoxLayout(self.LED19_Display_frame)
        self.LED19_toggleButton_layout.setSpacing(0)
        self.LED19_toggleButton_layout.setObjectName(u"LED19_toggleButton_layout")
        self.LED19_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED19_Display_label = QLabel(self.LED19_Display_frame)
        self.LED19_Display_label.setObjectName(u"LED19_Display_label")
        self.LED19_Display_label.setMaximumSize(QSize(16777215, 16777215))
        self.LED19_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED19_toggleButton_layout.addWidget(self.LED19_Display_label)


        self.aa_36.addWidget(self.LED19_Display_frame)

        self.LED19_Slider_frame = QFrame(self.LED19_frame)
        self.LED19_Slider_frame.setObjectName(u"LED19_Slider_frame")
        self.LED19_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED19_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED19_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_108 = QHBoxLayout(self.LED19_Slider_frame)
        self.horizontalLayout_108.setSpacing(0)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.LED19_Slider = QSlider(self.LED19_Slider_frame)
        self.LED19_Slider.setObjectName(u"LED19_Slider")
        self.LED19_Slider.setMaximum(100)
        self.LED19_Slider.setSliderPosition(0)
        self.LED19_Slider.setOrientation(Qt.Horizontal)
        self.LED19_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED19_Slider.setTickInterval(10)

        self.horizontalLayout_108.addWidget(self.LED19_Slider)


        self.aa_36.addWidget(self.LED19_Slider_frame)

        self.LED19_Light_frame = QFrame(self.LED19_frame)
        self.LED19_Light_frame.setObjectName(u"LED19_Light_frame")
        self.LED19_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED19_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED19_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.LED19_Light_frame)
        self.horizontalLayout_109.setSpacing(0)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.LED19_Value = QLabel(self.LED19_Light_frame)
        self.LED19_Value.setObjectName(u"LED19_Value")
        self.LED19_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_109.addWidget(self.LED19_Value)


        self.aa_36.addWidget(self.LED19_Light_frame)


        self.verticalLayout_23.addWidget(self.LED19_frame)

        self.LED20_frame = QFrame(self.frame_3)
        self.LED20_frame.setObjectName(u"LED20_frame")
        self.LED20_frame.setFrameShape(QFrame.StyledPanel)
        self.LED20_frame.setFrameShadow(QFrame.Raised)
        self.aa_28 = QHBoxLayout(self.LED20_frame)
        self.aa_28.setSpacing(5)
        self.aa_28.setObjectName(u"aa_28")
        self.aa_28.setContentsMargins(0, 0, 0, 0)
        self.LED20_Display_frame = QFrame(self.LED20_frame)
        self.LED20_Display_frame.setObjectName(u"LED20_Display_frame")
        self.LED20_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED20_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED20_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED20_toggleButton_layout = QHBoxLayout(self.LED20_Display_frame)
        self.LED20_toggleButton_layout.setSpacing(0)
        self.LED20_toggleButton_layout.setObjectName(u"LED20_toggleButton_layout")
        self.LED20_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED20_Display_label = QLabel(self.LED20_Display_frame)
        self.LED20_Display_label.setObjectName(u"LED20_Display_label")
        self.LED20_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED20_toggleButton_layout.addWidget(self.LED20_Display_label)


        self.aa_28.addWidget(self.LED20_Display_frame)

        self.LED20_Slider_frame = QFrame(self.LED20_frame)
        self.LED20_Slider_frame.setObjectName(u"LED20_Slider_frame")
        self.LED20_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED20_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED20_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.LED20_Slider_frame)
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.LED20_Slider = QSlider(self.LED20_Slider_frame)
        self.LED20_Slider.setObjectName(u"LED20_Slider")
        self.LED20_Slider.setMaximum(100)
        self.LED20_Slider.setSliderPosition(0)
        self.LED20_Slider.setOrientation(Qt.Horizontal)
        self.LED20_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED20_Slider.setTickInterval(10)

        self.horizontalLayout_93.addWidget(self.LED20_Slider)


        self.aa_28.addWidget(self.LED20_Slider_frame)

        self.LED20_Light_frame = QFrame(self.LED20_frame)
        self.LED20_Light_frame.setObjectName(u"LED20_Light_frame")
        self.LED20_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED20_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED20_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.LED20_Light_frame)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.LED20_Value = QLabel(self.LED20_Light_frame)
        self.LED20_Value.setObjectName(u"LED20_Value")
        self.LED20_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_94.addWidget(self.LED20_Value)


        self.aa_28.addWidget(self.LED20_Light_frame)


        self.verticalLayout_23.addWidget(self.LED20_frame)

        self.LED21_frame = QFrame(self.frame_3)
        self.LED21_frame.setObjectName(u"LED21_frame")
        self.LED21_frame.setFrameShape(QFrame.StyledPanel)
        self.LED21_frame.setFrameShadow(QFrame.Raised)
        self.aa_34 = QHBoxLayout(self.LED21_frame)
        self.aa_34.setSpacing(5)
        self.aa_34.setObjectName(u"aa_34")
        self.aa_34.setContentsMargins(0, 0, 0, 0)
        self.LED21_Display_frame = QFrame(self.LED21_frame)
        self.LED21_Display_frame.setObjectName(u"LED21_Display_frame")
        self.LED21_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED21_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED21_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED21_toggleButton_layout = QHBoxLayout(self.LED21_Display_frame)
        self.LED21_toggleButton_layout.setSpacing(0)
        self.LED21_toggleButton_layout.setObjectName(u"LED21_toggleButton_layout")
        self.LED21_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED21_Display_label = QLabel(self.LED21_Display_frame)
        self.LED21_Display_label.setObjectName(u"LED21_Display_label")
        self.LED21_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED21_toggleButton_layout.addWidget(self.LED21_Display_label)


        self.aa_34.addWidget(self.LED21_Display_frame)

        self.LED21_Slider_frame = QFrame(self.LED21_frame)
        self.LED21_Slider_frame.setObjectName(u"LED21_Slider_frame")
        self.LED21_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED21_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED21_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.LED21_Slider_frame)
        self.horizontalLayout_104.setSpacing(0)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.LED21_Slider = QSlider(self.LED21_Slider_frame)
        self.LED21_Slider.setObjectName(u"LED21_Slider")
        self.LED21_Slider.setMaximum(100)
        self.LED21_Slider.setSliderPosition(0)
        self.LED21_Slider.setOrientation(Qt.Horizontal)
        self.LED21_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED21_Slider.setTickInterval(10)

        self.horizontalLayout_104.addWidget(self.LED21_Slider)


        self.aa_34.addWidget(self.LED21_Slider_frame)

        self.LED21_Light_frame = QFrame(self.LED21_frame)
        self.LED21_Light_frame.setObjectName(u"LED21_Light_frame")
        self.LED21_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED21_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED21_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.LED21_Light_frame)
        self.horizontalLayout_105.setSpacing(0)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.LED21_Value = QLabel(self.LED21_Light_frame)
        self.LED21_Value.setObjectName(u"LED21_Value")
        self.LED21_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_105.addWidget(self.LED21_Value)


        self.aa_34.addWidget(self.LED21_Light_frame)


        self.verticalLayout_23.addWidget(self.LED21_frame)

        self.LED22_frame = QFrame(self.frame_3)
        self.LED22_frame.setObjectName(u"LED22_frame")
        self.LED22_frame.setFrameShape(QFrame.StyledPanel)
        self.LED22_frame.setFrameShadow(QFrame.Raised)
        self.aa_33 = QHBoxLayout(self.LED22_frame)
        self.aa_33.setSpacing(5)
        self.aa_33.setObjectName(u"aa_33")
        self.aa_33.setContentsMargins(0, 0, 0, 0)
        self.LED22_Display_frame = QFrame(self.LED22_frame)
        self.LED22_Display_frame.setObjectName(u"LED22_Display_frame")
        self.LED22_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED22_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED22_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED022_toggleButton_layout = QHBoxLayout(self.LED22_Display_frame)
        self.LED022_toggleButton_layout.setSpacing(0)
        self.LED022_toggleButton_layout.setObjectName(u"LED022_toggleButton_layout")
        self.LED022_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED22_Display_label = QLabel(self.LED22_Display_frame)
        self.LED22_Display_label.setObjectName(u"LED22_Display_label")
        self.LED22_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED022_toggleButton_layout.addWidget(self.LED22_Display_label)


        self.aa_33.addWidget(self.LED22_Display_frame)

        self.LED22_Slider_frame = QFrame(self.LED22_frame)
        self.LED22_Slider_frame.setObjectName(u"LED22_Slider_frame")
        self.LED22_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED22_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED22_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.LED22_Slider_frame)
        self.horizontalLayout_102.setSpacing(0)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.LED22_Slider = QSlider(self.LED22_Slider_frame)
        self.LED22_Slider.setObjectName(u"LED22_Slider")
        self.LED22_Slider.setMaximum(100)
        self.LED22_Slider.setSliderPosition(0)
        self.LED22_Slider.setOrientation(Qt.Horizontal)
        self.LED22_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED22_Slider.setTickInterval(10)

        self.horizontalLayout_102.addWidget(self.LED22_Slider)


        self.aa_33.addWidget(self.LED22_Slider_frame)

        self.LED22_Light_frame = QFrame(self.LED22_frame)
        self.LED22_Light_frame.setObjectName(u"LED22_Light_frame")
        self.LED22_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED22_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED22_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.LED22_Light_frame)
        self.horizontalLayout_103.setSpacing(0)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.LED22_Value = QLabel(self.LED22_Light_frame)
        self.LED22_Value.setObjectName(u"LED22_Value")
        self.LED22_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_103.addWidget(self.LED22_Value)


        self.aa_33.addWidget(self.LED22_Light_frame)


        self.verticalLayout_23.addWidget(self.LED22_frame)

        self.LED23_frame = QFrame(self.frame_3)
        self.LED23_frame.setObjectName(u"LED23_frame")
        self.LED23_frame.setFrameShape(QFrame.StyledPanel)
        self.LED23_frame.setFrameShadow(QFrame.Raised)
        self.aa_35 = QHBoxLayout(self.LED23_frame)
        self.aa_35.setSpacing(5)
        self.aa_35.setObjectName(u"aa_35")
        self.aa_35.setContentsMargins(0, 0, 0, 0)
        self.LED23_Display_frame = QFrame(self.LED23_frame)
        self.LED23_Display_frame.setObjectName(u"LED23_Display_frame")
        self.LED23_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED23_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED23_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED23_toggleButton_layout = QHBoxLayout(self.LED23_Display_frame)
        self.LED23_toggleButton_layout.setSpacing(0)
        self.LED23_toggleButton_layout.setObjectName(u"LED23_toggleButton_layout")
        self.LED23_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED23_Display_label = QLabel(self.LED23_Display_frame)
        self.LED23_Display_label.setObjectName(u"LED23_Display_label")
        self.LED23_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED23_toggleButton_layout.addWidget(self.LED23_Display_label)


        self.aa_35.addWidget(self.LED23_Display_frame)

        self.LED23_Slider_frame = QFrame(self.LED23_frame)
        self.LED23_Slider_frame.setObjectName(u"LED23_Slider_frame")
        self.LED23_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED23_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED23_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.LED23_Slider_frame)
        self.horizontalLayout_106.setSpacing(0)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.LED23_Slider = QSlider(self.LED23_Slider_frame)
        self.LED23_Slider.setObjectName(u"LED23_Slider")
        self.LED23_Slider.setMaximum(100)
        self.LED23_Slider.setSliderPosition(0)
        self.LED23_Slider.setOrientation(Qt.Horizontal)
        self.LED23_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED23_Slider.setTickInterval(10)

        self.horizontalLayout_106.addWidget(self.LED23_Slider)


        self.aa_35.addWidget(self.LED23_Slider_frame)

        self.LED23_Light_frame = QFrame(self.LED23_frame)
        self.LED23_Light_frame.setObjectName(u"LED23_Light_frame")
        self.LED23_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED23_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED23_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.LED23_Light_frame)
        self.horizontalLayout_107.setSpacing(0)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.LED23_Value = QLabel(self.LED23_Light_frame)
        self.LED23_Value.setObjectName(u"LED23_Value")

        self.horizontalLayout_107.addWidget(self.LED23_Value)


        self.aa_35.addWidget(self.LED23_Light_frame)


        self.verticalLayout_23.addWidget(self.LED23_frame)

        self.LED24_frame = QFrame(self.frame_3)
        self.LED24_frame.setObjectName(u"LED24_frame")
        self.LED24_frame.setFrameShape(QFrame.StyledPanel)
        self.LED24_frame.setFrameShadow(QFrame.Raised)
        self.aa_26 = QHBoxLayout(self.LED24_frame)
        self.aa_26.setSpacing(5)
        self.aa_26.setObjectName(u"aa_26")
        self.aa_26.setContentsMargins(0, 0, 0, 0)
        self.LED24_Display_frame = QFrame(self.LED24_frame)
        self.LED24_Display_frame.setObjectName(u"LED24_Display_frame")
        self.LED24_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.LED24_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LED24_Display_frame.setFrameShadow(QFrame.Raised)
        self.LED24_toggleButton_layout = QHBoxLayout(self.LED24_Display_frame)
        self.LED24_toggleButton_layout.setSpacing(0)
        self.LED24_toggleButton_layout.setObjectName(u"LED24_toggleButton_layout")
        self.LED24_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.LED24_Display_label = QLabel(self.LED24_Display_frame)
        self.LED24_Display_label.setObjectName(u"LED24_Display_label")
        self.LED24_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.LED24_toggleButton_layout.addWidget(self.LED24_Display_label)


        self.aa_26.addWidget(self.LED24_Display_frame)

        self.LED24_Slider_frame = QFrame(self.LED24_frame)
        self.LED24_Slider_frame.setObjectName(u"LED24_Slider_frame")
        self.LED24_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.LED24_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.LED24_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.LED24_Slider_frame)
        self.horizontalLayout_89.setSpacing(0)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.LED24_Slider = QSlider(self.LED24_Slider_frame)
        self.LED24_Slider.setObjectName(u"LED24_Slider")
        self.LED24_Slider.setMaximum(100)
        self.LED24_Slider.setSliderPosition(0)
        self.LED24_Slider.setOrientation(Qt.Horizontal)
        self.LED24_Slider.setTickPosition(QSlider.TicksBelow)
        self.LED24_Slider.setTickInterval(10)

        self.horizontalLayout_89.addWidget(self.LED24_Slider)


        self.aa_26.addWidget(self.LED24_Slider_frame)

        self.LED24_Light_frame = QFrame(self.LED24_frame)
        self.LED24_Light_frame.setObjectName(u"LED24_Light_frame")
        self.LED24_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.LED24_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.LED24_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.LED24_Light_frame)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.LED24_Value = QLabel(self.LED24_Light_frame)
        self.LED24_Value.setObjectName(u"LED24_Value")
        self.LED24_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_90.addWidget(self.LED24_Value)


        self.aa_26.addWidget(self.LED24_Light_frame)


        self.verticalLayout_23.addWidget(self.LED24_frame)


        self.verticalLayout_22.addWidget(self.frame_3)

        self.LEDZap_stackedWidget.addWidget(self.LEDZap_page2)

        self.verticalLayout_11.addWidget(self.LEDZap_stackedWidget)

        self.LEDZap_SwitchPage_frame = QFrame(self.LEDZap_LED_frame)
        self.LEDZap_SwitchPage_frame.setObjectName(u"LEDZap_SwitchPage_frame")
        self.LEDZap_SwitchPage_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_SwitchPage_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.LEDZap_SwitchPage_frame)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Switch_pudhButton1_frame = QFrame(self.LEDZap_SwitchPage_frame)
        self.LEDZap_Switch_pudhButton1_frame.setObjectName(u"LEDZap_Switch_pudhButton1_frame")
        self.LEDZap_Switch_pudhButton1_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Switch_pudhButton1_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.LEDZap_Switch_pudhButton1_frame)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Switch_pushButton1 = QPushButton(self.LEDZap_Switch_pudhButton1_frame)
        self.LEDZap_Switch_pushButton1.setObjectName(u"LEDZap_Switch_pushButton1")
        self.LEDZap_Switch_pushButton1.setMaximumSize(QSize(100, 16777215))
        font6 = QFont()
        font6.setPointSize(9)
        self.LEDZap_Switch_pushButton1.setFont(font6)
        self.LEDZap_Switch_pushButton1.setCheckable(True)
        self.LEDZap_Switch_pushButton1.setChecked(True)

        self.horizontalLayout_86.addWidget(self.LEDZap_Switch_pushButton1)


        self.horizontalLayout_84.addWidget(self.LEDZap_Switch_pudhButton1_frame)

        self.LEDZap_Switch_pudhButton2_frame = QFrame(self.LEDZap_SwitchPage_frame)
        self.LEDZap_Switch_pudhButton2_frame.setObjectName(u"LEDZap_Switch_pudhButton2_frame")
        self.LEDZap_Switch_pudhButton2_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDZap_Switch_pudhButton2_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.LEDZap_Switch_pudhButton2_frame)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.LEDZap_Switch_pushButton2 = QPushButton(self.LEDZap_Switch_pudhButton2_frame)
        self.LEDZap_Switch_pushButton2.setObjectName(u"LEDZap_Switch_pushButton2")
        self.LEDZap_Switch_pushButton2.setMaximumSize(QSize(100, 16777215))
        self.LEDZap_Switch_pushButton2.setFont(font6)
        self.LEDZap_Switch_pushButton2.setCheckable(True)

        self.horizontalLayout_85.addWidget(self.LEDZap_Switch_pushButton2)


        self.horizontalLayout_84.addWidget(self.LEDZap_Switch_pudhButton2_frame)


        self.verticalLayout_11.addWidget(self.LEDZap_SwitchPage_frame)


        self.verticalLayout_9.addWidget(self.LEDZap_LED_frame)


        self.horizontalLayout_13.addWidget(self.LEDZap_Stimulus_frame)


        self.verticalLayout_7.addWidget(self.LEDZap_Frame)

        self.Main_stackedWidget.addWidget(self.LEDZap_Page)
        self.Chrolis_Page = QWidget()
        self.Chrolis_Page.setObjectName(u"Chrolis_Page")
        self.verticalLayout_15 = QVBoxLayout(self.Chrolis_Page)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Frame = QFrame(self.Chrolis_Page)
        self.Chrolis_Frame.setObjectName(u"Chrolis_Frame")
        self.Chrolis_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.Chrolis_Frame)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_MainContent_Frame = QFrame(self.Chrolis_Frame)
        self.Chrolis_MainContent_Frame.setObjectName(u"Chrolis_MainContent_Frame")
        self.Chrolis_MainContent_Frame.setMinimumSize(QSize(0, 0))
        self.Chrolis_MainContent_Frame.setMaximumSize(QSize(16777215, 16777215))
        self.Chrolis_MainContent_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_MainContent_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.Chrolis_MainContent_Frame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Connect_Frame = QFrame(self.Chrolis_MainContent_Frame)
        self.Chrolis_Connect_Frame.setObjectName(u"Chrolis_Connect_Frame")
        self.Chrolis_Connect_Frame.setMinimumSize(QSize(0, 50))
        self.Chrolis_Connect_Frame.setMaximumSize(QSize(16777215, 50))
        self.Chrolis_Connect_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Connect_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.Chrolis_Connect_Frame)
        self.horizontalLayout_34.setSpacing(10)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(5, 5, 5, 5)
        self.Chrolis_SelectPortLabel = QLabel(self.Chrolis_Connect_Frame)
        self.Chrolis_SelectPortLabel.setObjectName(u"Chrolis_SelectPortLabel")
        self.Chrolis_SelectPortLabel.setFont(font1)

        self.horizontalLayout_34.addWidget(self.Chrolis_SelectPortLabel, 0, Qt.AlignHCenter)

        self.Chrolis_SelectPortComboBox = QComboBox(self.Chrolis_Connect_Frame)
        self.Chrolis_SelectPortComboBox.addItem("")
        self.Chrolis_SelectPortComboBox.setObjectName(u"Chrolis_SelectPortComboBox")

        self.horizontalLayout_34.addWidget(self.Chrolis_SelectPortComboBox)

        self.Chrolis_ConnectButton = QPushButton(self.Chrolis_Connect_Frame)
        self.Chrolis_ConnectButton.setObjectName(u"Chrolis_ConnectButton")
        self.Chrolis_ConnectButton.setEnabled(True)
        self.Chrolis_ConnectButton.setFont(font1)
        self.Chrolis_ConnectButton.setCheckable(True)

        self.horizontalLayout_34.addWidget(self.Chrolis_ConnectButton)


        self.verticalLayout_13.addWidget(self.Chrolis_Connect_Frame)

        self.Chrolis_ProxyLED_frame = QFrame(self.Chrolis_MainContent_Frame)
        self.Chrolis_ProxyLED_frame.setObjectName(u"Chrolis_ProxyLED_frame")
        self.Chrolis_ProxyLED_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_ProxyLED_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_119 = QHBoxLayout(self.Chrolis_ProxyLED_frame)
        self.horizontalLayout_119.setSpacing(5)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_ProxyLED_empty_frame = QFrame(self.Chrolis_ProxyLED_frame)
        self.Chrolis_ProxyLED_empty_frame.setObjectName(u"Chrolis_ProxyLED_empty_frame")
        self.Chrolis_ProxyLED_empty_frame.setMinimumSize(QSize(300, 0))
        self.Chrolis_ProxyLED_empty_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_ProxyLED_empty_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_119.addWidget(self.Chrolis_ProxyLED_empty_frame)

        self.Chrolis_ProxyLED_label = QLabel(self.Chrolis_ProxyLED_frame)
        self.Chrolis_ProxyLED_label.setObjectName(u"Chrolis_ProxyLED_label")
        self.Chrolis_ProxyLED_label.setFont(font4)

        self.horizontalLayout_119.addWidget(self.Chrolis_ProxyLED_label, 0, Qt.AlignTop)

        self.Chrolis_ProxyLED_Slider = QSlider(self.Chrolis_ProxyLED_frame)
        self.Chrolis_ProxyLED_Slider.setObjectName(u"Chrolis_ProxyLED_Slider")
        self.Chrolis_ProxyLED_Slider.setMaximum(255)
        self.Chrolis_ProxyLED_Slider.setPageStep(25)
        self.Chrolis_ProxyLED_Slider.setValue(100)
        self.Chrolis_ProxyLED_Slider.setOrientation(Qt.Horizontal)
        self.Chrolis_ProxyLED_Slider.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_119.addWidget(self.Chrolis_ProxyLED_Slider)

        self.Chrolis_ProxyLED_value = QLabel(self.Chrolis_ProxyLED_frame)
        self.Chrolis_ProxyLED_value.setObjectName(u"Chrolis_ProxyLED_value")
        self.Chrolis_ProxyLED_value.setMinimumSize(QSize(50, 0))
        self.Chrolis_ProxyLED_value.setFont(font1)
        self.Chrolis_ProxyLED_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_119.addWidget(self.Chrolis_ProxyLED_value, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.Chrolis_ProxyLED_frame)

        self.Chrolis_Display_Frame = QFrame(self.Chrolis_MainContent_Frame)
        self.Chrolis_Display_Frame.setObjectName(u"Chrolis_Display_Frame")
        self.Chrolis_Display_Frame.setMinimumSize(QSize(0, 100))
        self.Chrolis_Display_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Display_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.Chrolis_Display_Frame)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Display_stackedWidget = QStackedWidget(self.Chrolis_Display_Frame)
        self.Chrolis_Display_stackedWidget.setObjectName(u"Chrolis_Display_stackedWidget")
        self.Chrolis_Display_page1 = QWidget()
        self.Chrolis_Display_page1.setObjectName(u"Chrolis_Display_page1")
        self.verticalLayout_24 = QVBoxLayout(self.Chrolis_Display_page1)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 2, 0, 0)
        self.Chrolis_Display1_pushButton_frame = QFrame(self.Chrolis_Display_page1)
        self.Chrolis_Display1_pushButton_frame.setObjectName(u"Chrolis_Display1_pushButton_frame")
        self.Chrolis_Display1_pushButton_frame.setMaximumSize(QSize(16777215, 20))
        self.Chrolis_Display1_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Display1_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.Chrolis_Display1_pushButton_frame)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 5, 0)
        self.Chrolis_Display1_pushButton = QPushButton(self.Chrolis_Display1_pushButton_frame)
        self.Chrolis_Display1_pushButton.setObjectName(u"Chrolis_Display1_pushButton")
        self.Chrolis_Display1_pushButton.setMinimumSize(QSize(150, 20))
        self.Chrolis_Display1_pushButton.setMaximumSize(QSize(150, 20))

        self.verticalLayout_31.addWidget(self.Chrolis_Display1_pushButton, 0, Qt.AlignRight)


        self.verticalLayout_24.addWidget(self.Chrolis_Display1_pushButton_frame, 0, Qt.AlignTop)

        self.Chrolis_Display1 = PlotWidget(self.Chrolis_Display_page1)
        self.Chrolis_Display1.setObjectName(u"Chrolis_Display1")
        self.verticalLayout_37 = QVBoxLayout(self.Chrolis_Display1)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 2, 0, 0)

        self.verticalLayout_24.addWidget(self.Chrolis_Display1)

        self.Chrolis_Display_stackedWidget.addWidget(self.Chrolis_Display_page1)
        self.Chrolis_Display_page2 = QWidget()
        self.Chrolis_Display_page2.setObjectName(u"Chrolis_Display_page2")
        self.verticalLayout_32 = QVBoxLayout(self.Chrolis_Display_page2)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 2, 0, 0)
        self.Chrolis_Display2_pushButton_frame = QFrame(self.Chrolis_Display_page2)
        self.Chrolis_Display2_pushButton_frame.setObjectName(u"Chrolis_Display2_pushButton_frame")
        self.Chrolis_Display2_pushButton_frame.setMaximumSize(QSize(16777215, 20))
        self.Chrolis_Display2_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Display2_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.Chrolis_Display2_pushButton_frame)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 5, 0)
        self.Chrolis_Display2_pushButton = QPushButton(self.Chrolis_Display2_pushButton_frame)
        self.Chrolis_Display2_pushButton.setObjectName(u"Chrolis_Display2_pushButton")
        self.Chrolis_Display2_pushButton.setMinimumSize(QSize(150, 20))
        self.Chrolis_Display2_pushButton.setMaximumSize(QSize(150, 20))

        self.verticalLayout_35.addWidget(self.Chrolis_Display2_pushButton, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_32.addWidget(self.Chrolis_Display2_pushButton_frame)

        self.Chrolis_Display2 = QFrame(self.Chrolis_Display_page2)
        self.Chrolis_Display2.setObjectName(u"Chrolis_Display2")
        self.Chrolis_Display2.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Display2.setFrameShadow(QFrame.Raised)
        self.Chrolis_Display2_Layout = QVBoxLayout(self.Chrolis_Display2)
        self.Chrolis_Display2_Layout.setSpacing(0)
        self.Chrolis_Display2_Layout.setObjectName(u"Chrolis_Display2_Layout")
        self.Chrolis_Display2_Layout.setContentsMargins(0, 2, 0, 0)

        self.verticalLayout_32.addWidget(self.Chrolis_Display2)

        self.Chrolis_Display_stackedWidget.addWidget(self.Chrolis_Display_page2)

        self.verticalLayout_28.addWidget(self.Chrolis_Display_stackedWidget)


        self.verticalLayout_13.addWidget(self.Chrolis_Display_Frame)

        self.Chrolis_Serial_Frame = QFrame(self.Chrolis_MainContent_Frame)
        self.Chrolis_Serial_Frame.setObjectName(u"Chrolis_Serial_Frame")
        self.Chrolis_Serial_Frame.setMinimumSize(QSize(0, 60))
        self.Chrolis_Serial_Frame.setMaximumSize(QSize(16777215, 60))
        self.Chrolis_Serial_Frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Serial_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.Chrolis_Serial_Frame)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Serial = QWidget(self.Chrolis_Serial_Frame)
        self.Chrolis_Serial.setObjectName(u"Chrolis_Serial")
        self.Chrolis_Serial.setStyleSheet(u"background-color: rgb(0,12,15);")
        self.verticalLayout_29 = QVBoxLayout(self.Chrolis_Serial)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(10, 0, 10, 0)
        self.Chrolis_Serial_label = QLabel(self.Chrolis_Serial)
        self.Chrolis_Serial_label.setObjectName(u"Chrolis_Serial_label")
        self.Chrolis_Serial_label.setFont(font1)
        self.Chrolis_Serial_label.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.Chrolis_Serial_label)


        self.horizontalLayout_36.addWidget(self.Chrolis_Serial)


        self.verticalLayout_13.addWidget(self.Chrolis_Serial_Frame, 0, Qt.AlignBottom)


        self.horizontalLayout_32.addWidget(self.Chrolis_MainContent_Frame)

        self.line_5 = QFrame(self.Chrolis_Frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_32.addWidget(self.line_5)

        self.Chrolis_Stimulus_frame = QFrame(self.Chrolis_Frame)
        self.Chrolis_Stimulus_frame.setObjectName(u"Chrolis_Stimulus_frame")
        self.Chrolis_Stimulus_frame.setMaximumSize(QSize(400, 16777215))
        self.Chrolis_Stimulus_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Stimulus_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.Chrolis_Stimulus_frame)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_StimulusControl_frame = QFrame(self.Chrolis_Stimulus_frame)
        self.Chrolis_StimulusControl_frame.setObjectName(u"Chrolis_StimulusControl_frame")
        self.Chrolis_StimulusControl_frame.setMinimumSize(QSize(0, 100))
        self.Chrolis_StimulusControl_frame.setMaximumSize(QSize(16777215, 100))
        self.Chrolis_StimulusControl_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_StimulusControl_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.Chrolis_StimulusControl_frame)
        self.verticalLayout_17.setSpacing(10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 0)
        self.Chrolis_Load_frame = QFrame(self.Chrolis_StimulusControl_frame)
        self.Chrolis_Load_frame.setObjectName(u"Chrolis_Load_frame")
        self.Chrolis_Load_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Load_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.Chrolis_Load_frame)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Load_pushButton_frame = QFrame(self.Chrolis_Load_frame)
        self.Chrolis_Load_pushButton_frame.setObjectName(u"Chrolis_Load_pushButton_frame")
        self.Chrolis_Load_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis_Load_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Load_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.Chrolis_Load_pushButton_frame)
        self.horizontalLayout_110.setSpacing(0)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Load_pushButton = QPushButton(self.Chrolis_Load_pushButton_frame)
        self.Chrolis_Load_pushButton.setObjectName(u"Chrolis_Load_pushButton")
        self.Chrolis_Load_pushButton.setMinimumSize(QSize(100, 0))
        self.Chrolis_Load_pushButton.setMaximumSize(QSize(100, 16777215))
        self.Chrolis_Load_pushButton.setFont(font1)
        self.Chrolis_Load_pushButton.setCheckable(True)

        self.horizontalLayout_110.addWidget(self.Chrolis_Load_pushButton)


        self.horizontalLayout_15.addWidget(self.Chrolis_Load_pushButton_frame)

        self.Chrolis_Stimulus_Label_frame = QFrame(self.Chrolis_Load_frame)
        self.Chrolis_Stimulus_Label_frame.setObjectName(u"Chrolis_Stimulus_Label_frame")
        self.Chrolis_Stimulus_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Stimulus_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.Chrolis_Stimulus_Label_frame)
        self.horizontalLayout_111.setSpacing(0)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Stimulus_Label = QLabel(self.Chrolis_Stimulus_Label_frame)
        self.Chrolis_Stimulus_Label.setObjectName(u"Chrolis_Stimulus_Label")
        self.Chrolis_Stimulus_Label.setMinimumSize(QSize(0, 25))
        self.Chrolis_Stimulus_Label.setMaximumSize(QSize(275, 25))
        self.Chrolis_Stimulus_Label.setFont(font5)
        self.Chrolis_Stimulus_Label.setScaledContents(True)
        self.Chrolis_Stimulus_Label.setWordWrap(True)

        self.horizontalLayout_111.addWidget(self.Chrolis_Stimulus_Label)


        self.horizontalLayout_15.addWidget(self.Chrolis_Stimulus_Label_frame)


        self.verticalLayout_17.addWidget(self.Chrolis_Load_frame)

        self.Chrolis_StimulusMain_frame = QFrame(self.Chrolis_StimulusControl_frame)
        self.Chrolis_StimulusMain_frame.setObjectName(u"Chrolis_StimulusMain_frame")
        self.Chrolis_StimulusMain_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_StimulusMain_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.Chrolis_StimulusMain_frame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Stimulus_Left_frame = QFrame(self.Chrolis_StimulusMain_frame)
        self.Chrolis_Stimulus_Left_frame.setObjectName(u"Chrolis_Stimulus_Left_frame")
        self.Chrolis_Stimulus_Left_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Stimulus_Left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.Chrolis_Stimulus_Left_frame)
        self.verticalLayout_99.setSpacing(10)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Display_pushButton_frame = QFrame(self.Chrolis_Stimulus_Left_frame)
        self.Chrolis_Display_pushButton_frame.setObjectName(u"Chrolis_Display_pushButton_frame")
        self.Chrolis_Display_pushButton_frame.setMinimumSize(QSize(125, 0))
        self.Chrolis_Display_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis_Display_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Display_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_147 = QHBoxLayout(self.Chrolis_Display_pushButton_frame)
        self.horizontalLayout_147.setSpacing(0)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Display_pushButton = QPushButton(self.Chrolis_Display_pushButton_frame)
        self.Chrolis_Display_pushButton.setObjectName(u"Chrolis_Display_pushButton")
        self.Chrolis_Display_pushButton.setMinimumSize(QSize(100, 0))
        self.Chrolis_Display_pushButton.setMaximumSize(QSize(100, 16777215))
        self.Chrolis_Display_pushButton.setFont(font1)
        self.Chrolis_Display_pushButton.setCheckable(True)

        self.horizontalLayout_147.addWidget(self.Chrolis_Display_pushButton)


        self.verticalLayout_99.addWidget(self.Chrolis_Display_pushButton_frame)

        self.Chrolis_Test_pushButton_frame = QFrame(self.Chrolis_Stimulus_Left_frame)
        self.Chrolis_Test_pushButton_frame.setObjectName(u"Chrolis_Test_pushButton_frame")
        self.Chrolis_Test_pushButton_frame.setMinimumSize(QSize(125, 0))
        self.Chrolis_Test_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis_Test_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Test_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_148 = QHBoxLayout(self.Chrolis_Test_pushButton_frame)
        self.horizontalLayout_148.setSpacing(0)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Test_pushButton = QPushButton(self.Chrolis_Test_pushButton_frame)
        self.Chrolis_Test_pushButton.setObjectName(u"Chrolis_Test_pushButton")
        self.Chrolis_Test_pushButton.setMinimumSize(QSize(100, 0))
        self.Chrolis_Test_pushButton.setMaximumSize(QSize(100, 16777215))
        self.Chrolis_Test_pushButton.setFont(font1)

        self.horizontalLayout_148.addWidget(self.Chrolis_Test_pushButton)


        self.verticalLayout_99.addWidget(self.Chrolis_Test_pushButton_frame)


        self.horizontalLayout_16.addWidget(self.Chrolis_Stimulus_Left_frame)

        self.Chrolis_Stimulus_Right_frame = QFrame(self.Chrolis_StimulusMain_frame)
        self.Chrolis_Stimulus_Right_frame.setObjectName(u"Chrolis_Stimulus_Right_frame")
        self.Chrolis_Stimulus_Right_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Stimulus_Right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.Chrolis_Stimulus_Right_frame)
        self.verticalLayout_98.setSpacing(0)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Stimulus_Play_frame = QFrame(self.Chrolis_Stimulus_Right_frame)
        self.Chrolis_Stimulus_Play_frame.setObjectName(u"Chrolis_Stimulus_Play_frame")
        self.Chrolis_Stimulus_Play_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Stimulus_Play_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.Chrolis_Stimulus_Play_frame)
        self.horizontalLayout_60.setSpacing(10)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Start_pushButton_frame = QFrame(self.Chrolis_Stimulus_Play_frame)
        self.Chrolis_Start_pushButton_frame.setObjectName(u"Chrolis_Start_pushButton_frame")
        self.Chrolis_Start_pushButton_frame.setMinimumSize(QSize(125, 0))
        self.Chrolis_Start_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis_Start_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Start_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_112 = QHBoxLayout(self.Chrolis_Start_pushButton_frame)
        self.horizontalLayout_112.setSpacing(0)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Start_pushButton = QPushButton(self.Chrolis_Start_pushButton_frame)
        self.Chrolis_Start_pushButton.setObjectName(u"Chrolis_Start_pushButton")
        self.Chrolis_Start_pushButton.setMinimumSize(QSize(125, 0))
        self.Chrolis_Start_pushButton.setMaximumSize(QSize(125, 16777215))
        self.Chrolis_Start_pushButton.setFont(font1)
        self.Chrolis_Start_pushButton.setCheckable(True)

        self.horizontalLayout_112.addWidget(self.Chrolis_Start_pushButton)


        self.horizontalLayout_60.addWidget(self.Chrolis_Start_pushButton_frame)

        self.Chrolis_Stop_pushButton_frame = QFrame(self.Chrolis_Stimulus_Play_frame)
        self.Chrolis_Stop_pushButton_frame.setObjectName(u"Chrolis_Stop_pushButton_frame")
        self.Chrolis_Stop_pushButton_frame.setMinimumSize(QSize(125, 0))
        self.Chrolis_Stop_pushButton_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis_Stop_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Stop_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.Chrolis_Stop_pushButton_frame)
        self.horizontalLayout_138.setSpacing(0)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Stop_pushButton = QPushButton(self.Chrolis_Stop_pushButton_frame)
        self.Chrolis_Stop_pushButton.setObjectName(u"Chrolis_Stop_pushButton")
        self.Chrolis_Stop_pushButton.setMinimumSize(QSize(125, 0))
        self.Chrolis_Stop_pushButton.setMaximumSize(QSize(125, 16777215))
        self.Chrolis_Stop_pushButton.setFont(font1)
        self.Chrolis_Stop_pushButton.setCheckable(True)

        self.horizontalLayout_138.addWidget(self.Chrolis_Stop_pushButton)


        self.horizontalLayout_60.addWidget(self.Chrolis_Stop_pushButton_frame)


        self.verticalLayout_98.addWidget(self.Chrolis_Stimulus_Play_frame)

        self.Chrolis_NumbeofLoop_frame = QFrame(self.Chrolis_Stimulus_Right_frame)
        self.Chrolis_NumbeofLoop_frame.setObjectName(u"Chrolis_NumbeofLoop_frame")
        self.Chrolis_NumbeofLoop_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_NumbeofLoop_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.Chrolis_NumbeofLoop_frame)
        self.horizontalLayout_144.setSpacing(0)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_NumbeofLoop_Label_frame = QFrame(self.Chrolis_NumbeofLoop_frame)
        self.Chrolis_NumbeofLoop_Label_frame.setObjectName(u"Chrolis_NumbeofLoop_Label_frame")
        self.Chrolis_NumbeofLoop_Label_frame.setMinimumSize(QSize(125, 0))
        self.Chrolis_NumbeofLoop_Label_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis_NumbeofLoop_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_NumbeofLoop_Label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_145 = QHBoxLayout(self.Chrolis_NumbeofLoop_Label_frame)
        self.horizontalLayout_145.setSpacing(0)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_NumbeofLoop_Label = QLabel(self.Chrolis_NumbeofLoop_Label_frame)
        self.Chrolis_NumbeofLoop_Label.setObjectName(u"Chrolis_NumbeofLoop_Label")
        self.Chrolis_NumbeofLoop_Label.setMaximumSize(QSize(1752, 16777215))
        self.Chrolis_NumbeofLoop_Label.setFont(font4)

        self.horizontalLayout_145.addWidget(self.Chrolis_NumbeofLoop_Label, 0, Qt.AlignRight)


        self.horizontalLayout_144.addWidget(self.Chrolis_NumbeofLoop_Label_frame, 0, Qt.AlignHCenter)

        self.Chrolis_NumbeofLoop_lineEdit_frame = QFrame(self.Chrolis_NumbeofLoop_frame)
        self.Chrolis_NumbeofLoop_lineEdit_frame.setObjectName(u"Chrolis_NumbeofLoop_lineEdit_frame")
        self.Chrolis_NumbeofLoop_lineEdit_frame.setMinimumSize(QSize(125, 0))
        self.Chrolis_NumbeofLoop_lineEdit_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis_NumbeofLoop_lineEdit_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_NumbeofLoop_lineEdit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_146 = QHBoxLayout(self.Chrolis_NumbeofLoop_lineEdit_frame)
        self.horizontalLayout_146.setSpacing(0)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.horizontalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_NumbeofLoop = QLineEdit(self.Chrolis_NumbeofLoop_lineEdit_frame)
        self.Chrolis_NumbeofLoop.setObjectName(u"Chrolis_NumbeofLoop")
        self.Chrolis_NumbeofLoop.setMinimumSize(QSize(100, 0))
        self.Chrolis_NumbeofLoop.setMaximumSize(QSize(100, 16777215))
        self.Chrolis_NumbeofLoop.setFont(font1)
        self.Chrolis_NumbeofLoop.setStyleSheet(u" border: 1px solid rgb(147,161,161);\n"
"background-color: rgb(7, 54, 66);")
        self.Chrolis_NumbeofLoop.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_146.addWidget(self.Chrolis_NumbeofLoop)


        self.horizontalLayout_144.addWidget(self.Chrolis_NumbeofLoop_lineEdit_frame, 0, Qt.AlignHCenter)


        self.verticalLayout_98.addWidget(self.Chrolis_NumbeofLoop_frame)


        self.horizontalLayout_16.addWidget(self.Chrolis_Stimulus_Right_frame)


        self.verticalLayout_17.addWidget(self.Chrolis_StimulusMain_frame)


        self.verticalLayout_14.addWidget(self.Chrolis_StimulusControl_frame)

        self.line_6 = QFrame(self.Chrolis_Stimulus_frame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_6)

        self.Chrolis_LED_frame = QFrame(self.Chrolis_Stimulus_frame)
        self.Chrolis_LED_frame.setObjectName(u"Chrolis_LED_frame")
        self.Chrolis_LED_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_LED_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.Chrolis_LED_frame)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 0, 5, 5)
        self.ChrolisAll_LED = QFrame(self.Chrolis_LED_frame)
        self.ChrolisAll_LED.setObjectName(u"ChrolisAll_LED")
        self.ChrolisAll_LED.setFrameShape(QFrame.StyledPanel)
        self.ChrolisAll_LED.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.ChrolisAll_LED)
        self.horizontalLayout_37.setSpacing(5)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.ChrolisAll_LED_Display_frame = QFrame(self.ChrolisAll_LED)
        self.ChrolisAll_LED_Display_frame.setObjectName(u"ChrolisAll_LED_Display_frame")
        self.ChrolisAll_LED_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.ChrolisAll_LED_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.ChrolisAll_LED_Display_frame.setFrameShadow(QFrame.Raised)
        self.ChrolisAll_toggleButton_layout = QHBoxLayout(self.ChrolisAll_LED_Display_frame)
        self.ChrolisAll_toggleButton_layout.setSpacing(0)
        self.ChrolisAll_toggleButton_layout.setObjectName(u"ChrolisAll_toggleButton_layout")
        self.ChrolisAll_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.ChrolisAll_LED_label = QLabel(self.ChrolisAll_LED_Display_frame)
        self.ChrolisAll_LED_label.setObjectName(u"ChrolisAll_LED_label")
        self.ChrolisAll_LED_label.setMaximumSize(QSize(200, 16777215))
        self.ChrolisAll_LED_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.ChrolisAll_toggleButton_layout.addWidget(self.ChrolisAll_LED_label)


        self.horizontalLayout_37.addWidget(self.ChrolisAll_LED_Display_frame)

        self.ChrolisAll_LED_Slider_frame = QFrame(self.ChrolisAll_LED)
        self.ChrolisAll_LED_Slider_frame.setObjectName(u"ChrolisAll_LED_Slider_frame")
        self.ChrolisAll_LED_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.ChrolisAll_LED_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.ChrolisAll_LED_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.ChrolisAll_LED_Slider_frame)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.ChrolisAll_LED_Slider = QSlider(self.ChrolisAll_LED_Slider_frame)
        self.ChrolisAll_LED_Slider.setObjectName(u"ChrolisAll_LED_Slider")
        self.ChrolisAll_LED_Slider.setMaximum(100)
        self.ChrolisAll_LED_Slider.setSliderPosition(100)
        self.ChrolisAll_LED_Slider.setOrientation(Qt.Horizontal)
        self.ChrolisAll_LED_Slider.setTickPosition(QSlider.TicksBelow)
        self.ChrolisAll_LED_Slider.setTickInterval(10)

        self.horizontalLayout_38.addWidget(self.ChrolisAll_LED_Slider)


        self.horizontalLayout_37.addWidget(self.ChrolisAll_LED_Slider_frame)

        self.ChrolisAll_LED_Light_frame_ = QFrame(self.ChrolisAll_LED)
        self.ChrolisAll_LED_Light_frame_.setObjectName(u"ChrolisAll_LED_Light_frame_")
        self.ChrolisAll_LED_Light_frame_.setMaximumSize(QSize(50, 16777215))
        self.ChrolisAll_LED_Light_frame_.setFrameShape(QFrame.StyledPanel)
        self.ChrolisAll_LED_Light_frame_.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.ChrolisAll_LED_Light_frame_)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.ChrolisAll_LED_value = QLabel(self.ChrolisAll_LED_Light_frame_)
        self.ChrolisAll_LED_value.setObjectName(u"ChrolisAll_LED_value")
        self.ChrolisAll_LED_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.ChrolisAll_LED_value)


        self.horizontalLayout_37.addWidget(self.ChrolisAll_LED_Light_frame_)


        self.verticalLayout_18.addWidget(self.ChrolisAll_LED)

        self.Chrolis_Preselect_frame = QFrame(self.Chrolis_LED_frame)
        self.Chrolis_Preselect_frame.setObjectName(u"Chrolis_Preselect_frame")
        self.Chrolis_Preselect_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Preselect_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.Chrolis_Preselect_frame)
        self.horizontalLayout_135.setSpacing(0)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(0, 10, 0, 10)
        self.Chrolis_Preselect_Button_frame = QFrame(self.Chrolis_Preselect_frame)
        self.Chrolis_Preselect_Button_frame.setObjectName(u"Chrolis_Preselect_Button_frame")
        self.Chrolis_Preselect_Button_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis_Preselect_Button_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Preselect_Button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.Chrolis_Preselect_Button_frame)
        self.verticalLayout_92.setSpacing(5)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(5, 0, 0, 0)
        self.Chrolis_Preselect_Load_frame = QFrame(self.Chrolis_Preselect_Button_frame)
        self.Chrolis_Preselect_Load_frame.setObjectName(u"Chrolis_Preselect_Load_frame")
        self.Chrolis_Preselect_Load_frame.setMinimumSize(QSize(0, 0))
        self.Chrolis_Preselect_Load_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis_Preselect_Load_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Preselect_Load_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.Chrolis_Preselect_Load_frame)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(5, 0, 0, 0)
        self.Chrolis_Preselect_Load_frame_pushButton = QPushButton(self.Chrolis_Preselect_Load_frame)
        self.Chrolis_Preselect_Load_frame_pushButton.setObjectName(u"Chrolis_Preselect_Load_frame_pushButton")
        self.Chrolis_Preselect_Load_frame_pushButton.setMaximumSize(QSize(100, 16777215))
        self.Chrolis_Preselect_Load_frame_pushButton.setFont(font1)

        self.verticalLayout_91.addWidget(self.Chrolis_Preselect_Load_frame_pushButton)


        self.verticalLayout_92.addWidget(self.Chrolis_Preselect_Load_frame)

        self.Chrolis_Preselect_Apply_frame = QFrame(self.Chrolis_Preselect_Button_frame)
        self.Chrolis_Preselect_Apply_frame.setObjectName(u"Chrolis_Preselect_Apply_frame")
        self.Chrolis_Preselect_Apply_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis_Preselect_Apply_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Preselect_Apply_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.Chrolis_Preselect_Apply_frame)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(5, 0, 0, 0)
        self.Chrolis_Preselect_Apply_pushButton = QPushButton(self.Chrolis_Preselect_Apply_frame)
        self.Chrolis_Preselect_Apply_pushButton.setObjectName(u"Chrolis_Preselect_Apply_pushButton")
        self.Chrolis_Preselect_Apply_pushButton.setMaximumSize(QSize(100, 16777215))
        self.Chrolis_Preselect_Apply_pushButton.setFont(font1)

        self.verticalLayout_95.addWidget(self.Chrolis_Preselect_Apply_pushButton)


        self.verticalLayout_92.addWidget(self.Chrolis_Preselect_Apply_frame)


        self.horizontalLayout_135.addWidget(self.Chrolis_Preselect_Button_frame)

        self.Chrolis_Preselect_Label_frame = QFrame(self.Chrolis_Preselect_frame)
        self.Chrolis_Preselect_Label_frame.setObjectName(u"Chrolis_Preselect_Label_frame")
        self.Chrolis_Preselect_Label_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_Preselect_Label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.Chrolis_Preselect_Label_frame)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_Preselect_Label = QLabel(self.Chrolis_Preselect_Label_frame)
        self.Chrolis_Preselect_Label.setObjectName(u"Chrolis_Preselect_Label")
        self.Chrolis_Preselect_Label.setMaximumSize(QSize(275, 16777215))
        self.Chrolis_Preselect_Label.setAutoFillBackground(False)
        self.Chrolis_Preselect_Label.setScaledContents(True)
        self.Chrolis_Preselect_Label.setWordWrap(True)

        self.verticalLayout_90.addWidget(self.Chrolis_Preselect_Label)


        self.horizontalLayout_135.addWidget(self.Chrolis_Preselect_Label_frame)


        self.verticalLayout_18.addWidget(self.Chrolis_Preselect_frame)

        self.Chrolis01_frame = QFrame(self.Chrolis_LED_frame)
        self.Chrolis01_frame.setObjectName(u"Chrolis01_frame")
        self.Chrolis01_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis01_frame.setFrameShadow(QFrame.Raised)
        self.aa_13 = QHBoxLayout(self.Chrolis01_frame)
        self.aa_13.setSpacing(5)
        self.aa_13.setObjectName(u"aa_13")
        self.aa_13.setContentsMargins(0, 0, 0, 0)
        self.Chrolis01_Display_frame = QFrame(self.Chrolis01_frame)
        self.Chrolis01_Display_frame.setObjectName(u"Chrolis01_Display_frame")
        self.Chrolis01_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis01_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis01_Display_frame.setFrameShadow(QFrame.Raised)
        self.Chrolis01_toggleButton_layout = QHBoxLayout(self.Chrolis01_Display_frame)
        self.Chrolis01_toggleButton_layout.setSpacing(0)
        self.Chrolis01_toggleButton_layout.setObjectName(u"Chrolis01_toggleButton_layout")
        self.Chrolis01_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Chrolis01_Display_label = QLabel(self.Chrolis01_Display_frame)
        self.Chrolis01_Display_label.setObjectName(u"Chrolis01_Display_label")
        self.Chrolis01_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Chrolis01_toggleButton_layout.addWidget(self.Chrolis01_Display_label)


        self.aa_13.addWidget(self.Chrolis01_Display_frame)

        self.Chrolis01_Slider_frame = QFrame(self.Chrolis01_frame)
        self.Chrolis01_Slider_frame.setObjectName(u"Chrolis01_Slider_frame")
        self.Chrolis01_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Chrolis01_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis01_Slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.Chrolis01_Slider_frame)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Chrolis01_Slider = QSlider(self.Chrolis01_Slider_frame)
        self.Chrolis01_Slider.setObjectName(u"Chrolis01_Slider")
        self.Chrolis01_Slider.setMaximum(100)
        self.Chrolis01_Slider.setSliderPosition(100)
        self.Chrolis01_Slider.setOrientation(Qt.Horizontal)
        self.Chrolis01_Slider.setTickPosition(QSlider.TicksBelow)
        self.Chrolis01_Slider.setTickInterval(10)

        self.verticalLayout_19.addWidget(self.Chrolis01_Slider)


        self.aa_13.addWidget(self.Chrolis01_Slider_frame)

        self.Chrolis01_Light_frame = QFrame(self.Chrolis01_frame)
        self.Chrolis01_Light_frame.setObjectName(u"Chrolis01_Light_frame")
        self.Chrolis01_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Chrolis01_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis01_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.Chrolis01_Light_frame)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.Chrolis01_Value = QLabel(self.Chrolis01_Light_frame)
        self.Chrolis01_Value.setObjectName(u"Chrolis01_Value")
        self.Chrolis01_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.Chrolis01_Value)


        self.aa_13.addWidget(self.Chrolis01_Light_frame)


        self.verticalLayout_18.addWidget(self.Chrolis01_frame)

        self.Chrolis02_frame = QFrame(self.Chrolis_LED_frame)
        self.Chrolis02_frame.setObjectName(u"Chrolis02_frame")
        self.Chrolis02_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis02_frame.setFrameShadow(QFrame.Raised)
        self.aa_14 = QHBoxLayout(self.Chrolis02_frame)
        self.aa_14.setSpacing(5)
        self.aa_14.setObjectName(u"aa_14")
        self.aa_14.setContentsMargins(0, 0, 0, 0)
        self.Chrolis02_Display_frame = QFrame(self.Chrolis02_frame)
        self.Chrolis02_Display_frame.setObjectName(u"Chrolis02_Display_frame")
        self.Chrolis02_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis02_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis02_Display_frame.setFrameShadow(QFrame.Raised)
        self.Chrolis02_toggleButton_layout = QHBoxLayout(self.Chrolis02_Display_frame)
        self.Chrolis02_toggleButton_layout.setSpacing(0)
        self.Chrolis02_toggleButton_layout.setObjectName(u"Chrolis02_toggleButton_layout")
        self.Chrolis02_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Chrolis02_Display_label = QLabel(self.Chrolis02_Display_frame)
        self.Chrolis02_Display_label.setObjectName(u"Chrolis02_Display_label")
        self.Chrolis02_Display_label.setMaximumSize(QSize(16777215, 16777215))
        self.Chrolis02_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Chrolis02_toggleButton_layout.addWidget(self.Chrolis02_Display_label)


        self.aa_14.addWidget(self.Chrolis02_Display_frame)

        self.Chrolis02_Slider_frame = QFrame(self.Chrolis02_frame)
        self.Chrolis02_Slider_frame.setObjectName(u"Chrolis02_Slider_frame")
        self.Chrolis02_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Chrolis02_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis02_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.Chrolis02_Slider_frame)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.Chrolis02_Slider = QSlider(self.Chrolis02_Slider_frame)
        self.Chrolis02_Slider.setObjectName(u"Chrolis02_Slider")
        self.Chrolis02_Slider.setMaximumSize(QSize(16777215, 16777215))
        self.Chrolis02_Slider.setMaximum(100)
        self.Chrolis02_Slider.setSliderPosition(100)
        self.Chrolis02_Slider.setOrientation(Qt.Horizontal)
        self.Chrolis02_Slider.setTickPosition(QSlider.TicksBelow)
        self.Chrolis02_Slider.setTickInterval(10)

        self.horizontalLayout_40.addWidget(self.Chrolis02_Slider)


        self.aa_14.addWidget(self.Chrolis02_Slider_frame)

        self.Chrolis02_Light_frame = QFrame(self.Chrolis02_frame)
        self.Chrolis02_Light_frame.setObjectName(u"Chrolis02_Light_frame")
        self.Chrolis02_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Chrolis02_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis02_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.Chrolis02_Light_frame)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.Chrolis02_Value = QLabel(self.Chrolis02_Light_frame)
        self.Chrolis02_Value.setObjectName(u"Chrolis02_Value")
        self.Chrolis02_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.Chrolis02_Value)


        self.aa_14.addWidget(self.Chrolis02_Light_frame)


        self.verticalLayout_18.addWidget(self.Chrolis02_frame)

        self.Chrolis03_frame = QFrame(self.Chrolis_LED_frame)
        self.Chrolis03_frame.setObjectName(u"Chrolis03_frame")
        self.Chrolis03_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis03_frame.setFrameShadow(QFrame.Raised)
        self.aa_15 = QHBoxLayout(self.Chrolis03_frame)
        self.aa_15.setSpacing(5)
        self.aa_15.setObjectName(u"aa_15")
        self.aa_15.setContentsMargins(0, 0, 0, 0)
        self.Chrolis03_Display_frame = QFrame(self.Chrolis03_frame)
        self.Chrolis03_Display_frame.setObjectName(u"Chrolis03_Display_frame")
        self.Chrolis03_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis03_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis03_Display_frame.setFrameShadow(QFrame.Raised)
        self.Chrolis03_toggleButton_layout = QHBoxLayout(self.Chrolis03_Display_frame)
        self.Chrolis03_toggleButton_layout.setSpacing(0)
        self.Chrolis03_toggleButton_layout.setObjectName(u"Chrolis03_toggleButton_layout")
        self.Chrolis03_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Chrolis03_Display_label = QLabel(self.Chrolis03_Display_frame)
        self.Chrolis03_Display_label.setObjectName(u"Chrolis03_Display_label")
        self.Chrolis03_Display_label.setMaximumSize(QSize(16777215, 16777215))
        self.Chrolis03_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Chrolis03_toggleButton_layout.addWidget(self.Chrolis03_Display_label)


        self.aa_15.addWidget(self.Chrolis03_Display_frame)

        self.Chrolis03_Slider_frame = QFrame(self.Chrolis03_frame)
        self.Chrolis03_Slider_frame.setObjectName(u"Chrolis03_Slider_frame")
        self.Chrolis03_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Chrolis03_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis03_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.Chrolis03_Slider_frame)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.Chrolis03_Slider = QSlider(self.Chrolis03_Slider_frame)
        self.Chrolis03_Slider.setObjectName(u"Chrolis03_Slider")
        self.Chrolis03_Slider.setMaximum(100)
        self.Chrolis03_Slider.setSliderPosition(100)
        self.Chrolis03_Slider.setOrientation(Qt.Horizontal)
        self.Chrolis03_Slider.setTickPosition(QSlider.TicksBelow)
        self.Chrolis03_Slider.setTickInterval(10)

        self.horizontalLayout_41.addWidget(self.Chrolis03_Slider)


        self.aa_15.addWidget(self.Chrolis03_Slider_frame)

        self.Chrolis03_Light_frame = QFrame(self.Chrolis03_frame)
        self.Chrolis03_Light_frame.setObjectName(u"Chrolis03_Light_frame")
        self.Chrolis03_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Chrolis03_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis03_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.Chrolis03_Light_frame)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.Chrolis03_Value = QLabel(self.Chrolis03_Light_frame)
        self.Chrolis03_Value.setObjectName(u"Chrolis03_Value")
        self.Chrolis03_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.Chrolis03_Value)


        self.aa_15.addWidget(self.Chrolis03_Light_frame)


        self.verticalLayout_18.addWidget(self.Chrolis03_frame)

        self.Chrolis04_frame = QFrame(self.Chrolis_LED_frame)
        self.Chrolis04_frame.setObjectName(u"Chrolis04_frame")
        self.Chrolis04_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis04_frame.setFrameShadow(QFrame.Raised)
        self.aa_16 = QHBoxLayout(self.Chrolis04_frame)
        self.aa_16.setSpacing(5)
        self.aa_16.setObjectName(u"aa_16")
        self.aa_16.setContentsMargins(0, 0, 0, 0)
        self.Chrolis04_Display_frame = QFrame(self.Chrolis04_frame)
        self.Chrolis04_Display_frame.setObjectName(u"Chrolis04_Display_frame")
        self.Chrolis04_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis04_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis04_Display_frame.setFrameShadow(QFrame.Raised)
        self.Chrolis04_toggleButton_layout = QHBoxLayout(self.Chrolis04_Display_frame)
        self.Chrolis04_toggleButton_layout.setSpacing(0)
        self.Chrolis04_toggleButton_layout.setObjectName(u"Chrolis04_toggleButton_layout")
        self.Chrolis04_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Chrolis04_Display_label = QLabel(self.Chrolis04_Display_frame)
        self.Chrolis04_Display_label.setObjectName(u"Chrolis04_Display_label")
        self.Chrolis04_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Chrolis04_toggleButton_layout.addWidget(self.Chrolis04_Display_label)


        self.aa_16.addWidget(self.Chrolis04_Display_frame)

        self.Chrolis04_Slider_frame = QFrame(self.Chrolis04_frame)
        self.Chrolis04_Slider_frame.setObjectName(u"Chrolis04_Slider_frame")
        self.Chrolis04_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Chrolis04_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis04_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.Chrolis04_Slider_frame)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.Chrolis04_Slider = QSlider(self.Chrolis04_Slider_frame)
        self.Chrolis04_Slider.setObjectName(u"Chrolis04_Slider")
        self.Chrolis04_Slider.setMaximum(100)
        self.Chrolis04_Slider.setSliderPosition(100)
        self.Chrolis04_Slider.setOrientation(Qt.Horizontal)
        self.Chrolis04_Slider.setTickPosition(QSlider.TicksBelow)
        self.Chrolis04_Slider.setTickInterval(10)

        self.horizontalLayout_42.addWidget(self.Chrolis04_Slider)


        self.aa_16.addWidget(self.Chrolis04_Slider_frame)

        self.Chrolis04_Light_frame = QFrame(self.Chrolis04_frame)
        self.Chrolis04_Light_frame.setObjectName(u"Chrolis04_Light_frame")
        self.Chrolis04_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Chrolis04_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis04_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.Chrolis04_Light_frame)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.Chrolis04_Value = QLabel(self.Chrolis04_Light_frame)
        self.Chrolis04_Value.setObjectName(u"Chrolis04_Value")
        self.Chrolis04_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.Chrolis04_Value)


        self.aa_16.addWidget(self.Chrolis04_Light_frame)


        self.verticalLayout_18.addWidget(self.Chrolis04_frame)

        self.Chrolis05_frame = QFrame(self.Chrolis_LED_frame)
        self.Chrolis05_frame.setObjectName(u"Chrolis05_frame")
        self.Chrolis05_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis05_frame.setFrameShadow(QFrame.Raised)
        self.aa_17 = QHBoxLayout(self.Chrolis05_frame)
        self.aa_17.setSpacing(5)
        self.aa_17.setObjectName(u"aa_17")
        self.aa_17.setContentsMargins(0, 0, 0, 0)
        self.Chrolis05_Display_frame = QFrame(self.Chrolis05_frame)
        self.Chrolis05_Display_frame.setObjectName(u"Chrolis05_Display_frame")
        self.Chrolis05_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis05_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis05_Display_frame.setFrameShadow(QFrame.Raised)
        self.Chrolis05_toggleButton_layout = QHBoxLayout(self.Chrolis05_Display_frame)
        self.Chrolis05_toggleButton_layout.setSpacing(0)
        self.Chrolis05_toggleButton_layout.setObjectName(u"Chrolis05_toggleButton_layout")
        self.Chrolis05_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Chrolis05_Display_label = QLabel(self.Chrolis05_Display_frame)
        self.Chrolis05_Display_label.setObjectName(u"Chrolis05_Display_label")
        self.Chrolis05_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Chrolis05_toggleButton_layout.addWidget(self.Chrolis05_Display_label)


        self.aa_17.addWidget(self.Chrolis05_Display_frame)

        self.Chrolis05_Slider_frame = QFrame(self.Chrolis05_frame)
        self.Chrolis05_Slider_frame.setObjectName(u"Chrolis05_Slider_frame")
        self.Chrolis05_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Chrolis05_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis05_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.Chrolis05_Slider_frame)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.Chrolis05_Slider = QSlider(self.Chrolis05_Slider_frame)
        self.Chrolis05_Slider.setObjectName(u"Chrolis05_Slider")
        self.Chrolis05_Slider.setMaximum(100)
        self.Chrolis05_Slider.setSliderPosition(100)
        self.Chrolis05_Slider.setOrientation(Qt.Horizontal)
        self.Chrolis05_Slider.setTickPosition(QSlider.TicksBelow)
        self.Chrolis05_Slider.setTickInterval(10)

        self.horizontalLayout_43.addWidget(self.Chrolis05_Slider)


        self.aa_17.addWidget(self.Chrolis05_Slider_frame)

        self.Chrolis05_Light_frame = QFrame(self.Chrolis05_frame)
        self.Chrolis05_Light_frame.setObjectName(u"Chrolis05_Light_frame")
        self.Chrolis05_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Chrolis05_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis05_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.Chrolis05_Light_frame)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.Chrolis05_Value = QLabel(self.Chrolis05_Light_frame)
        self.Chrolis05_Value.setObjectName(u"Chrolis05_Value")
        self.Chrolis05_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.Chrolis05_Value)


        self.aa_17.addWidget(self.Chrolis05_Light_frame)


        self.verticalLayout_18.addWidget(self.Chrolis05_frame)

        self.Chrolis06_frame = QFrame(self.Chrolis_LED_frame)
        self.Chrolis06_frame.setObjectName(u"Chrolis06_frame")
        self.Chrolis06_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis06_frame.setFrameShadow(QFrame.Raised)
        self.aa_18 = QHBoxLayout(self.Chrolis06_frame)
        self.aa_18.setSpacing(5)
        self.aa_18.setObjectName(u"aa_18")
        self.aa_18.setContentsMargins(0, 0, 0, 0)
        self.Chrolis06_Display_frame = QFrame(self.Chrolis06_frame)
        self.Chrolis06_Display_frame.setObjectName(u"Chrolis06_Display_frame")
        self.Chrolis06_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis06_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis06_Display_frame.setFrameShadow(QFrame.Raised)
        self.Chrolis06_toggleButton_layout = QHBoxLayout(self.Chrolis06_Display_frame)
        self.Chrolis06_toggleButton_layout.setSpacing(0)
        self.Chrolis06_toggleButton_layout.setObjectName(u"Chrolis06_toggleButton_layout")
        self.Chrolis06_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Chrolis06_Display_label = QLabel(self.Chrolis06_Display_frame)
        self.Chrolis06_Display_label.setObjectName(u"Chrolis06_Display_label")
        self.Chrolis06_Display_label.setMaximumSize(QSize(200, 16777215))
        self.Chrolis06_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Chrolis06_toggleButton_layout.addWidget(self.Chrolis06_Display_label)


        self.aa_18.addWidget(self.Chrolis06_Display_frame)

        self.Chrolis06_Slider_frame = QFrame(self.Chrolis06_frame)
        self.Chrolis06_Slider_frame.setObjectName(u"Chrolis06_Slider_frame")
        self.Chrolis06_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Chrolis06_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis06_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.Chrolis06_Slider_frame)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.Chrolis06_Slider = QSlider(self.Chrolis06_Slider_frame)
        self.Chrolis06_Slider.setObjectName(u"Chrolis06_Slider")
        self.Chrolis06_Slider.setMaximum(100)
        self.Chrolis06_Slider.setValue(100)
        self.Chrolis06_Slider.setSliderPosition(100)
        self.Chrolis06_Slider.setOrientation(Qt.Horizontal)
        self.Chrolis06_Slider.setTickPosition(QSlider.TicksBelow)
        self.Chrolis06_Slider.setTickInterval(10)

        self.horizontalLayout_44.addWidget(self.Chrolis06_Slider)


        self.aa_18.addWidget(self.Chrolis06_Slider_frame)

        self.Chrolis06_Light_frame = QFrame(self.Chrolis06_frame)
        self.Chrolis06_Light_frame.setObjectName(u"Chrolis06_Light_frame")
        self.Chrolis06_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Chrolis06_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis06_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.Chrolis06_Light_frame)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.Chrolis06_Value = QLabel(self.Chrolis06_Light_frame)
        self.Chrolis06_Value.setObjectName(u"Chrolis06_Value")
        self.Chrolis06_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.Chrolis06_Value)


        self.aa_18.addWidget(self.Chrolis06_Light_frame)


        self.verticalLayout_18.addWidget(self.Chrolis06_frame)

        self.Chrolis07_frame = QFrame(self.Chrolis_LED_frame)
        self.Chrolis07_frame.setObjectName(u"Chrolis07_frame")
        self.Chrolis07_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis07_frame.setFrameShadow(QFrame.Raised)
        self.aa_19 = QHBoxLayout(self.Chrolis07_frame)
        self.aa_19.setSpacing(5)
        self.aa_19.setObjectName(u"aa_19")
        self.aa_19.setContentsMargins(0, 0, 0, 0)
        self.Chrolis07_Display_frame = QFrame(self.Chrolis07_frame)
        self.Chrolis07_Display_frame.setObjectName(u"Chrolis07_Display_frame")
        self.Chrolis07_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis07_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis07_Display_frame.setFrameShadow(QFrame.Raised)
        self.Chrolis07_toggleButton_layout = QHBoxLayout(self.Chrolis07_Display_frame)
        self.Chrolis07_toggleButton_layout.setSpacing(0)
        self.Chrolis07_toggleButton_layout.setObjectName(u"Chrolis07_toggleButton_layout")
        self.Chrolis07_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Chrolis07_Display_label = QLabel(self.Chrolis07_Display_frame)
        self.Chrolis07_Display_label.setObjectName(u"Chrolis07_Display_label")
        self.Chrolis07_Display_label.setMaximumSize(QSize(16777215, 16777215))
        self.Chrolis07_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Chrolis07_toggleButton_layout.addWidget(self.Chrolis07_Display_label)


        self.aa_19.addWidget(self.Chrolis07_Display_frame)

        self.Chrolis07_Slider_frame = QFrame(self.Chrolis07_frame)
        self.Chrolis07_Slider_frame.setObjectName(u"Chrolis07_Slider_frame")
        self.Chrolis07_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Chrolis07_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis07_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.Chrolis07_Slider_frame)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.Chrolis07_Slider = QSlider(self.Chrolis07_Slider_frame)
        self.Chrolis07_Slider.setObjectName(u"Chrolis07_Slider")
        self.Chrolis07_Slider.setMaximum(100)
        self.Chrolis07_Slider.setSliderPosition(100)
        self.Chrolis07_Slider.setOrientation(Qt.Horizontal)
        self.Chrolis07_Slider.setTickPosition(QSlider.TicksBelow)
        self.Chrolis07_Slider.setTickInterval(10)

        self.horizontalLayout_45.addWidget(self.Chrolis07_Slider)


        self.aa_19.addWidget(self.Chrolis07_Slider_frame)

        self.Chrolis07_Light_frame = QFrame(self.Chrolis07_frame)
        self.Chrolis07_Light_frame.setObjectName(u"Chrolis07_Light_frame")
        self.Chrolis07_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Chrolis07_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis07_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.Chrolis07_Light_frame)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.Chrolis07_Value = QLabel(self.Chrolis07_Light_frame)
        self.Chrolis07_Value.setObjectName(u"Chrolis07_Value")
        self.Chrolis07_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.Chrolis07_Value)


        self.aa_19.addWidget(self.Chrolis07_Light_frame)


        self.verticalLayout_18.addWidget(self.Chrolis07_frame)

        self.Chrolis08_frame = QFrame(self.Chrolis_LED_frame)
        self.Chrolis08_frame.setObjectName(u"Chrolis08_frame")
        self.Chrolis08_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis08_frame.setFrameShadow(QFrame.Raised)
        self.aa_20 = QHBoxLayout(self.Chrolis08_frame)
        self.aa_20.setSpacing(5)
        self.aa_20.setObjectName(u"aa_20")
        self.aa_20.setContentsMargins(0, 0, 0, 0)
        self.Chrolis08_Display_frame = QFrame(self.Chrolis08_frame)
        self.Chrolis08_Display_frame.setObjectName(u"Chrolis08_Display_frame")
        self.Chrolis08_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis08_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis08_Display_frame.setFrameShadow(QFrame.Raised)
        self.Chrolis08_toggleButton_layout = QHBoxLayout(self.Chrolis08_Display_frame)
        self.Chrolis08_toggleButton_layout.setSpacing(0)
        self.Chrolis08_toggleButton_layout.setObjectName(u"Chrolis08_toggleButton_layout")
        self.Chrolis08_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Chrolis08_Display_label = QLabel(self.Chrolis08_Display_frame)
        self.Chrolis08_Display_label.setObjectName(u"Chrolis08_Display_label")
        self.Chrolis08_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Chrolis08_toggleButton_layout.addWidget(self.Chrolis08_Display_label)


        self.aa_20.addWidget(self.Chrolis08_Display_frame)

        self.Chrolis08_Slider_frame = QFrame(self.Chrolis08_frame)
        self.Chrolis08_Slider_frame.setObjectName(u"Chrolis08_Slider_frame")
        self.Chrolis08_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Chrolis08_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis08_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.Chrolis08_Slider_frame)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.Chrolis08_Slider = QSlider(self.Chrolis08_Slider_frame)
        self.Chrolis08_Slider.setObjectName(u"Chrolis08_Slider")
        self.Chrolis08_Slider.setMaximum(100)
        self.Chrolis08_Slider.setSliderPosition(100)
        self.Chrolis08_Slider.setOrientation(Qt.Horizontal)
        self.Chrolis08_Slider.setTickPosition(QSlider.TicksBelow)
        self.Chrolis08_Slider.setTickInterval(10)

        self.horizontalLayout_69.addWidget(self.Chrolis08_Slider)


        self.aa_20.addWidget(self.Chrolis08_Slider_frame)

        self.Chrolis08_Light_frame = QFrame(self.Chrolis08_frame)
        self.Chrolis08_Light_frame.setObjectName(u"Chrolis08_Light_frame")
        self.Chrolis08_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Chrolis08_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis08_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.Chrolis08_Light_frame)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.Chrolis08_Value = QLabel(self.Chrolis08_Light_frame)
        self.Chrolis08_Value.setObjectName(u"Chrolis08_Value")
        self.Chrolis08_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_70.addWidget(self.Chrolis08_Value)


        self.aa_20.addWidget(self.Chrolis08_Light_frame)


        self.verticalLayout_18.addWidget(self.Chrolis08_frame)

        self.Chrolis09_frame = QFrame(self.Chrolis_LED_frame)
        self.Chrolis09_frame.setObjectName(u"Chrolis09_frame")
        self.Chrolis09_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis09_frame.setFrameShadow(QFrame.Raised)
        self.aa_21 = QHBoxLayout(self.Chrolis09_frame)
        self.aa_21.setSpacing(5)
        self.aa_21.setObjectName(u"aa_21")
        self.aa_21.setContentsMargins(0, 0, 0, 0)
        self.Chrolis09_Display_frame = QFrame(self.Chrolis09_frame)
        self.Chrolis09_Display_frame.setObjectName(u"Chrolis09_Display_frame")
        self.Chrolis09_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis09_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis09_Display_frame.setFrameShadow(QFrame.Raised)
        self.Chrolis09_toggleButton_layout = QHBoxLayout(self.Chrolis09_Display_frame)
        self.Chrolis09_toggleButton_layout.setSpacing(0)
        self.Chrolis09_toggleButton_layout.setObjectName(u"Chrolis09_toggleButton_layout")
        self.Chrolis09_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Chrolis09_Display_label = QLabel(self.Chrolis09_Display_frame)
        self.Chrolis09_Display_label.setObjectName(u"Chrolis09_Display_label")
        self.Chrolis09_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Chrolis09_toggleButton_layout.addWidget(self.Chrolis09_Display_label)


        self.aa_21.addWidget(self.Chrolis09_Display_frame)

        self.Chrolis09_Slider_frame = QFrame(self.Chrolis09_frame)
        self.Chrolis09_Slider_frame.setObjectName(u"Chrolis09_Slider_frame")
        self.Chrolis09_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Chrolis09_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis09_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.Chrolis09_Slider_frame)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.Chrolis09_Slider = QSlider(self.Chrolis09_Slider_frame)
        self.Chrolis09_Slider.setObjectName(u"Chrolis09_Slider")
        self.Chrolis09_Slider.setMaximum(100)
        self.Chrolis09_Slider.setSliderPosition(100)
        self.Chrolis09_Slider.setOrientation(Qt.Horizontal)
        self.Chrolis09_Slider.setTickPosition(QSlider.TicksBelow)
        self.Chrolis09_Slider.setTickInterval(10)

        self.horizontalLayout_71.addWidget(self.Chrolis09_Slider)


        self.aa_21.addWidget(self.Chrolis09_Slider_frame)

        self.Chrolis09_Light_frame = QFrame(self.Chrolis09_frame)
        self.Chrolis09_Light_frame.setObjectName(u"Chrolis09_Light_frame")
        self.Chrolis09_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Chrolis09_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis09_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.Chrolis09_Light_frame)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.Chrolis09_Value = QLabel(self.Chrolis09_Light_frame)
        self.Chrolis09_Value.setObjectName(u"Chrolis09_Value")
        self.Chrolis09_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.Chrolis09_Value)


        self.aa_21.addWidget(self.Chrolis09_Light_frame)


        self.verticalLayout_18.addWidget(self.Chrolis09_frame)

        self.Chrolis10_frame = QFrame(self.Chrolis_LED_frame)
        self.Chrolis10_frame.setObjectName(u"Chrolis10_frame")
        self.Chrolis10_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis10_frame.setFrameShadow(QFrame.Raised)
        self.aa_22 = QHBoxLayout(self.Chrolis10_frame)
        self.aa_22.setSpacing(5)
        self.aa_22.setObjectName(u"aa_22")
        self.aa_22.setContentsMargins(0, 0, 0, 0)
        self.Chrolis10_Display_frame = QFrame(self.Chrolis10_frame)
        self.Chrolis10_Display_frame.setObjectName(u"Chrolis10_Display_frame")
        self.Chrolis10_Display_frame.setMaximumSize(QSize(1265, 16777215))
        self.Chrolis10_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis10_Display_frame.setFrameShadow(QFrame.Raised)
        self.Chrolis10_toggleButton_layout = QHBoxLayout(self.Chrolis10_Display_frame)
        self.Chrolis10_toggleButton_layout.setSpacing(0)
        self.Chrolis10_toggleButton_layout.setObjectName(u"Chrolis10_toggleButton_layout")
        self.Chrolis10_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Chrolis10_Display_label = QLabel(self.Chrolis10_Display_frame)
        self.Chrolis10_Display_label.setObjectName(u"Chrolis10_Display_label")
        self.Chrolis10_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Chrolis10_toggleButton_layout.addWidget(self.Chrolis10_Display_label)


        self.aa_22.addWidget(self.Chrolis10_Display_frame)

        self.Chrolis10_Slider_frame = QFrame(self.Chrolis10_frame)
        self.Chrolis10_Slider_frame.setObjectName(u"Chrolis10_Slider_frame")
        self.Chrolis10_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Chrolis10_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis10_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.Chrolis10_Slider_frame)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.Chrolis10_Slider = QSlider(self.Chrolis10_Slider_frame)
        self.Chrolis10_Slider.setObjectName(u"Chrolis10_Slider")
        self.Chrolis10_Slider.setMaximum(100)
        self.Chrolis10_Slider.setSliderPosition(100)
        self.Chrolis10_Slider.setOrientation(Qt.Horizontal)
        self.Chrolis10_Slider.setTickPosition(QSlider.TicksBelow)
        self.Chrolis10_Slider.setTickInterval(10)

        self.horizontalLayout_73.addWidget(self.Chrolis10_Slider)


        self.aa_22.addWidget(self.Chrolis10_Slider_frame)

        self.Chrolis10_Light_frame = QFrame(self.Chrolis10_frame)
        self.Chrolis10_Light_frame.setObjectName(u"Chrolis10_Light_frame")
        self.Chrolis10_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Chrolis10_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis10_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.Chrolis10_Light_frame)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.Chrolis10_Value = QLabel(self.Chrolis10_Light_frame)
        self.Chrolis10_Value.setObjectName(u"Chrolis10_Value")
        self.Chrolis10_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.Chrolis10_Value)


        self.aa_22.addWidget(self.Chrolis10_Light_frame)


        self.verticalLayout_18.addWidget(self.Chrolis10_frame)

        self.Chrolis11_frame = QFrame(self.Chrolis_LED_frame)
        self.Chrolis11_frame.setObjectName(u"Chrolis11_frame")
        self.Chrolis11_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis11_frame.setFrameShadow(QFrame.Raised)
        self.aa_23 = QHBoxLayout(self.Chrolis11_frame)
        self.aa_23.setSpacing(5)
        self.aa_23.setObjectName(u"aa_23")
        self.aa_23.setContentsMargins(0, 0, 0, 0)
        self.Chrolis11_Display_frame = QFrame(self.Chrolis11_frame)
        self.Chrolis11_Display_frame.setObjectName(u"Chrolis11_Display_frame")
        self.Chrolis11_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis11_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis11_Display_frame.setFrameShadow(QFrame.Raised)
        self.Chrolis11_toggleButton_layout = QHBoxLayout(self.Chrolis11_Display_frame)
        self.Chrolis11_toggleButton_layout.setSpacing(0)
        self.Chrolis11_toggleButton_layout.setObjectName(u"Chrolis11_toggleButton_layout")
        self.Chrolis11_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Chrolis11_Display_label = QLabel(self.Chrolis11_Display_frame)
        self.Chrolis11_Display_label.setObjectName(u"Chrolis11_Display_label")
        self.Chrolis11_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Chrolis11_toggleButton_layout.addWidget(self.Chrolis11_Display_label)


        self.aa_23.addWidget(self.Chrolis11_Display_frame)

        self.Chrolis11_Slider_frame = QFrame(self.Chrolis11_frame)
        self.Chrolis11_Slider_frame.setObjectName(u"Chrolis11_Slider_frame")
        self.Chrolis11_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Chrolis11_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis11_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.Chrolis11_Slider_frame)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.Chrolis11_Slider = QSlider(self.Chrolis11_Slider_frame)
        self.Chrolis11_Slider.setObjectName(u"Chrolis11_Slider")
        self.Chrolis11_Slider.setMaximum(100)
        self.Chrolis11_Slider.setSliderPosition(100)
        self.Chrolis11_Slider.setOrientation(Qt.Horizontal)
        self.Chrolis11_Slider.setTickPosition(QSlider.TicksBelow)
        self.Chrolis11_Slider.setTickInterval(10)

        self.horizontalLayout_75.addWidget(self.Chrolis11_Slider)


        self.aa_23.addWidget(self.Chrolis11_Slider_frame)

        self.Chrolis11_Light_frame = QFrame(self.Chrolis11_frame)
        self.Chrolis11_Light_frame.setObjectName(u"Chrolis11_Light_frame")
        self.Chrolis11_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Chrolis11_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis11_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.Chrolis11_Light_frame)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.Chrolis11_Value = QLabel(self.Chrolis11_Light_frame)
        self.Chrolis11_Value.setObjectName(u"Chrolis11_Value")
        self.Chrolis11_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_76.addWidget(self.Chrolis11_Value)


        self.aa_23.addWidget(self.Chrolis11_Light_frame)


        self.verticalLayout_18.addWidget(self.Chrolis11_frame)

        self.Chrolis12_frame = QFrame(self.Chrolis_LED_frame)
        self.Chrolis12_frame.setObjectName(u"Chrolis12_frame")
        self.Chrolis12_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis12_frame.setFrameShadow(QFrame.Raised)
        self.aa_24 = QHBoxLayout(self.Chrolis12_frame)
        self.aa_24.setSpacing(5)
        self.aa_24.setObjectName(u"aa_24")
        self.aa_24.setContentsMargins(0, 0, 0, 0)
        self.Chrolis12_Display_frame = QFrame(self.Chrolis12_frame)
        self.Chrolis12_Display_frame.setObjectName(u"Chrolis12_Display_frame")
        self.Chrolis12_Display_frame.setMaximumSize(QSize(125, 16777215))
        self.Chrolis12_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis12_Display_frame.setFrameShadow(QFrame.Raised)
        self.Chrolis12_toggleButton_layout = QHBoxLayout(self.Chrolis12_Display_frame)
        self.Chrolis12_toggleButton_layout.setSpacing(0)
        self.Chrolis12_toggleButton_layout.setObjectName(u"Chrolis12_toggleButton_layout")
        self.Chrolis12_toggleButton_layout.setContentsMargins(0, 0, 5, 0)
        self.Chrolis12_Display_label = QLabel(self.Chrolis12_Display_frame)
        self.Chrolis12_Display_label.setObjectName(u"Chrolis12_Display_label")
        self.Chrolis12_Display_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.Chrolis12_toggleButton_layout.addWidget(self.Chrolis12_Display_label)


        self.aa_24.addWidget(self.Chrolis12_Display_frame)

        self.Chrolis12_Slider_frame = QFrame(self.Chrolis12_frame)
        self.Chrolis12_Slider_frame.setObjectName(u"Chrolis12_Slider_frame")
        self.Chrolis12_Slider_frame.setMaximumSize(QSize(225, 16777215))
        self.Chrolis12_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis12_Slider_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.Chrolis12_Slider_frame)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.Chrolis12_Slider = QSlider(self.Chrolis12_Slider_frame)
        self.Chrolis12_Slider.setObjectName(u"Chrolis12_Slider")
        self.Chrolis12_Slider.setMaximum(100)
        self.Chrolis12_Slider.setSliderPosition(100)
        self.Chrolis12_Slider.setOrientation(Qt.Horizontal)
        self.Chrolis12_Slider.setTickPosition(QSlider.TicksBelow)
        self.Chrolis12_Slider.setTickInterval(10)

        self.horizontalLayout_77.addWidget(self.Chrolis12_Slider)


        self.aa_24.addWidget(self.Chrolis12_Slider_frame)

        self.Chrolis12_Light_frame = QFrame(self.Chrolis12_frame)
        self.Chrolis12_Light_frame.setObjectName(u"Chrolis12_Light_frame")
        self.Chrolis12_Light_frame.setMaximumSize(QSize(50, 16777215))
        self.Chrolis12_Light_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis12_Light_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.Chrolis12_Light_frame)
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.Chrolis12_Value = QLabel(self.Chrolis12_Light_frame)
        self.Chrolis12_Value.setObjectName(u"Chrolis12_Value")
        self.Chrolis12_Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.Chrolis12_Value)


        self.aa_24.addWidget(self.Chrolis12_Light_frame)


        self.verticalLayout_18.addWidget(self.Chrolis12_frame)


        self.verticalLayout_14.addWidget(self.Chrolis_LED_frame)


        self.horizontalLayout_32.addWidget(self.Chrolis_Stimulus_frame)


        self.verticalLayout_15.addWidget(self.Chrolis_Frame)

        self.Main_stackedWidget.addWidget(self.Chrolis_Page)
        self.Stimulus_Page = QWidget()
        self.Stimulus_Page.setObjectName(u"Stimulus_Page")
        self.Main_stackedWidget.addWidget(self.Stimulus_Page)
        self.About_Page = QWidget()
        self.About_Page.setObjectName(u"About_Page")
        self.Main_stackedWidget.addWidget(self.About_Page)
        self.GitHub_Page = QWidget()
        self.GitHub_Page.setObjectName(u"GitHub_Page")
        self.Main_stackedWidget.addWidget(self.GitHub_Page)
        self.Help_Page = QWidget()
        self.Help_Page.setObjectName(u"Help_Page")
        self.Main_stackedWidget.addWidget(self.Help_Page)
        self.Settings_Page = QWidget()
        self.Settings_Page.setObjectName(u"Settings_Page")
        self.Main_stackedWidget.addWidget(self.Settings_Page)
        self.Spectra_Page = QWidget()
        self.Spectra_Page.setObjectName(u"Spectra_Page")
        self.horizontalLayout_18 = QHBoxLayout(self.Spectra_Page)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.SpectraPlot_Frame = QFrame(self.Spectra_Page)
        self.SpectraPlot_Frame.setObjectName(u"SpectraPlot_Frame")
        self.SpectraPlot_Frame.setFrameShape(QFrame.StyledPanel)
        self.SpectraPlot_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.SpectraPlot_Frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Spectra_plotWidget_Frame = QFrame(self.SpectraPlot_Frame)
        self.Spectra_plotWidget_Frame.setObjectName(u"Spectra_plotWidget_Frame")
        self.Spectra_plotWidget_Frame.setFrameShape(QFrame.StyledPanel)
        self.Spectra_plotWidget_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.Spectra_plotWidget_Frame)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.Spectra_plotWidget = PlotWidget(self.Spectra_plotWidget_Frame)
        self.Spectra_plotWidget.setObjectName(u"Spectra_plotWidget")

        self.horizontalLayout_17.addWidget(self.Spectra_plotWidget)


        self.verticalLayout_10.addWidget(self.Spectra_plotWidget_Frame)

        self.frame_5 = QFrame(self.SpectraPlot_Frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_5)


        self.horizontalLayout_18.addWidget(self.SpectraPlot_Frame)

        self.line_3 = QFrame(self.Spectra_Page)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_18.addWidget(self.line_3)

        self.Spectra_CenterMenu_container = QFrame(self.Spectra_Page)
        self.Spectra_CenterMenu_container.setObjectName(u"Spectra_CenterMenu_container")
        self.Spectra_CenterMenu_container.setMaximumSize(QSize(200, 16777215))
        self.Spectra_CenterMenu_container.setFrameShape(QFrame.StyledPanel)
        self.Spectra_CenterMenu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.Spectra_CenterMenu_container)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.Spectra_CenterMenu_Hide_frame = QFrame(self.Spectra_CenterMenu_container)
        self.Spectra_CenterMenu_Hide_frame.setObjectName(u"Spectra_CenterMenu_Hide_frame")
        self.Spectra_CenterMenu_Hide_frame.setFrameShape(QFrame.StyledPanel)
        self.Spectra_CenterMenu_Hide_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.Spectra_CenterMenu_Hide_frame)
        self.horizontalLayout_117.setSpacing(0)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.Spectra_CenterMenu_Hide_pushButton = QPushButton(self.Spectra_CenterMenu_Hide_frame)
        self.Spectra_CenterMenu_Hide_pushButton.setObjectName(u"Spectra_CenterMenu_Hide_pushButton")
        icon13 = QIcon()
        icon13.addFile(u":/resources/resources/DropMenuRight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Spectra_CenterMenu_Hide_pushButton.setIcon(icon13)
        self.Spectra_CenterMenu_Hide_pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_117.addWidget(self.Spectra_CenterMenu_Hide_pushButton, 0, Qt.AlignLeft)


        self.verticalLayout_44.addWidget(self.Spectra_CenterMenu_Hide_frame)

        self.Spectra_stackedWidget = QStackedWidget(self.Spectra_CenterMenu_container)
        self.Spectra_stackedWidget.setObjectName(u"Spectra_stackedWidget")
        self.OpsinSpectra_page = QWidget()
        self.OpsinSpectra_page.setObjectName(u"OpsinSpectra_page")
        self.verticalLayout_45 = QVBoxLayout(self.OpsinSpectra_page)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.OpsinSpectra_frame = QFrame(self.OpsinSpectra_page)
        self.OpsinSpectra_frame.setObjectName(u"OpsinSpectra_frame")
        self.OpsinSpectra_frame.setFrameShape(QFrame.StyledPanel)
        self.OpsinSpectra_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.OpsinSpectra_frame)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 20)
        self.OpsinSpectra_Title_frame = QFrame(self.OpsinSpectra_frame)
        self.OpsinSpectra_Title_frame.setObjectName(u"OpsinSpectra_Title_frame")
        self.OpsinSpectra_Title_frame.setMaximumSize(QSize(16777215, 40))
        self.OpsinSpectra_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.OpsinSpectra_Title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.OpsinSpectra_Title_frame)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(5, 10, 5, 10)
        self.OpsinSpectra_Title = QLabel(self.OpsinSpectra_Title_frame)
        self.OpsinSpectra_Title.setObjectName(u"OpsinSpectra_Title")
        self.OpsinSpectra_Title.setFont(font1)
        self.OpsinSpectra_Title.setMidLineWidth(0)

        self.verticalLayout_48.addWidget(self.OpsinSpectra_Title, 0, Qt.AlignHCenter)


        self.verticalLayout_47.addWidget(self.OpsinSpectra_Title_frame)

        self.OpsinSpectra_Load_frame = QFrame(self.OpsinSpectra_frame)
        self.OpsinSpectra_Load_frame.setObjectName(u"OpsinSpectra_Load_frame")
        self.OpsinSpectra_Load_frame.setMaximumSize(QSize(16777215, 125))
        self.OpsinSpectra_Load_frame.setFrameShape(QFrame.StyledPanel)
        self.OpsinSpectra_Load_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.OpsinSpectra_Load_frame)
        self.verticalLayout_51.setSpacing(10)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(5, 20, 5, 10)
        self.OpsinSpectra_Load_label = QLabel(self.OpsinSpectra_Load_frame)
        self.OpsinSpectra_Load_label.setObjectName(u"OpsinSpectra_Load_label")
        self.OpsinSpectra_Load_label.setAlignment(Qt.AlignCenter)
        self.OpsinSpectra_Load_label.setWordWrap(True)

        self.verticalLayout_51.addWidget(self.OpsinSpectra_Load_label)

        self.OpsinSpectra_Load_comboBox_frame = QFrame(self.OpsinSpectra_Load_frame)
        self.OpsinSpectra_Load_comboBox_frame.setObjectName(u"OpsinSpectra_Load_comboBox_frame")
        self.OpsinSpectra_Load_comboBox_frame.setMinimumSize(QSize(0, 0))
        self.OpsinSpectra_Load_comboBox_frame.setMaximumSize(QSize(16777215, 25))
        self.OpsinSpectra_Load_comboBox_frame.setFrameShape(QFrame.StyledPanel)
        self.OpsinSpectra_Load_comboBox_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.OpsinSpectra_Load_comboBox_frame)
        self.horizontalLayout_120.setSpacing(0)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(5, 0, 5, 0)
        self.OpsinSpectra_Load_comboBox = QComboBox(self.OpsinSpectra_Load_comboBox_frame)
        self.OpsinSpectra_Load_comboBox.addItem("")
        self.OpsinSpectra_Load_comboBox.addItem("")
        self.OpsinSpectra_Load_comboBox.addItem("")
        self.OpsinSpectra_Load_comboBox.addItem("")
        self.OpsinSpectra_Load_comboBox.addItem("")
        self.OpsinSpectra_Load_comboBox.addItem("")
        self.OpsinSpectra_Load_comboBox.setObjectName(u"OpsinSpectra_Load_comboBox")
        font7 = QFont()
        font7.setPointSize(11)
        self.OpsinSpectra_Load_comboBox.setFont(font7)
        self.OpsinSpectra_Load_comboBox.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_120.addWidget(self.OpsinSpectra_Load_comboBox)


        self.verticalLayout_51.addWidget(self.OpsinSpectra_Load_comboBox_frame)


        self.verticalLayout_47.addWidget(self.OpsinSpectra_Load_frame)

        self.line_4 = QFrame(self.OpsinSpectra_frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_47.addWidget(self.line_4)

        self.OpsinSpectra_Display_frame = QFrame(self.OpsinSpectra_frame)
        self.OpsinSpectra_Display_frame.setObjectName(u"OpsinSpectra_Display_frame")
        self.OpsinSpectra_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.OpsinSpectra_Display_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.OpsinSpectra_Display_frame)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(5, 10, 5, 10)
        self.OpsinSpectra_DisplayOpsin_pushButton_frame = QFrame(self.OpsinSpectra_Display_frame)
        self.OpsinSpectra_DisplayOpsin_pushButton_frame.setObjectName(u"OpsinSpectra_DisplayOpsin_pushButton_frame")
        self.OpsinSpectra_DisplayOpsin_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.OpsinSpectra_DisplayOpsin_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.OpsinSpectra_DisplayOpsin_pushButton_frame)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(5, 5, 5, 5)
        self.OpsinSpectra_DisplayOpsin_pushButton = QPushButton(self.OpsinSpectra_DisplayOpsin_pushButton_frame)
        self.OpsinSpectra_DisplayOpsin_pushButton.setObjectName(u"OpsinSpectra_DisplayOpsin_pushButton")

        self.verticalLayout_52.addWidget(self.OpsinSpectra_DisplayOpsin_pushButton)


        self.verticalLayout_49.addWidget(self.OpsinSpectra_DisplayOpsin_pushButton_frame)

        self.OpsinSpectra_stackedWidget = QStackedWidget(self.OpsinSpectra_Display_frame)
        self.OpsinSpectra_stackedWidget.setObjectName(u"OpsinSpectra_stackedWidget")
        self.Blank_page = QWidget()
        self.Blank_page.setObjectName(u"Blank_page")
        self.OpsinSpectra_stackedWidget.addWidget(self.Blank_page)
        self.Human_page = QWidget()
        self.Human_page.setObjectName(u"Human_page")
        self.verticalLayout_64 = QVBoxLayout(self.Human_page)
        self.verticalLayout_64.setSpacing(5)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(5, 5, 5, 5)
        self.Human_frame = QFrame(self.Human_page)
        self.Human_frame.setObjectName(u"Human_frame")
        self.Human_frame.setFrameShape(QFrame.StyledPanel)
        self.Human_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.Human_frame)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.Human_Blue = QFrame(self.Human_frame)
        self.Human_Blue.setObjectName(u"Human_Blue")
        self.Human_Blue.setFrameShape(QFrame.StyledPanel)
        self.Human_Blue.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.Human_Blue)
        self.horizontalLayout_125.setSpacing(0)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.Human_Blue_toggleButton_frame = QFrame(self.Human_Blue)
        self.Human_Blue_toggleButton_frame.setObjectName(u"Human_Blue_toggleButton_frame")
        self.Human_Blue_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Human_Blue_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Human_Blue_layout = QVBoxLayout(self.Human_Blue_toggleButton_frame)
        self.Human_Blue_layout.setSpacing(0)
        self.Human_Blue_layout.setObjectName(u"Human_Blue_layout")
        self.Human_Blue_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_125.addWidget(self.Human_Blue_toggleButton_frame)

        self.Human_Blue_label_frame = QFrame(self.Human_Blue)
        self.Human_Blue_label_frame.setObjectName(u"Human_Blue_label_frame")
        self.Human_Blue_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Human_Blue_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.Human_Blue_label_frame)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.Human_Blue_label = QLabel(self.Human_Blue_label_frame)
        self.Human_Blue_label.setObjectName(u"Human_Blue_label")
        self.Human_Blue_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_61.addWidget(self.Human_Blue_label)


        self.horizontalLayout_125.addWidget(self.Human_Blue_label_frame)


        self.verticalLayout_59.addWidget(self.Human_Blue)

        self.Human_Green = QFrame(self.Human_frame)
        self.Human_Green.setObjectName(u"Human_Green")
        self.Human_Green.setFrameShape(QFrame.StyledPanel)
        self.Human_Green.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.Human_Green)
        self.horizontalLayout_126.setSpacing(0)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.Human_Green_toggleButton_frame = QFrame(self.Human_Green)
        self.Human_Green_toggleButton_frame.setObjectName(u"Human_Green_toggleButton_frame")
        self.Human_Green_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Human_Green_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Human_Green_layout = QVBoxLayout(self.Human_Green_toggleButton_frame)
        self.Human_Green_layout.setSpacing(0)
        self.Human_Green_layout.setObjectName(u"Human_Green_layout")
        self.Human_Green_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_126.addWidget(self.Human_Green_toggleButton_frame)

        self.Human_Green_label_frame = QFrame(self.Human_Green)
        self.Human_Green_label_frame.setObjectName(u"Human_Green_label_frame")
        self.Human_Green_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Human_Green_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.Human_Green_label_frame)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.Human_Green_label = QLabel(self.Human_Green_label_frame)
        self.Human_Green_label.setObjectName(u"Human_Green_label")
        self.Human_Green_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.Human_Green_label)


        self.horizontalLayout_126.addWidget(self.Human_Green_label_frame)


        self.verticalLayout_59.addWidget(self.Human_Green)

        self.Human_Red = QFrame(self.Human_frame)
        self.Human_Red.setObjectName(u"Human_Red")
        self.Human_Red.setFrameShape(QFrame.StyledPanel)
        self.Human_Red.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_127 = QHBoxLayout(self.Human_Red)
        self.horizontalLayout_127.setSpacing(0)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.Human_Red_toggleButton_frame = QFrame(self.Human_Red)
        self.Human_Red_toggleButton_frame.setObjectName(u"Human_Red_toggleButton_frame")
        self.Human_Red_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Human_Red_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Human_Red_layout = QVBoxLayout(self.Human_Red_toggleButton_frame)
        self.Human_Red_layout.setSpacing(0)
        self.Human_Red_layout.setObjectName(u"Human_Red_layout")
        self.Human_Red_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_127.addWidget(self.Human_Red_toggleButton_frame)

        self.Human_Red_label_frame = QFrame(self.Human_Red)
        self.Human_Red_label_frame.setObjectName(u"Human_Red_label_frame")
        self.Human_Red_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Human_Red_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.Human_Red_label_frame)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.Human_Red_label = QLabel(self.Human_Red_label_frame)
        self.Human_Red_label.setObjectName(u"Human_Red_label")
        self.Human_Red_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_63.addWidget(self.Human_Red_label)


        self.horizontalLayout_127.addWidget(self.Human_Red_label_frame)


        self.verticalLayout_59.addWidget(self.Human_Red)


        self.verticalLayout_64.addWidget(self.Human_frame)

        self.OpsinSpectra_stackedWidget.addWidget(self.Human_page)
        self.Zebrafish_page = QWidget()
        self.Zebrafish_page.setObjectName(u"Zebrafish_page")
        self.verticalLayout_53 = QVBoxLayout(self.Zebrafish_page)
        self.verticalLayout_53.setSpacing(5)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(5, 5, 5, 5)
        self.Zebrafish_frame = QFrame(self.Zebrafish_page)
        self.Zebrafish_frame.setObjectName(u"Zebrafish_frame")
        self.Zebrafish_frame.setFrameShape(QFrame.StyledPanel)
        self.Zebrafish_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.Zebrafish_frame)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.Zebrafish_UV = QFrame(self.Zebrafish_frame)
        self.Zebrafish_UV.setObjectName(u"Zebrafish_UV")
        self.Zebrafish_UV.setFrameShape(QFrame.StyledPanel)
        self.Zebrafish_UV.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_118 = QHBoxLayout(self.Zebrafish_UV)
        self.horizontalLayout_118.setSpacing(0)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.Zebrafish_UV_toggleButton_frame = QFrame(self.Zebrafish_UV)
        self.Zebrafish_UV_toggleButton_frame.setObjectName(u"Zebrafish_UV_toggleButton_frame")
        self.Zebrafish_UV_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Zebrafish_UV_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Zebrafish_UV_layout = QVBoxLayout(self.Zebrafish_UV_toggleButton_frame)
        self.Zebrafish_UV_layout.setSpacing(0)
        self.Zebrafish_UV_layout.setObjectName(u"Zebrafish_UV_layout")
        self.Zebrafish_UV_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_118.addWidget(self.Zebrafish_UV_toggleButton_frame)

        self.Zebrafish_UV_label_frame = QFrame(self.Zebrafish_UV)
        self.Zebrafish_UV_label_frame.setObjectName(u"Zebrafish_UV_label_frame")
        self.Zebrafish_UV_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Zebrafish_UV_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.Zebrafish_UV_label_frame)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.Zebrafish_UV_label = QLabel(self.Zebrafish_UV_label_frame)
        self.Zebrafish_UV_label.setObjectName(u"Zebrafish_UV_label")
        self.Zebrafish_UV_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_55.addWidget(self.Zebrafish_UV_label)


        self.horizontalLayout_118.addWidget(self.Zebrafish_UV_label_frame)


        self.verticalLayout_54.addWidget(self.Zebrafish_UV)

        self.Zebrafish_Blue = QFrame(self.Zebrafish_frame)
        self.Zebrafish_Blue.setObjectName(u"Zebrafish_Blue")
        self.Zebrafish_Blue.setFrameShape(QFrame.StyledPanel)
        self.Zebrafish_Blue.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.Zebrafish_Blue)
        self.horizontalLayout_121.setSpacing(0)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.Zebrafish_Blue_toggleButton_frame = QFrame(self.Zebrafish_Blue)
        self.Zebrafish_Blue_toggleButton_frame.setObjectName(u"Zebrafish_Blue_toggleButton_frame")
        self.Zebrafish_Blue_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Zebrafish_Blue_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Zebrafish_Blue_layout = QVBoxLayout(self.Zebrafish_Blue_toggleButton_frame)
        self.Zebrafish_Blue_layout.setSpacing(0)
        self.Zebrafish_Blue_layout.setObjectName(u"Zebrafish_Blue_layout")
        self.Zebrafish_Blue_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_121.addWidget(self.Zebrafish_Blue_toggleButton_frame)

        self.Zebrafish_Blue_label_frame = QFrame(self.Zebrafish_Blue)
        self.Zebrafish_Blue_label_frame.setObjectName(u"Zebrafish_Blue_label_frame")
        self.Zebrafish_Blue_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Zebrafish_Blue_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.Zebrafish_Blue_label_frame)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.Zebrafish_Blue_label = QLabel(self.Zebrafish_Blue_label_frame)
        self.Zebrafish_Blue_label.setObjectName(u"Zebrafish_Blue_label")
        self.Zebrafish_Blue_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_57.addWidget(self.Zebrafish_Blue_label)


        self.horizontalLayout_121.addWidget(self.Zebrafish_Blue_label_frame)


        self.verticalLayout_54.addWidget(self.Zebrafish_Blue)

        self.Zebrafish_Green = QFrame(self.Zebrafish_frame)
        self.Zebrafish_Green.setObjectName(u"Zebrafish_Green")
        self.Zebrafish_Green.setFrameShape(QFrame.StyledPanel)
        self.Zebrafish_Green.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_122 = QHBoxLayout(self.Zebrafish_Green)
        self.horizontalLayout_122.setSpacing(0)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.Zebrafish_Green_toggleButton_frame = QFrame(self.Zebrafish_Green)
        self.Zebrafish_Green_toggleButton_frame.setObjectName(u"Zebrafish_Green_toggleButton_frame")
        self.Zebrafish_Green_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Zebrafish_Green_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Zebrafish_Green_layout = QVBoxLayout(self.Zebrafish_Green_toggleButton_frame)
        self.Zebrafish_Green_layout.setSpacing(0)
        self.Zebrafish_Green_layout.setObjectName(u"Zebrafish_Green_layout")
        self.Zebrafish_Green_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_122.addWidget(self.Zebrafish_Green_toggleButton_frame)

        self.Zebrafish_Green_label_frame = QFrame(self.Zebrafish_Green)
        self.Zebrafish_Green_label_frame.setObjectName(u"Zebrafish_Green_label_frame")
        self.Zebrafish_Green_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Zebrafish_Green_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.Zebrafish_Green_label_frame)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.Zebrafish_Green_label = QLabel(self.Zebrafish_Green_label_frame)
        self.Zebrafish_Green_label.setObjectName(u"Zebrafish_Green_label")
        self.Zebrafish_Green_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_56.addWidget(self.Zebrafish_Green_label)


        self.horizontalLayout_122.addWidget(self.Zebrafish_Green_label_frame)


        self.verticalLayout_54.addWidget(self.Zebrafish_Green)

        self.Zebrafish_Red = QFrame(self.Zebrafish_frame)
        self.Zebrafish_Red.setObjectName(u"Zebrafish_Red")
        self.Zebrafish_Red.setFrameShape(QFrame.StyledPanel)
        self.Zebrafish_Red.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.Zebrafish_Red)
        self.horizontalLayout_123.setSpacing(0)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.Zebrafish_Red_toggleButton_frame = QFrame(self.Zebrafish_Red)
        self.Zebrafish_Red_toggleButton_frame.setObjectName(u"Zebrafish_Red_toggleButton_frame")
        self.Zebrafish_Red_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Zebrafish_Red_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Zebrafish_Red_layout = QVBoxLayout(self.Zebrafish_Red_toggleButton_frame)
        self.Zebrafish_Red_layout.setSpacing(0)
        self.Zebrafish_Red_layout.setObjectName(u"Zebrafish_Red_layout")
        self.Zebrafish_Red_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_123.addWidget(self.Zebrafish_Red_toggleButton_frame)

        self.Zebrafish_Red_label_frame = QFrame(self.Zebrafish_Red)
        self.Zebrafish_Red_label_frame.setObjectName(u"Zebrafish_Red_label_frame")
        self.Zebrafish_Red_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Zebrafish_Red_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.Zebrafish_Red_label_frame)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.Zebrafish_Red_label = QLabel(self.Zebrafish_Red_label_frame)
        self.Zebrafish_Red_label.setObjectName(u"Zebrafish_Red_label")
        self.Zebrafish_Red_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_58.addWidget(self.Zebrafish_Red_label)


        self.horizontalLayout_123.addWidget(self.Zebrafish_Red_label_frame)


        self.verticalLayout_54.addWidget(self.Zebrafish_Red)


        self.verticalLayout_53.addWidget(self.Zebrafish_frame)

        self.OpsinSpectra_stackedWidget.addWidget(self.Zebrafish_page)
        self.Chicken_page = QWidget()
        self.Chicken_page.setObjectName(u"Chicken_page")
        self.verticalLayout_69 = QVBoxLayout(self.Chicken_page)
        self.verticalLayout_69.setSpacing(5)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(5, 5, 5, 5)
        self.Chicken_frame = QFrame(self.Chicken_page)
        self.Chicken_frame.setObjectName(u"Chicken_frame")
        self.Chicken_frame.setFrameShape(QFrame.StyledPanel)
        self.Chicken_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.Chicken_frame)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.Chicken_UV = QFrame(self.Chicken_frame)
        self.Chicken_UV.setObjectName(u"Chicken_UV")
        self.Chicken_UV.setFrameShape(QFrame.StyledPanel)
        self.Chicken_UV.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.Chicken_UV)
        self.horizontalLayout_124.setSpacing(0)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.Chicken_UV_toggleButton_frame = QFrame(self.Chicken_UV)
        self.Chicken_UV_toggleButton_frame.setObjectName(u"Chicken_UV_toggleButton_frame")
        self.Chicken_UV_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Chicken_UV_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Chicken_UV_layout = QVBoxLayout(self.Chicken_UV_toggleButton_frame)
        self.Chicken_UV_layout.setSpacing(0)
        self.Chicken_UV_layout.setObjectName(u"Chicken_UV_layout")
        self.Chicken_UV_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_124.addWidget(self.Chicken_UV_toggleButton_frame)

        self.Chicken_UV_label_frame = QFrame(self.Chicken_UV)
        self.Chicken_UV_label_frame.setObjectName(u"Chicken_UV_label_frame")
        self.Chicken_UV_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Chicken_UV_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.Chicken_UV_label_frame)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.Chicken_UV_label = QLabel(self.Chicken_UV_label_frame)
        self.Chicken_UV_label.setObjectName(u"Chicken_UV_label")
        self.Chicken_UV_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.Chicken_UV_label)


        self.horizontalLayout_124.addWidget(self.Chicken_UV_label_frame)


        self.verticalLayout_60.addWidget(self.Chicken_UV)

        self.Chicken_Blue = QFrame(self.Chicken_frame)
        self.Chicken_Blue.setObjectName(u"Chicken_Blue")
        self.Chicken_Blue.setFrameShape(QFrame.StyledPanel)
        self.Chicken_Blue.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_128 = QHBoxLayout(self.Chicken_Blue)
        self.horizontalLayout_128.setSpacing(0)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.Chicken_Blue_toggleButton_frame = QFrame(self.Chicken_Blue)
        self.Chicken_Blue_toggleButton_frame.setObjectName(u"Chicken_Blue_toggleButton_frame")
        self.Chicken_Blue_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Chicken_Blue_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Chicken_Blue_layout = QVBoxLayout(self.Chicken_Blue_toggleButton_frame)
        self.Chicken_Blue_layout.setSpacing(0)
        self.Chicken_Blue_layout.setObjectName(u"Chicken_Blue_layout")
        self.Chicken_Blue_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_128.addWidget(self.Chicken_Blue_toggleButton_frame)

        self.Chicken_Blue_label_frame = QFrame(self.Chicken_Blue)
        self.Chicken_Blue_label_frame.setObjectName(u"Chicken_Blue_label_frame")
        self.Chicken_Blue_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Chicken_Blue_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.Chicken_Blue_label_frame)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.Chicken_Blue_label = QLabel(self.Chicken_Blue_label_frame)
        self.Chicken_Blue_label.setObjectName(u"Chicken_Blue_label")
        self.Chicken_Blue_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_66.addWidget(self.Chicken_Blue_label)


        self.horizontalLayout_128.addWidget(self.Chicken_Blue_label_frame)


        self.verticalLayout_60.addWidget(self.Chicken_Blue)

        self.Chicken_Green = QFrame(self.Chicken_frame)
        self.Chicken_Green.setObjectName(u"Chicken_Green")
        self.Chicken_Green.setFrameShape(QFrame.StyledPanel)
        self.Chicken_Green.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.Chicken_Green)
        self.horizontalLayout_129.setSpacing(0)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.Chicken_Green_toggleButton_frame = QFrame(self.Chicken_Green)
        self.Chicken_Green_toggleButton_frame.setObjectName(u"Chicken_Green_toggleButton_frame")
        self.Chicken_Green_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Chicken_Green_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Chicken_Green_layout = QVBoxLayout(self.Chicken_Green_toggleButton_frame)
        self.Chicken_Green_layout.setSpacing(0)
        self.Chicken_Green_layout.setObjectName(u"Chicken_Green_layout")
        self.Chicken_Green_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_129.addWidget(self.Chicken_Green_toggleButton_frame)

        self.Chicken_Green_label_frame = QFrame(self.Chicken_Green)
        self.Chicken_Green_label_frame.setObjectName(u"Chicken_Green_label_frame")
        self.Chicken_Green_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Chicken_Green_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.Chicken_Green_label_frame)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.Chicken_Green_label = QLabel(self.Chicken_Green_label_frame)
        self.Chicken_Green_label.setObjectName(u"Chicken_Green_label")
        self.Chicken_Green_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.Chicken_Green_label)


        self.horizontalLayout_129.addWidget(self.Chicken_Green_label_frame)


        self.verticalLayout_60.addWidget(self.Chicken_Green)

        self.Chicken_Red = QFrame(self.Chicken_frame)
        self.Chicken_Red.setObjectName(u"Chicken_Red")
        self.Chicken_Red.setFrameShape(QFrame.StyledPanel)
        self.Chicken_Red.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.Chicken_Red)
        self.horizontalLayout_130.setSpacing(0)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.Chicken_Red_toggleButton_frame = QFrame(self.Chicken_Red)
        self.Chicken_Red_toggleButton_frame.setObjectName(u"Chicken_Red_toggleButton_frame")
        self.Chicken_Red_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Chicken_Red_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Chicken_Red_layout = QVBoxLayout(self.Chicken_Red_toggleButton_frame)
        self.Chicken_Red_layout.setSpacing(0)
        self.Chicken_Red_layout.setObjectName(u"Chicken_Red_layout")
        self.Chicken_Red_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_130.addWidget(self.Chicken_Red_toggleButton_frame)

        self.Chicken_Red_label_frame = QFrame(self.Chicken_Red)
        self.Chicken_Red_label_frame.setObjectName(u"Chicken_Red_label_frame")
        self.Chicken_Red_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Chicken_Red_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.Chicken_Red_label_frame)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.Chicken_Red_label = QLabel(self.Chicken_Red_label_frame)
        self.Chicken_Red_label.setObjectName(u"Chicken_Red_label")
        self.Chicken_Red_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_68.addWidget(self.Chicken_Red_label)


        self.horizontalLayout_130.addWidget(self.Chicken_Red_label_frame)


        self.verticalLayout_60.addWidget(self.Chicken_Red)


        self.verticalLayout_69.addWidget(self.Chicken_frame)

        self.OpsinSpectra_stackedWidget.addWidget(self.Chicken_page)

        self.verticalLayout_49.addWidget(self.OpsinSpectra_stackedWidget)


        self.verticalLayout_47.addWidget(self.OpsinSpectra_Display_frame)

        self.OpsinSpectra_Update_pushButton_frame = QFrame(self.OpsinSpectra_frame)
        self.OpsinSpectra_Update_pushButton_frame.setObjectName(u"OpsinSpectra_Update_pushButton_frame")
        self.OpsinSpectra_Update_pushButton_frame.setMaximumSize(QSize(16777215, 40))
        self.OpsinSpectra_Update_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.OpsinSpectra_Update_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.OpsinSpectra_Update_pushButton_frame)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(5, 5, 5, 5)
        self.OpsinSpectra_Update_pushButton = QPushButton(self.OpsinSpectra_Update_pushButton_frame)
        self.OpsinSpectra_Update_pushButton.setObjectName(u"OpsinSpectra_Update_pushButton")

        self.verticalLayout_50.addWidget(self.OpsinSpectra_Update_pushButton)


        self.verticalLayout_47.addWidget(self.OpsinSpectra_Update_pushButton_frame)


        self.verticalLayout_45.addWidget(self.OpsinSpectra_frame)

        self.Spectra_stackedWidget.addWidget(self.OpsinSpectra_page)
        self.LEDSpectra_page = QWidget()
        self.LEDSpectra_page.setObjectName(u"LEDSpectra_page")
        self.verticalLayout_46 = QVBoxLayout(self.LEDSpectra_page)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.LEDSpectra_frame = QFrame(self.LEDSpectra_page)
        self.LEDSpectra_frame.setObjectName(u"LEDSpectra_frame")
        self.LEDSpectra_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDSpectra_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.LEDSpectra_frame)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 20)
        self.LEDSpectra_Title_frame = QFrame(self.LEDSpectra_frame)
        self.LEDSpectra_Title_frame.setObjectName(u"LEDSpectra_Title_frame")
        self.LEDSpectra_Title_frame.setMaximumSize(QSize(16777215, 40))
        self.LEDSpectra_Title_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDSpectra_Title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.LEDSpectra_Title_frame)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(5, 10, 5, 10)
        self.LEDSpectra_Title = QLabel(self.LEDSpectra_Title_frame)
        self.LEDSpectra_Title.setObjectName(u"LEDSpectra_Title")
        self.LEDSpectra_Title.setFont(font1)
        self.LEDSpectra_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_73.addWidget(self.LEDSpectra_Title)


        self.verticalLayout_70.addWidget(self.LEDSpectra_Title_frame)

        self.LEDSpectra_LoadData_frame = QFrame(self.LEDSpectra_frame)
        self.LEDSpectra_LoadData_frame.setObjectName(u"LEDSpectra_LoadData_frame")
        self.LEDSpectra_LoadData_frame.setMinimumSize(QSize(0, 0))
        self.LEDSpectra_LoadData_frame.setMaximumSize(QSize(16777215, 16777215))
        self.LEDSpectra_LoadData_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDSpectra_LoadData_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.LEDSpectra_LoadData_frame)
        self.verticalLayout_74.setSpacing(10)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(5, 20, 5, 10)
        self.LEDSpectra_LoadData_pushButton_frame = QFrame(self.LEDSpectra_LoadData_frame)
        self.LEDSpectra_LoadData_pushButton_frame.setObjectName(u"LEDSpectra_LoadData_pushButton_frame")
        self.LEDSpectra_LoadData_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDSpectra_LoadData_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.LEDSpectra_LoadData_pushButton_frame)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.LEDSpectra_LoadData_pushButton = QPushButton(self.LEDSpectra_LoadData_pushButton_frame)
        self.LEDSpectra_LoadData_pushButton.setObjectName(u"LEDSpectra_LoadData_pushButton")

        self.verticalLayout_72.addWidget(self.LEDSpectra_LoadData_pushButton)

        self.LEDSpectra_LoadData_label = QLabel(self.LEDSpectra_LoadData_pushButton_frame)
        self.LEDSpectra_LoadData_label.setObjectName(u"LEDSpectra_LoadData_label")
        self.LEDSpectra_LoadData_label.setMinimumSize(QSize(0, 20))
        self.LEDSpectra_LoadData_label.setWordWrap(True)

        self.verticalLayout_72.addWidget(self.LEDSpectra_LoadData_label)


        self.verticalLayout_74.addWidget(self.LEDSpectra_LoadData_pushButton_frame)

        self.LEDSpectra_Load_label = QLabel(self.LEDSpectra_LoadData_frame)
        self.LEDSpectra_Load_label.setObjectName(u"LEDSpectra_Load_label")
        self.LEDSpectra_Load_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_74.addWidget(self.LEDSpectra_Load_label)

        self.LEDSpectra_Load_comboBox_frame = QFrame(self.LEDSpectra_LoadData_frame)
        self.LEDSpectra_Load_comboBox_frame.setObjectName(u"LEDSpectra_Load_comboBox_frame")
        self.LEDSpectra_Load_comboBox_frame.setMaximumSize(QSize(16777215, 25))
        self.LEDSpectra_Load_comboBox_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDSpectra_Load_comboBox_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.LEDSpectra_Load_comboBox_frame)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(5, 0, 5, 0)
        self.LEDSpectra_Load_comboBox = QComboBox(self.LEDSpectra_Load_comboBox_frame)
        self.LEDSpectra_Load_comboBox.addItem("")
        self.LEDSpectra_Load_comboBox.addItem("")
        self.LEDSpectra_Load_comboBox.setObjectName(u"LEDSpectra_Load_comboBox")
        self.LEDSpectra_Load_comboBox.setFont(font1)
        self.LEDSpectra_Load_comboBox.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_71.addWidget(self.LEDSpectra_Load_comboBox)


        self.verticalLayout_74.addWidget(self.LEDSpectra_Load_comboBox_frame)


        self.verticalLayout_70.addWidget(self.LEDSpectra_LoadData_frame)

        self.line_7 = QFrame(self.LEDSpectra_frame)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_70.addWidget(self.line_7)

        self.LEDSpectra_Display_frame = QFrame(self.LEDSpectra_frame)
        self.LEDSpectra_Display_frame.setObjectName(u"LEDSpectra_Display_frame")
        self.LEDSpectra_Display_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDSpectra_Display_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.LEDSpectra_Display_frame)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(5, 10, 5, 10)
        self.LEDSpectra_Display_pushButton_frame = QFrame(self.LEDSpectra_Display_frame)
        self.LEDSpectra_Display_pushButton_frame.setObjectName(u"LEDSpectra_Display_pushButton_frame")
        self.LEDSpectra_Display_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.LEDSpectra_Display_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.LEDSpectra_Display_pushButton_frame)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(5, 5, 5, 5)
        self.LEDSpectra_Display_pushButton = QPushButton(self.LEDSpectra_Display_pushButton_frame)
        self.LEDSpectra_Display_pushButton.setObjectName(u"LEDSpectra_Display_pushButton")

        self.verticalLayout_87.addWidget(self.LEDSpectra_Display_pushButton)


        self.verticalLayout_75.addWidget(self.LEDSpectra_Display_pushButton_frame)

        self.LEDSpectra_Display_stackedWidget = QStackedWidget(self.LEDSpectra_Display_frame)
        self.LEDSpectra_Display_stackedWidget.setObjectName(u"LEDSpectra_Display_stackedWidget")
        self.LEDSpectra_Blank_page = QWidget()
        self.LEDSpectra_Blank_page.setObjectName(u"LEDSpectra_Blank_page")
        self.LEDSpectra_Display_stackedWidget.addWidget(self.LEDSpectra_Blank_page)
        self.Tetrachromatic_page = QWidget()
        self.Tetrachromatic_page.setObjectName(u"Tetrachromatic_page")
        self.verticalLayout_81 = QVBoxLayout(self.Tetrachromatic_page)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.Tetrachromatic_frame = QFrame(self.Tetrachromatic_page)
        self.Tetrachromatic_frame.setObjectName(u"Tetrachromatic_frame")
        self.Tetrachromatic_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.Tetrachromatic_frame)
        self.verticalLayout_76.setSpacing(5)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(5, 5, 5, 5)
        self.Tetrachromatic_UV = QFrame(self.Tetrachromatic_frame)
        self.Tetrachromatic_UV.setObjectName(u"Tetrachromatic_UV")
        self.Tetrachromatic_UV.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_UV.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_131 = QHBoxLayout(self.Tetrachromatic_UV)
        self.horizontalLayout_131.setSpacing(5)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.Tetrachromatic_UV_toggleButton_frame = QFrame(self.Tetrachromatic_UV)
        self.Tetrachromatic_UV_toggleButton_frame.setObjectName(u"Tetrachromatic_UV_toggleButton_frame")
        self.Tetrachromatic_UV_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_UV_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Tetrachromatic_UV_layout = QVBoxLayout(self.Tetrachromatic_UV_toggleButton_frame)
        self.Tetrachromatic_UV_layout.setSpacing(0)
        self.Tetrachromatic_UV_layout.setObjectName(u"Tetrachromatic_UV_layout")
        self.Tetrachromatic_UV_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_131.addWidget(self.Tetrachromatic_UV_toggleButton_frame)

        self.Tetrachromatic_UV_Slider_frame = QFrame(self.Tetrachromatic_UV)
        self.Tetrachromatic_UV_Slider_frame.setObjectName(u"Tetrachromatic_UV_Slider_frame")
        self.Tetrachromatic_UV_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_UV_Slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.Tetrachromatic_UV_Slider_frame)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.Tetrachromatic_UV_Slider = QSlider(self.Tetrachromatic_UV_Slider_frame)
        self.Tetrachromatic_UV_Slider.setObjectName(u"Tetrachromatic_UV_Slider")
        self.Tetrachromatic_UV_Slider.setMaximum(100)
        self.Tetrachromatic_UV_Slider.setValue(100)
        self.Tetrachromatic_UV_Slider.setOrientation(Qt.Horizontal)
        self.Tetrachromatic_UV_Slider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_85.addWidget(self.Tetrachromatic_UV_Slider)


        self.horizontalLayout_131.addWidget(self.Tetrachromatic_UV_Slider_frame)

        self.Tetrachromatic_UV_label_frame = QFrame(self.Tetrachromatic_UV)
        self.Tetrachromatic_UV_label_frame.setObjectName(u"Tetrachromatic_UV_label_frame")
        self.Tetrachromatic_UV_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_UV_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.Tetrachromatic_UV_label_frame)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.Tetrachromatic_UV_label = QLabel(self.Tetrachromatic_UV_label_frame)
        self.Tetrachromatic_UV_label.setObjectName(u"Tetrachromatic_UV_label")
        self.Tetrachromatic_UV_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_77.addWidget(self.Tetrachromatic_UV_label)


        self.horizontalLayout_131.addWidget(self.Tetrachromatic_UV_label_frame)


        self.verticalLayout_76.addWidget(self.Tetrachromatic_UV)

        self.Tetrachromatic_Blue = QFrame(self.Tetrachromatic_frame)
        self.Tetrachromatic_Blue.setObjectName(u"Tetrachromatic_Blue")
        self.Tetrachromatic_Blue.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_Blue.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.Tetrachromatic_Blue)
        self.horizontalLayout_132.setSpacing(5)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.Tetrachromatic_Blue_toggleButton_frame = QFrame(self.Tetrachromatic_Blue)
        self.Tetrachromatic_Blue_toggleButton_frame.setObjectName(u"Tetrachromatic_Blue_toggleButton_frame")
        self.Tetrachromatic_Blue_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_Blue_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Tetrachromatic_Blue_layout = QVBoxLayout(self.Tetrachromatic_Blue_toggleButton_frame)
        self.Tetrachromatic_Blue_layout.setSpacing(0)
        self.Tetrachromatic_Blue_layout.setObjectName(u"Tetrachromatic_Blue_layout")
        self.Tetrachromatic_Blue_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_132.addWidget(self.Tetrachromatic_Blue_toggleButton_frame)

        self.Tetrachromatic_Blue_Slider_frame = QFrame(self.Tetrachromatic_Blue)
        self.Tetrachromatic_Blue_Slider_frame.setObjectName(u"Tetrachromatic_Blue_Slider_frame")
        self.Tetrachromatic_Blue_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_Blue_Slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.Tetrachromatic_Blue_Slider_frame)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.Tetrachromatic_Blue_Slider = QSlider(self.Tetrachromatic_Blue_Slider_frame)
        self.Tetrachromatic_Blue_Slider.setObjectName(u"Tetrachromatic_Blue_Slider")
        self.Tetrachromatic_Blue_Slider.setMaximum(100)
        self.Tetrachromatic_Blue_Slider.setValue(100)
        self.Tetrachromatic_Blue_Slider.setOrientation(Qt.Horizontal)
        self.Tetrachromatic_Blue_Slider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_82.addWidget(self.Tetrachromatic_Blue_Slider)


        self.horizontalLayout_132.addWidget(self.Tetrachromatic_Blue_Slider_frame)

        self.Tetrachromatic_Blue_label_frame = QFrame(self.Tetrachromatic_Blue)
        self.Tetrachromatic_Blue_label_frame.setObjectName(u"Tetrachromatic_Blue_label_frame")
        self.Tetrachromatic_Blue_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_Blue_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.Tetrachromatic_Blue_label_frame)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.Tetrachromatic_Blue_label = QLabel(self.Tetrachromatic_Blue_label_frame)
        self.Tetrachromatic_Blue_label.setObjectName(u"Tetrachromatic_Blue_label")
        self.Tetrachromatic_Blue_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_78.addWidget(self.Tetrachromatic_Blue_label)


        self.horizontalLayout_132.addWidget(self.Tetrachromatic_Blue_label_frame)


        self.verticalLayout_76.addWidget(self.Tetrachromatic_Blue)

        self.Tetrachromatic_Green = QFrame(self.Tetrachromatic_frame)
        self.Tetrachromatic_Green.setObjectName(u"Tetrachromatic_Green")
        self.Tetrachromatic_Green.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_Green.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_133 = QHBoxLayout(self.Tetrachromatic_Green)
        self.horizontalLayout_133.setSpacing(5)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.Tetrachromatic_Green_toggleButton_frame = QFrame(self.Tetrachromatic_Green)
        self.Tetrachromatic_Green_toggleButton_frame.setObjectName(u"Tetrachromatic_Green_toggleButton_frame")
        self.Tetrachromatic_Green_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_Green_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Tetrachromatic_Green_layout = QVBoxLayout(self.Tetrachromatic_Green_toggleButton_frame)
        self.Tetrachromatic_Green_layout.setSpacing(0)
        self.Tetrachromatic_Green_layout.setObjectName(u"Tetrachromatic_Green_layout")
        self.Tetrachromatic_Green_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_133.addWidget(self.Tetrachromatic_Green_toggleButton_frame)

        self.Tetrachromatic_Green_Slider_frame = QFrame(self.Tetrachromatic_Green)
        self.Tetrachromatic_Green_Slider_frame.setObjectName(u"Tetrachromatic_Green_Slider_frame")
        self.Tetrachromatic_Green_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_Green_Slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.Tetrachromatic_Green_Slider_frame)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.Tetrachromatic_Green_Slider = QSlider(self.Tetrachromatic_Green_Slider_frame)
        self.Tetrachromatic_Green_Slider.setObjectName(u"Tetrachromatic_Green_Slider")
        self.Tetrachromatic_Green_Slider.setMaximum(100)
        self.Tetrachromatic_Green_Slider.setValue(100)
        self.Tetrachromatic_Green_Slider.setOrientation(Qt.Horizontal)
        self.Tetrachromatic_Green_Slider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_83.addWidget(self.Tetrachromatic_Green_Slider)


        self.horizontalLayout_133.addWidget(self.Tetrachromatic_Green_Slider_frame)

        self.Tetrachromatic_Green_label_frame = QFrame(self.Tetrachromatic_Green)
        self.Tetrachromatic_Green_label_frame.setObjectName(u"Tetrachromatic_Green_label_frame")
        self.Tetrachromatic_Green_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_Green_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.Tetrachromatic_Green_label_frame)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.Tetrachromatic_Green_label = QLabel(self.Tetrachromatic_Green_label_frame)
        self.Tetrachromatic_Green_label.setObjectName(u"Tetrachromatic_Green_label")
        self.Tetrachromatic_Green_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_79.addWidget(self.Tetrachromatic_Green_label)


        self.horizontalLayout_133.addWidget(self.Tetrachromatic_Green_label_frame)


        self.verticalLayout_76.addWidget(self.Tetrachromatic_Green)

        self.Tetrachromatic_Red = QFrame(self.Tetrachromatic_frame)
        self.Tetrachromatic_Red.setObjectName(u"Tetrachromatic_Red")
        self.Tetrachromatic_Red.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_Red.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_134 = QHBoxLayout(self.Tetrachromatic_Red)
        self.horizontalLayout_134.setSpacing(5)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.Tetrachromatic_Red_toggleButton_frame = QFrame(self.Tetrachromatic_Red)
        self.Tetrachromatic_Red_toggleButton_frame.setObjectName(u"Tetrachromatic_Red_toggleButton_frame")
        self.Tetrachromatic_Red_toggleButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_Red_toggleButton_frame.setFrameShadow(QFrame.Raised)
        self.Tetrachromatic_Red_layout = QVBoxLayout(self.Tetrachromatic_Red_toggleButton_frame)
        self.Tetrachromatic_Red_layout.setSpacing(0)
        self.Tetrachromatic_Red_layout.setObjectName(u"Tetrachromatic_Red_layout")
        self.Tetrachromatic_Red_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_134.addWidget(self.Tetrachromatic_Red_toggleButton_frame)

        self.Tetrachromatic_Red_Slider_frame = QFrame(self.Tetrachromatic_Red)
        self.Tetrachromatic_Red_Slider_frame.setObjectName(u"Tetrachromatic_Red_Slider_frame")
        self.Tetrachromatic_Red_Slider_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_Red_Slider_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.Tetrachromatic_Red_Slider_frame)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.Tetrachromatic_Red_Slider = QSlider(self.Tetrachromatic_Red_Slider_frame)
        self.Tetrachromatic_Red_Slider.setObjectName(u"Tetrachromatic_Red_Slider")
        self.Tetrachromatic_Red_Slider.setMaximum(100)
        self.Tetrachromatic_Red_Slider.setValue(100)
        self.Tetrachromatic_Red_Slider.setOrientation(Qt.Horizontal)
        self.Tetrachromatic_Red_Slider.setTickPosition(QSlider.TicksBelow)

        self.verticalLayout_84.addWidget(self.Tetrachromatic_Red_Slider)


        self.horizontalLayout_134.addWidget(self.Tetrachromatic_Red_Slider_frame)

        self.Tetrachromatic_Red_label_frame = QFrame(self.Tetrachromatic_Red)
        self.Tetrachromatic_Red_label_frame.setObjectName(u"Tetrachromatic_Red_label_frame")
        self.Tetrachromatic_Red_label_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_Red_label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.Tetrachromatic_Red_label_frame)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.Tetrachromatic_Red_label = QLabel(self.Tetrachromatic_Red_label_frame)
        self.Tetrachromatic_Red_label.setObjectName(u"Tetrachromatic_Red_label")
        self.Tetrachromatic_Red_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_80.addWidget(self.Tetrachromatic_Red_label)


        self.horizontalLayout_134.addWidget(self.Tetrachromatic_Red_label_frame)


        self.verticalLayout_76.addWidget(self.Tetrachromatic_Red)

        self.Tetrachromatic_Update_pushButton_frame = QFrame(self.Tetrachromatic_frame)
        self.Tetrachromatic_Update_pushButton_frame.setObjectName(u"Tetrachromatic_Update_pushButton_frame")
        self.Tetrachromatic_Update_pushButton_frame.setMinimumSize(QSize(0, 40))
        self.Tetrachromatic_Update_pushButton_frame.setMaximumSize(QSize(16777215, 40))
        self.Tetrachromatic_Update_pushButton_frame.setFrameShape(QFrame.StyledPanel)
        self.Tetrachromatic_Update_pushButton_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.Tetrachromatic_Update_pushButton_frame)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(5, 5, 5, 5)
        self.Tetrachromatic_Update_pushButton = QPushButton(self.Tetrachromatic_Update_pushButton_frame)
        self.Tetrachromatic_Update_pushButton.setObjectName(u"Tetrachromatic_Update_pushButton")

        self.verticalLayout_86.addWidget(self.Tetrachromatic_Update_pushButton)


        self.verticalLayout_76.addWidget(self.Tetrachromatic_Update_pushButton_frame)


        self.verticalLayout_81.addWidget(self.Tetrachromatic_frame)

        self.LEDSpectra_Display_stackedWidget.addWidget(self.Tetrachromatic_page)

        self.verticalLayout_75.addWidget(self.LEDSpectra_Display_stackedWidget)


        self.verticalLayout_70.addWidget(self.LEDSpectra_Display_frame)


        self.verticalLayout_46.addWidget(self.LEDSpectra_frame)

        self.Spectra_stackedWidget.addWidget(self.LEDSpectra_page)

        self.verticalLayout_44.addWidget(self.Spectra_stackedWidget)


        self.horizontalLayout_18.addWidget(self.Spectra_CenterMenu_container)

        self.Spectra_RightMenu_container = QFrame(self.Spectra_Page)
        self.Spectra_RightMenu_container.setObjectName(u"Spectra_RightMenu_container")
        self.Spectra_RightMenu_container.setMaximumSize(QSize(40, 16777215))
        self.Spectra_RightMenu_container.setFrameShape(QFrame.StyledPanel)
        self.Spectra_RightMenu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.Spectra_RightMenu_container)
        self.verticalLayout_41.setSpacing(50)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 5, 0)
        self.Spectra_RightMenu_container_frame_top = QFrame(self.Spectra_RightMenu_container)
        self.Spectra_RightMenu_container_frame_top.setObjectName(u"Spectra_RightMenu_container_frame_top")
        self.Spectra_RightMenu_container_frame_top.setFrameShape(QFrame.StyledPanel)
        self.Spectra_RightMenu_container_frame_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.Spectra_RightMenu_container_frame_top)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 20, 0, 0)
        self.Spectra_RightMenu_container_pushButton = QPushButton(self.Spectra_RightMenu_container_frame_top)
        self.Spectra_RightMenu_container_pushButton.setObjectName(u"Spectra_RightMenu_container_pushButton")
        icon14 = QIcon()
        icon14.addFile(u":/resources/resources/MenuRight.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Spectra_RightMenu_container_pushButton.setIcon(icon14)
        self.Spectra_RightMenu_container_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_42.addWidget(self.Spectra_RightMenu_container_pushButton)


        self.verticalLayout_41.addWidget(self.Spectra_RightMenu_container_frame_top, 0, Qt.AlignTop)

        self.Spectra_RightMenu_container_frame_middle = QFrame(self.Spectra_RightMenu_container)
        self.Spectra_RightMenu_container_frame_middle.setObjectName(u"Spectra_RightMenu_container_frame_middle")
        self.Spectra_RightMenu_container_frame_middle.setFrameShape(QFrame.StyledPanel)
        self.Spectra_RightMenu_container_frame_middle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.Spectra_RightMenu_container_frame_middle)
        self.verticalLayout_43.setSpacing(50)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.OpsinSpectra_tab_pushButton = QPushButton(self.Spectra_RightMenu_container_frame_middle)
        self.OpsinSpectra_tab_pushButton.setObjectName(u"OpsinSpectra_tab_pushButton")
        icon15 = QIcon()
        icon15.addFile(u":/resources/resources/Opsin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.OpsinSpectra_tab_pushButton.setIcon(icon15)
        self.OpsinSpectra_tab_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_43.addWidget(self.OpsinSpectra_tab_pushButton)

        self.LEDSpectra_tab_pushButton = QPushButton(self.Spectra_RightMenu_container_frame_middle)
        self.LEDSpectra_tab_pushButton.setObjectName(u"LEDSpectra_tab_pushButton")
        icon16 = QIcon()
        icon16.addFile(u":/resources/resources/LED.png", QSize(), QIcon.Normal, QIcon.Off)
        self.LEDSpectra_tab_pushButton.setIcon(icon16)
        self.LEDSpectra_tab_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_43.addWidget(self.LEDSpectra_tab_pushButton)

        self.pushButton_4 = QPushButton(self.Spectra_RightMenu_container_frame_middle)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setIcon(icon8)
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.verticalLayout_43.addWidget(self.pushButton_4)


        self.verticalLayout_41.addWidget(self.Spectra_RightMenu_container_frame_middle)

        self.Spectra_RightMenu_container_frame_bottom = QFrame(self.Spectra_RightMenu_container)
        self.Spectra_RightMenu_container_frame_bottom.setObjectName(u"Spectra_RightMenu_container_frame_bottom")
        self.Spectra_RightMenu_container_frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.Spectra_RightMenu_container_frame_bottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_41.addWidget(self.Spectra_RightMenu_container_frame_bottom)


        self.horizontalLayout_18.addWidget(self.Spectra_RightMenu_container)

        self.Main_stackedWidget.addWidget(self.Spectra_Page)

        self.horizontalLayout_12.addWidget(self.Main_stackedWidget)


        self.horizontalLayout_10.addWidget(self.MainContent_Frame)


        self.verticalLayout.addWidget(self.CenterMainFrame)

        self.BottomMainFrame = QFrame(self.centralwidget)
        self.BottomMainFrame.setObjectName(u"BottomMainFrame")
        self.BottomMainFrame.setMinimumSize(QSize(0, 30))
        self.BottomMainFrame.setMaximumSize(QSize(16777215, 30))
        self.BottomMainFrame.setFrameShape(QFrame.StyledPanel)
        self.BottomMainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.BottomMainFrame)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Footer_Frame = QFrame(self.BottomMainFrame)
        self.Footer_Frame.setObjectName(u"Footer_Frame")
        self.Footer_Frame.setMinimumSize(QSize(0, 30))
        self.Footer_Frame.setMaximumSize(QSize(16777215, 50))
        self.Footer_Frame.setFrameShape(QFrame.StyledPanel)
        self.Footer_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Footer_Frame)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.License_Frame = QFrame(self.Footer_Frame)
        self.License_Frame.setObjectName(u"License_Frame")
        self.License_Frame.setFrameShape(QFrame.StyledPanel)
        self.License_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.License_Frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.License_Label = QLabel(self.License_Frame)
        self.License_Label.setObjectName(u"License_Label")

        self.horizontalLayout_8.addWidget(self.License_Label)


        self.horizontalLayout_6.addWidget(self.License_Frame)

        self.Logo_Frame = QFrame(self.Footer_Frame)
        self.Logo_Frame.setObjectName(u"Logo_Frame")
        self.Logo_Frame.setFrameShape(QFrame.StyledPanel)
        self.Logo_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.Logo_Frame)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.BadenLab_Logo = QLabel(self.Logo_Frame)
        self.BadenLab_Logo.setObjectName(u"BadenLab_Logo")
        self.BadenLab_Logo.setMinimumSize(QSize(80, 30))
        self.BadenLab_Logo.setMaximumSize(QSize(80, 30))
        self.BadenLab_Logo.setPixmap(QPixmap(u":/resources/resources/Baden-Logo2.png"))
        self.BadenLab_Logo.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.BadenLab_Logo)


        self.horizontalLayout_6.addWidget(self.Logo_Frame, 0, Qt.AlignRight)

        self.OSN_Logo = QLabel(self.Footer_Frame)
        self.OSN_Logo.setObjectName(u"OSN_Logo")
        self.OSN_Logo.setMinimumSize(QSize(60, 30))
        self.OSN_Logo.setMaximumSize(QSize(60, 30))
        self.OSN_Logo.setPixmap(QPixmap(u":/resources/resources/SpikyLogo.png"))
        self.OSN_Logo.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.OSN_Logo)

        self.SizeGrip_Frame = QFrame(self.Footer_Frame)
        self.SizeGrip_Frame.setObjectName(u"SizeGrip_Frame")
        self.SizeGrip_Frame.setMinimumSize(QSize(20, 20))
        self.SizeGrip_Frame.setMaximumSize(QSize(20, 20))
        self.SizeGrip_Frame.setFrameShape(QFrame.StyledPanel)
        self.SizeGrip_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.SizeGrip_Frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.SizeGrip_Label = QLabel(self.SizeGrip_Frame)
        self.SizeGrip_Label.setObjectName(u"SizeGrip_Label")
        self.SizeGrip_Label.setPixmap(QPixmap(u":/resources/resources/SizeGrip.png"))
        self.SizeGrip_Label.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.SizeGrip_Label)


        self.horizontalLayout_6.addWidget(self.SizeGrip_Frame)


        self.horizontalLayout_5.addWidget(self.Footer_Frame)


        self.verticalLayout.addWidget(self.BottomMainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.Main_stackedWidget.setCurrentIndex(1)
        self.LED_Zap_Display_stackedWidget.setCurrentIndex(0)
        self.LEDZap_stackedWidget.setCurrentIndex(0)
        self.Chrolis_Display_stackedWidget.setCurrentIndex(0)
        self.Spectra_stackedWidget.setCurrentIndex(0)
        self.OpsinSpectra_stackedWidget.setCurrentIndex(2)
        self.LEDSpectra_Display_stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.AppName_pushButton.setText(QCoreApplication.translate("MainWindow", u"LED Zappelin' v2", None))
        self.Reduce_pushButton.setText("")
        self.Expand_pushButton.setText("")
        self.Exit_pushButton.setText("")
        self.DropMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide Menus", None))
        self.LEDZappelin_pushButton.setText(QCoreApplication.translate("MainWindow", u"LED Zappelin'", None))
        self.Chrolis_pushButton.setText(QCoreApplication.translate("MainWindow", u"Chrolis", None))
        self.Stimulus_pushButton.setText(QCoreApplication.translate("MainWindow", u"Stimuli", None))
        self.Spectra_pushButton.setText(QCoreApplication.translate("MainWindow", u"Spectra", None))
        self.Settings_pushButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.About_pushButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.Help_pushButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.GitHub_pushButton.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.HideSubFrame_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide Sub-Menus", None))
        self.Home_Logo.setText("")
        self.Home_Title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#93a1a1;\">LED Zappelin' </span><span style=\" font-size:16pt; color:#93a1a1;\">v2</span></p><p align=\"center\"><span style=\" font-size:16pt;\">An open source and versatile LED controller for arbitrary spectrum </span></p><p align=\"center\"><span style=\" font-size:16pt;\">visual stimulation and optogenetics during 2-photon imaging</span></p><p align=\"right\"><span style=\" font-size:8pt; font-weight:700;\">Conceived and developed by M.J.Y. Zimmermann</span></p></body></html>", None))
        self.Home_Main_Text.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">LED Zappelin was orignally designed to overcome the challenge of applying  a spectrally arbitrary light stimulation to a sample under a two-photon microscope. Challenge consisting of avoiding any crosstalk between light stimulation and fluorescence detection.</span></p>\n"
"<p align=\"justify\" style=\" marg"
                        "in-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">This simple and low-cost electronic solution based on an ESP32 microcontroller and a TLC5947 LED driver relies on rapidly time-interleaving stimulation and detection epochs during scans.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">This second version of the project offers a more intuitive and interactive interaction throught a dedicated GUI and now can be coupled to the Thorlbas Chrolis High-Power LED sources.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"><br />The original project was published in July 2020 in </span><span style=\" font-size:12pt; font-weight:700; color:#268bd2;\">Hardware"
                        "X</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#268bd2;\">This project is licensed under the </span><span style=\" font-size:12pt; font-weight:700; color:#268bd2;\">GNU General Public License v3.0</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#268bd2;\">The hardware is licensed under the </span><span style=\" font-size:12pt; font-weight:700; color:#268bd2;\">CERN OHL v1.2</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700; color:#268bd2;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#268bd2;\">https://github.com/OpenSourceNeuro/LED-Zappelin_V2</span></p></body></html>", None))
        self.Home_Main_Illustration_Title.setText(QCoreApplication.translate("MainWindow", u"Studying the Dark Side of the Retina", None))
        self.Home_Main_Illustration_Image.setText("")
        self.LEDZap_SelectPortLabel.setText(QCoreApplication.translate("MainWindow", u"Select Port :", None))
        self.LEDZap_SelectPortComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a COM port:", None))

        self.LEDZap_ConnectButton.setText(QCoreApplication.translate("MainWindow", u"Connect LED Zappelin'", None))
        self.LEDZap_ProxyLED_label.setText(QCoreApplication.translate("MainWindow", u"Proxy LED brightness", None))
        self.LEDZap_ProxyLED_value.setText("")
        self.LED_Zap_Display1_pushButton.setText(QCoreApplication.translate("MainWindow", u"Multiple Graph display", None))
        self.LED_Zap_Display2_pushButton.setText(QCoreApplication.translate("MainWindow", u"Single Graph display", None))
        self.LED_Zap_Serial_label.setText("")
        self.LEDZap_Load_pushButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.LEDZap_Stimulus_Label.setText(QCoreApplication.translate("MainWindow", u"Load a stimulus", None))
        self.LEDZap_Display_pushButton.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.LEDZap_Test_pushButton.setText(QCoreApplication.translate("MainWindow", u"LED test", None))
        self.LEDZap_Start_pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.LEDZap_Stop_pushButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.LEDZap_NumbeofLoop_Label.setText(QCoreApplication.translate("MainWindow", u"Number of Loop :", None))
        self.LEDZap_NumbeofLoop.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.All_LED_label.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.All_LED_value.setText("")
        self.Preselect_Load_frame_pushButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.Preselect_Apply_pushButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.Preselect_Label.setText(QCoreApplication.translate("MainWindow", u"Load LED intensity settings", None))
        self.LED01_Display_lineEdit.setText(QCoreApplication.translate("MainWindow", u"565", None))
        self.LED01_Display_label.setText(QCoreApplication.translate("MainWindow", u" nm ", None))
        self.LED01_Value.setText("")
        self.LED02_Display_lineEdit.setText(QCoreApplication.translate("MainWindow", u"482", None))
        self.LED02_Display_label.setText(QCoreApplication.translate("MainWindow", u" nm ", None))
        self.LED02_Value.setText("")
        self.LED03_Display_lineEdit.setText(QCoreApplication.translate("MainWindow", u"411", None))
        self.LED03_Display_label.setText(QCoreApplication.translate("MainWindow", u" nm ", None))
        self.LED03_Value.setText("")
        self.LED04_Display_lineEdit.setText(QCoreApplication.translate("MainWindow", u"361", None))
        self.LED04_Display_label.setText(QCoreApplication.translate("MainWindow", u" nm ", None))
        self.LED04_Value.setText("")
        self.LED05_Display_label.setText(QCoreApplication.translate("MainWindow", u" nm ", None))
        self.LED05_Value.setText("")
        self.LED06_Display_label.setText(QCoreApplication.translate("MainWindow", u" nm ", None))
        self.LED06_Value.setText("")
        self.LED07_Display_label.setText(QCoreApplication.translate("MainWindow", u" nm ", None))
        self.LED07_Value.setText("")
        self.LED08_Display_label.setText(QCoreApplication.translate("MainWindow", u" nm ", None))
        self.LED08_Value.setText("")
        self.LED09_Display_label.setText(QCoreApplication.translate("MainWindow", u" nm ", None))
        self.LED09_Value.setText("")
        self.LED10_Display_label.setText(QCoreApplication.translate("MainWindow", u" nm ", None))
        self.LED10_Value.setText("")
        self.LED11_Display_label.setText(QCoreApplication.translate("MainWindow", u" nm ", None))
        self.LED11_Value.setText("")
        self.LED12_Display_label.setText(QCoreApplication.translate("MainWindow", u" nm ", None))
        self.LED12_Value.setText("")
        self.LED13_Display_label.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.LED13_Value.setText("")
        self.LED14_Display_label.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.LED14_Value.setText("")
        self.LED15_Display_label.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.LED15_Value.setText("")
        self.LED16_Display_label.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.LED16_Value.setText("")
        self.LED17_Display_label.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.LED17_Value.setText("")
        self.LED18_Display_label.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.LED18_Value.setText("")
        self.LED19_Display_label.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.LED19_Value.setText("")
        self.LED20_Display_label.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.LED20_Value.setText("")
        self.LED21_Display_label.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.LED21_Value.setText("")
        self.LED22_Display_label.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.LED22_Value.setText("")
        self.LED23_Display_label.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.LED23_Value.setText("")
        self.LED24_Display_label.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.LED24_Value.setText("")
        self.LEDZap_Switch_pushButton1.setText(QCoreApplication.translate("MainWindow", u"1- 12", None))
        self.LEDZap_Switch_pushButton2.setText(QCoreApplication.translate("MainWindow", u"13 - 24", None))
        self.Chrolis_SelectPortLabel.setText(QCoreApplication.translate("MainWindow", u"Select Port :", None))
        self.Chrolis_SelectPortComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a COM port:", None))

        self.Chrolis_ConnectButton.setText(QCoreApplication.translate("MainWindow", u"Connect Chrolis", None))
        self.Chrolis_ProxyLED_label.setText(QCoreApplication.translate("MainWindow", u"Proxy LED brightness", None))
        self.Chrolis_ProxyLED_value.setText("")
        self.Chrolis_Display1_pushButton.setText(QCoreApplication.translate("MainWindow", u"Multiple Graph display", None))
        self.Chrolis_Display2_pushButton.setText(QCoreApplication.translate("MainWindow", u"Single Graph display", None))
        self.Chrolis_Serial_label.setText("")
        self.Chrolis_Load_pushButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.Chrolis_Stimulus_Label.setText(QCoreApplication.translate("MainWindow", u"Load a stimulus", None))
        self.Chrolis_Display_pushButton.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.Chrolis_Test_pushButton.setText(QCoreApplication.translate("MainWindow", u"LED test", None))
        self.Chrolis_Start_pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Chrolis_Stop_pushButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.Chrolis_NumbeofLoop_Label.setText(QCoreApplication.translate("MainWindow", u"Number of Loop :", None))
        self.Chrolis_NumbeofLoop.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ChrolisAll_LED_label.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.ChrolisAll_LED_value.setText("")
        self.Chrolis_Preselect_Load_frame_pushButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.Chrolis_Preselect_Apply_pushButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.Chrolis_Preselect_Label.setText(QCoreApplication.translate("MainWindow", u"Load LED intensity settings", None))
        self.Chrolis01_Display_label.setText(QCoreApplication.translate("MainWindow", u"365 nm", None))
        self.Chrolis01_Value.setText("")
        self.Chrolis02_Display_label.setText(QCoreApplication.translate("MainWindow", u"366 nm", None))
        self.Chrolis02_Value.setText("")
        self.Chrolis03_Display_label.setText(QCoreApplication.translate("MainWindow", u"385 nm", None))
        self.Chrolis03_Value.setText("")
        self.Chrolis04_Display_label.setText(QCoreApplication.translate("MainWindow", u"405 nm", None))
        self.Chrolis04_Value.setText("")
        self.Chrolis05_Display_label.setText(QCoreApplication.translate("MainWindow", u"420 nm", None))
        self.Chrolis05_Value.setText("")
        self.Chrolis06_Display_label.setText(QCoreApplication.translate("MainWindow", u"475 nm", None))
        self.Chrolis06_Value.setText("")
        self.Chrolis07_Display_label.setText(QCoreApplication.translate("MainWindow", u"490 nm", None))
        self.Chrolis07_Value.setText("")
        self.Chrolis08_Display_label.setText(QCoreApplication.translate("MainWindow", u"525 nm", None))
        self.Chrolis08_Value.setText("")
        self.Chrolis09_Display_label.setText(QCoreApplication.translate("MainWindow", u"543 nm", None))
        self.Chrolis09_Value.setText("")
        self.Chrolis10_Display_label.setText(QCoreApplication.translate("MainWindow", u"570 nm", None))
        self.Chrolis10_Value.setText("")
        self.Chrolis11_Display_label.setText(QCoreApplication.translate("MainWindow", u"610 nm", None))
        self.Chrolis11_Value.setText("")
        self.Chrolis12_Display_label.setText(QCoreApplication.translate("MainWindow", u"625 nm", None))
        self.Chrolis12_Value.setText("")
        self.Spectra_CenterMenu_Hide_pushButton.setText(QCoreApplication.translate("MainWindow", u"   Hide Tab", None))
        self.OpsinSpectra_Title.setText(QCoreApplication.translate("MainWindow", u"Opsin Absorption Spectra", None))
        self.OpsinSpectra_Load_label.setText(QCoreApplication.translate("MainWindow", u"Select an animal model", None))
        self.OpsinSpectra_Load_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select", None))
        self.OpsinSpectra_Load_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Human", None))
        self.OpsinSpectra_Load_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Zebrafish", None))
        self.OpsinSpectra_Load_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Chicken", None))
        self.OpsinSpectra_Load_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Frog", None))
        self.OpsinSpectra_Load_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Shark, because why not", None))

        self.OpsinSpectra_DisplayOpsin_pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate Opsin(s)", None))
        self.Human_Blue_label.setText(QCoreApplication.translate("MainWindow", u"420nm", None))
        self.Human_Green_label.setText(QCoreApplication.translate("MainWindow", u"530nm", None))
        self.Human_Red_label.setText(QCoreApplication.translate("MainWindow", u"560nm", None))
        self.Zebrafish_UV_label.setText(QCoreApplication.translate("MainWindow", u"361nm", None))
        self.Zebrafish_Blue_label.setText(QCoreApplication.translate("MainWindow", u"411nm", None))
        self.Zebrafish_Green_label.setText(QCoreApplication.translate("MainWindow", u"482nm", None))
        self.Zebrafish_Red_label.setText(QCoreApplication.translate("MainWindow", u"565nm", None))
        self.Chicken_UV_label.setText(QCoreApplication.translate("MainWindow", u"415nm", None))
        self.Chicken_Blue_label.setText(QCoreApplication.translate("MainWindow", u"455nm", None))
        self.Chicken_Green_label.setText(QCoreApplication.translate("MainWindow", u"508nm", None))
        self.Chicken_Red_label.setText(QCoreApplication.translate("MainWindow", u"571nm", None))
        self.OpsinSpectra_Update_pushButton.setText(QCoreApplication.translate("MainWindow", u"Update Opsin", None))
        self.LEDSpectra_Title.setText(QCoreApplication.translate("MainWindow", u"LED Spectra", None))
        self.LEDSpectra_LoadData_pushButton.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.LEDSpectra_LoadData_label.setText("")
        self.LEDSpectra_Load_label.setText(QCoreApplication.translate("MainWindow", u"Select a stimulation LED array", None))
        self.LEDSpectra_Load_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select", None))
        self.LEDSpectra_Load_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Original tetrachromatic", None))

        self.LEDSpectra_Display_pushButton.setText(QCoreApplication.translate("MainWindow", u"Display LED Spectra", None))
        self.Tetrachromatic_UV_label.setText(QCoreApplication.translate("MainWindow", u"373nm", None))
        self.Tetrachromatic_Blue_label.setText(QCoreApplication.translate("MainWindow", u"428nm", None))
        self.Tetrachromatic_Green_label.setText(QCoreApplication.translate("MainWindow", u"487nm", None))
        self.Tetrachromatic_Red_label.setText(QCoreApplication.translate("MainWindow", u"587nm", None))
        self.Tetrachromatic_Update_pushButton.setText(QCoreApplication.translate("MainWindow", u"Update LED", None))
        self.Spectra_RightMenu_container_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide Sub Menus", None))
        self.OpsinSpectra_tab_pushButton.setText(QCoreApplication.translate("MainWindow", u"Cone Absoprtion Spectra", None))
        self.LEDSpectra_tab_pushButton.setText(QCoreApplication.translate("MainWindow", u"LED Spectra", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.License_Label.setText(QCoreApplication.translate("MainWindow", u"This project is licensed under the GNU General Public License v3.0", None))
        self.BadenLab_Logo.setText("")
        self.OSN_Logo.setText("")
        self.SizeGrip_Label.setText("")
    # retranslateUi

