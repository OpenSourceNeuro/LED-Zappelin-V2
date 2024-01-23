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
        icon5 = QIcon()
        icon5.addFile(u":/resources/resources/Settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Settings_pushButton.setIcon(icon5)
        self.Settings_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.Settings_pushButton)

        self.About_pushButton = QPushButton(self.Options_Frame)
        self.About_pushButton.setObjectName(u"About_pushButton")
        self.About_pushButton.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/resources/resources/About.png", QSize(), QIcon.Normal, QIcon.Off)
        self.About_pushButton.setIcon(icon6)
        self.About_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.About_pushButton)

        self.Help_pushButton = QPushButton(self.Options_Frame)
        self.Help_pushButton.setObjectName(u"Help_pushButton")
        self.Help_pushButton.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u":/resources/resources/Help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Help_pushButton.setIcon(icon7)
        self.Help_pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.Help_pushButton)

        self.GitHub_pushButton = QPushButton(self.Options_Frame)
        self.GitHub_pushButton.setObjectName(u"GitHub_pushButton")
        self.GitHub_pushButton.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u":/resources/resources/GitHub.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GitHub_pushButton.setIcon(icon8)
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
        font4 = QFont()
        font4.setPointSize(10)
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
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Chrolis_StimulusControl_frame = QFrame(self.Chrolis_Stimulus_frame)
        self.Chrolis_StimulusControl_frame.setObjectName(u"Chrolis_StimulusControl_frame")
        self.Chrolis_StimulusControl_frame.setMinimumSize(QSize(0, 50))
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
        font5 = QFont()
        font5.setPointSize(8)
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

        self.label_2 = QLabel(self.Chrolis_Stimulus_frame)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        self.label_2.setFont(font6)

        self.verticalLayout_14.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.Blanking_Frame = QFrame(self.Chrolis_Stimulus_frame)
        self.Blanking_Frame.setObjectName(u"Blanking_Frame")
        self.Blanking_Frame.setMinimumSize(QSize(0, 30))
        self.Blanking_Frame.setFrameShape(QFrame.StyledPanel)
        self.Blanking_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.Blanking_Frame)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Blanking_Toggle_Frame = QFrame(self.Blanking_Frame)
        self.Blanking_Toggle_Frame.setObjectName(u"Blanking_Toggle_Frame")
        self.Blanking_Toggle_Frame.setMinimumSize(QSize(0, 0))
        self.Blanking_Toggle_Frame.setMaximumSize(QSize(16777215, 16777215))
        self.Blanking_Toggle_Frame.setFrameShape(QFrame.StyledPanel)
        self.Blanking_Toggle_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.Blanking_Toggle_Frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Blanking_Toggle_Label_Frame = QFrame(self.Blanking_Toggle_Frame)
        self.Blanking_Toggle_Label_Frame.setObjectName(u"Blanking_Toggle_Label_Frame")
        self.Blanking_Toggle_Label_Frame.setFrameShape(QFrame.StyledPanel)
        self.Blanking_Toggle_Label_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.Blanking_Toggle_Label_Frame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 0, 0, 0)
        self.Blanking_Toggle_Label = QLabel(self.Blanking_Toggle_Label_Frame)
        self.Blanking_Toggle_Label.setObjectName(u"Blanking_Toggle_Label")
        self.Blanking_Toggle_Label.setMaximumSize(QSize(200, 16777215))
        self.Blanking_Toggle_Label.setFont(font1)
        self.Blanking_Toggle_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.Blanking_Toggle_Label)


        self.horizontalLayout_13.addWidget(self.Blanking_Toggle_Label_Frame)

        self.Blanking_Toggle_frame = QFrame(self.Blanking_Toggle_Frame)
        self.Blanking_Toggle_frame.setObjectName(u"Blanking_Toggle_frame")
        self.Blanking_Toggle_frame.setMaximumSize(QSize(16777215, 16777215))
        self.Blanking_Toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.Blanking_Toggle_frame.setFrameShadow(QFrame.Raised)
        self.Blanking_toggleButton_layout = QHBoxLayout(self.Blanking_Toggle_frame)
        self.Blanking_toggleButton_layout.setSpacing(0)
        self.Blanking_toggleButton_layout.setObjectName(u"Blanking_toggleButton_layout")
        self.Blanking_toggleButton_layout.setContentsMargins(5, 0, 10, 0)

        self.horizontalLayout_13.addWidget(self.Blanking_Toggle_frame)


        self.horizontalLayout_11.addWidget(self.Blanking_Toggle_Frame)

        self.Blanking_Value_Frame = QFrame(self.Blanking_Frame)
        self.Blanking_Value_Frame.setObjectName(u"Blanking_Value_Frame")
        self.Blanking_Value_Frame.setFrameShape(QFrame.StyledPanel)
        self.Blanking_Value_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.Blanking_Value_Frame)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 10, 0)
        self.Blanking_lineEdit_Frame = QFrame(self.Blanking_Value_Frame)
        self.Blanking_lineEdit_Frame.setObjectName(u"Blanking_lineEdit_Frame")
        self.Blanking_lineEdit_Frame.setMinimumSize(QSize(100, 0))
        self.Blanking_lineEdit_Frame.setMaximumSize(QSize(100, 16777215))
        self.Blanking_lineEdit_Frame.setStyleSheet(u"")
        self.Blanking_lineEdit_Frame.setFrameShape(QFrame.StyledPanel)
        self.Blanking_lineEdit_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.Blanking_lineEdit_Frame)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 5, 0)
        self.Blanking_lineEdit = QLineEdit(self.Blanking_lineEdit_Frame)
        self.Blanking_lineEdit.setObjectName(u"Blanking_lineEdit")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        self.Blanking_lineEdit.setFont(font7)
        self.Blanking_lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.Blanking_lineEdit.setStyleSheet(u" border: 1px solid rgb(147,161,161);\n"
"background-color: rgb(7, 54, 66);")
        self.Blanking_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.Blanking_lineEdit)


        self.horizontalLayout_18.addWidget(self.Blanking_lineEdit_Frame)

        self.Blanking_Label_Frame = QFrame(self.Blanking_Value_Frame)
        self.Blanking_Label_Frame.setObjectName(u"Blanking_Label_Frame")
        self.Blanking_Label_Frame.setFrameShape(QFrame.StyledPanel)
        self.Blanking_Label_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.Blanking_Label_Frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Blanking_Label = QLabel(self.Blanking_Label_Frame)
        self.Blanking_Label.setObjectName(u"Blanking_Label")
        self.Blanking_Label.setFont(font7)

        self.horizontalLayout_14.addWidget(self.Blanking_Label)


        self.horizontalLayout_18.addWidget(self.Blanking_Label_Frame)


        self.horizontalLayout_11.addWidget(self.Blanking_Value_Frame, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.Blanking_Frame)

        self.line = QFrame(self.Chrolis_Stimulus_frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(0, 30, 38);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line)

        self.Chrolis_LED_frame = QFrame(self.Chrolis_Stimulus_frame)
        self.Chrolis_LED_frame.setObjectName(u"Chrolis_LED_frame")
        self.Chrolis_LED_frame.setFrameShape(QFrame.StyledPanel)
        self.Chrolis_LED_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.Chrolis_LED_frame)
        self.verticalLayout_18.setSpacing(7)
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
        self.horizontalLayout_135.setContentsMargins(0, 5, 0, 5)
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
        self.Chrolis_Display_stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.AppName_pushButton.setText(QCoreApplication.translate("MainWindow", u"LED Zappelin' v2 - Chrolis vanilla version", None))
        self.Reduce_pushButton.setText("")
        self.Expand_pushButton.setText("")
        self.Exit_pushButton.setText("")
        self.DropMenu_pushButton.setText(QCoreApplication.translate("MainWindow", u"Hide Menus", None))
        self.LEDZappelin_pushButton.setText(QCoreApplication.translate("MainWindow", u"LED Zappelin'", None))
        self.Settings_pushButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.About_pushButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.Help_pushButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.GitHub_pushButton.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Blanking Parameters", None))
        self.Blanking_Toggle_Label.setText(QCoreApplication.translate("MainWindow", u"Invert", None))
        self.Blanking_lineEdit.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.Blanking_Label.setText(QCoreApplication.translate("MainWindow", u"\u03bcs", None))
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
        self.License_Label.setText(QCoreApplication.translate("MainWindow", u"This project is licensed under the GNU General Public License v3.0", None))
        self.BadenLab_Logo.setText("")
        self.OSN_Logo.setText("")
        self.SizeGrip_Label.setText("")
    # retranslateUi

