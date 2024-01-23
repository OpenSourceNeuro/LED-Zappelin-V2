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

        self.verticalLayout_11.addWidget(self.LEDZap_stackedWidget)


        self.verticalLayout_9.addWidget(self.LEDZap_LED_frame)


        self.horizontalLayout_13.addWidget(self.LEDZap_Stimulus_frame)


        self.verticalLayout_7.addWidget(self.LEDZap_Frame)

        self.Main_stackedWidget.addWidget(self.LEDZap_Page)

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

        self.Main_stackedWidget.setCurrentIndex(1)
        self.LED_Zap_Display_stackedWidget.setCurrentIndex(0)
        self.LEDZap_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.AppName_pushButton.setText(QCoreApplication.translate("MainWindow", u"LED Zappelin' v2 - Lagnado version ", None))
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
        self.License_Label.setText(QCoreApplication.translate("MainWindow", u"This project is licensed under the GNU General Public License v3.0", None))
        self.BadenLab_Logo.setText("")
        self.OSN_Logo.setText("")
        self.SizeGrip_Label.setText("")
    # retranslateUi

