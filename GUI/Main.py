########################################################################
# Libraries import

import sys
import os
import platform
import serial

# Import QT libraries
from PySide6 import QtCore, QtGui, QtWidgets, QtSerialPort
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

from Arrays import *
from Settings import *
from SerialMonitor import *
from Colours import *

from LED_Zappelin import Ui_MainWindow

# Import GUI page scripts
import Page000, Page101, Page201, Page301, Page401, Page501, Page601, Page701, Page801


# Setting UART parameters
#ports = Settings.COM()
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    if sys.platform == "linux" or sys.platform == "linux2":
        portList.append(port.systemLocation())
        print(port.systemLocation())
    else:
        portList.append(port.portName())

## ==> GLOBALS
counter = 0
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Custom Navigation bar buttons
        self.icon_expand = QIcon()
        self.icon_expand.addFile(u":/resources/resources/Expand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_reduce = QIcon()
        self.icon_reduce.addFile(u":/resources/resources/Reduce.png", QSize(), QIcon.Normal, QIcon.Off)

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                p = event.globalPosition()
                self.move(self.pos() + p.toPoint() - self.dragPos)
                self.dragPos = p.toPoint()
                event.accept()

        # Generate LED colours
        LEDZap_Colours(self)
        Chrolis_Colours(self)
        Spectra_Colours(self)

        # Generate toggle buttons for LEDZap
        LEDZapSetup(self)
        # Generate toggle buttons for Chrolis
        ChrolisSetup(self)
        # Generate toggle buttons for Spectra
        SpectraSetup(self)

        LEDZap_Arrays(self)
        Chrolis_Arrays(self)
        Spectra_Arrays(self)


        # Custom Navigation bar movement
        self.ui.Header_Frame.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)


        ########################################################################
        # Set menu/navigation buttons

        # Main Menu Container
        self.icon_DropMenuLeft = QIcon()
        self.icon_DropMenuLeft.addFile(u":/resources/resources/DropMenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_MenuLeft = QIcon()
        self.icon_MenuLeft.addFile(u":/resources/resources/MenuLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.SubMenu_Frame.setMaximumSize(QSize(0, 16777215))
        self.ui.SubMenu_Frame.setMinimumSize(QSize(0, 16777215))
        self.ui.Menu_Frame.setMinimumSize(QSize(leftMenu_max, 16777215))
        self.ui.DropMenu_pushButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, self.ui.Menu_Frame, leftMenu_min, leftMenu_max, animation_speed,
                                                                                   self.ui.DropMenu_pushButton, self.icon_MenuLeft, self.icon_DropMenuLeft, True))

        # Left Menu Container
        self.ui.LEDZappelin_pushButton.clicked.connect(lambda: Page101.LED_Zappelin.ShowPage(self))
        self.ui.Chrolis_pushButton.clicked.connect(lambda: Page201.Chrolis.ShowPage(self))
        self.ui.Stimulus_pushButton.clicked.connect(lambda: Page301.ShowPage(self))
        self.ui.Spectra_pushButton.clicked.connect(lambda: Page401.Spectra.ShowPage(self))
        self.ui.Settings_pushButton.clicked.connect(lambda: UIFunctions.expandMenu(self, self.ui.SubMenu_Frame, centerMenu_min, centerMenu_max,animation_speed, True))
        self.ui.About_pushButton.clicked.connect(lambda: Page601.ShowPage(self))
        self.ui.Help_pushButton.clicked.connect(lambda: Page701.ShowPage(self))
        self.ui.GitHub_pushButton.clicked.connect(lambda: Page801.ShowPage(self))
        self.ui.HideSubFrame_pushButton.clicked.connect(lambda: UIFunctions.collapseMenu(self, self.ui.SubMenu_Frame, centerMenu_min, centerMenu_max, animation_speed, True))


        ########################################################################
        # Home Page - page000
        # Display Home page on start up
        self.ui.Main_stackedWidget.setCurrentWidget(self.ui.Home_Page)

        self.ui.AppName_pushButton.clicked.connect(lambda: self.ui.Main_stackedWidget.setCurrentWidget(self.ui.Home_Page))

        ########################################################################
        # LED Zappelin Page - page101

        # Display page101 when LED Zappelin button is clicked
        self.ui.LEDZappelin_pushButton.clicked.connect(lambda: Page101.LED_Zappelin.ShowPage(self))

        #Init Flag and Monitor
        self.ui.LED_Zap_Serial_label.setText('Select a COM port to connect LED Zappelin device')
        self.ui.LEDZap_ConnectFlag = False
        self.ui.LEDZap_SerialFlag = False
        self.ui.LEDZap_StimulusFlag = False
        self.ui.LEDZap_StartStimulusFlag = False
        self.ui.LEDZap_PlayingFlag = False
        self.ui.GetLEDFlag = True
        self.ui.LED_Zap_Display1.clear()
        Page101.LEDZap_Stimuli.SetGraph(self)
        self.ui.LEDZap_LED_counter = 0

        # Update connected port COM and append them
        for i in range(len(ports)):
            self.ui.LEDZap_SelectPortComboBox.addItem("")
        for i in range(len(ports)):
            self.ui.LEDZap_SelectPortComboBox.setItemText(i + 1, str(portList[i]))
        #COM port connections
        self.ui.LEDZap_SelectPortComboBox.currentIndexChanged.connect(lambda: Page101.LED_Zappelin.ChangePort(self))

        # Start reading serial when connect button is clicked
        self.ui.LEDZap_ConnectButton.clicked.connect(lambda: Page101.LED_Zappelin.ConnectSerial(self))

        # Play Stimulus
        self.ui.LEDZap_Start_pushButton.clicked.connect(lambda: Page101.PlayStimuli(self))

        # Sop Stimulus
        self.ui.LEDZap_Stop_pushButton.clicked.connect(lambda: Page101.StopStimulus(self))

        # Load Stimulus
        self.ui.LEDZap_Load_pushButton.clicked.connect(lambda: Page101.LoadStimulus(self))

        # Display Stimulus
        self.ui.LEDZap_Display_pushButton.clicked.connect(lambda: Page101.LEDZap_Stimuli.DrawGraph(self))

        # Switch LED page
        self.ui.LEDZap_Switch_pushButton1.clicked.connect(lambda: self.ui.LEDZap_stackedWidget.setCurrentWidget(self.ui.LEDZap_page1))
        self.ui.LEDZap_Switch_pushButton2.clicked.connect(lambda: self.ui.LEDZap_stackedWidget.setCurrentWidget(self.ui.LEDZap_page2))

        # Graph Display page
        self.ui.LED_Zap_Display1_pushButton.clicked.connect(lambda: self.ui.LED_Zap_Display_stackedWidget.setCurrentWidget(self.ui.LED_Zap_Display_page2))
        self.ui.LED_Zap_Display2_pushButton.clicked.connect(lambda: self.ui.LED_Zap_Display_stackedWidget.setCurrentWidget(self.ui.LED_Zap_Display_page1))

        # LED toggle buttons
        self.ui.All_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.DeactivateAllLED(self))
        self.ui.LED01_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.DeactivateLED(self, 0))
        self.ui.LED02_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.DeactivateLED(self, 1))
        self.ui.LED03_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.DeactivateLED(self, 2))
        self.ui.LED04_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.DeactivateLED(self, 3))
        self.ui.LED05_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.DeactivateLED(self, 4))
        self.ui.LED06_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.DeactivateLED(self, 5))
        self.ui.LED07_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.DeactivateLED(self, 6))
        self.ui.LED08_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.DeactivateLED(self, 7))
        self.ui.LED09_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.DeactivateLED(self, 8))
        self.ui.LED10_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.DeactivateLED(self, 9))
        self.ui.LED11_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.DeactivateLED(self, 10))
        self.ui.LED12_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.DeactivateLED(self, 11))


        ########################################################################
        # Chrolis Page - page201

        # Display page201 when Chrolis button is clicked
        self.ui.Chrolis_pushButton.clicked.connect(lambda: Page201.Chrolis.ShowPage(self))

        #Init Flag and Monitor
        self.ui.Chrolis_Serial_label.setText('Select a COM port to connect LED Zappelin device')
        self.ui.Chrolis_ConnectFlag = False
        self.ui.Chrolis_SerialFlag = False
        self.ui.Chrolis_StimulusFlag = False
        self.ui.Chrolis_StartStimulusFlag = False
        self.ui.Chrolis_PlayingFlag = False
        self.ui.GetChrolisFlag = True
        self.ui.Chrolis_Display1.clear()
        Page201.Chrolis_Stimuli.SetGraph(self)
        self.ui.Chrolis_LED_counter = 0



        # Update connected port COM and append them
        for i in range(len(ports)):
            self.ui.Chrolis_SelectPortComboBox.addItem("")
        for i in range(len(ports)):
            self.ui.Chrolis_SelectPortComboBox.setItemText(i + 1, str(portList[i]))
        # COM port connections
        self.ui.Chrolis_SelectPortComboBox.currentIndexChanged.connect(lambda: Page201.Chrolis.ChangePort(self))

        # Start reading serial when connect button is clicked
        self.ui.Chrolis_ConnectButton.clicked.connect(lambda: Page201.Chrolis.ConnectSerial(self))

        # Play Stimulus
        self.ui.Chrolis_Start_pushButton.clicked.connect(lambda: Page201.PlayStimuli(self))

        # Sop Stimulus
        self.ui.Chrolis_Stop_pushButton.clicked.connect(lambda: Page201.StopStimulus(self))

        # Load Stimulus
        self.ui.Chrolis_Load_pushButton.clicked.connect(lambda: Page201.LoadStimulus(self))

        # Display Stimulus
        self.ui.Chrolis_Display_pushButton.clicked.connect(lambda: Page201.Chrolis_Stimuli.DrawGraph(self))

        # Graph Display page
        self.ui.Chrolis_Display1_pushButton.clicked.connect(lambda: self.ui.Chrolis_Display_stackedWidget.setCurrentWidget(self.ui.Chrolis_Display_page2))
        self.ui.Chrolis_Display2_pushButton.clicked.connect(lambda: self.ui.Chrolis_Display_stackedWidget.setCurrentWidget(self.ui.Chrolis_Display_page1))

        # LED toggle buttons
        self.ui.ChrolisAll_toggleButton.toggled.connect(lambda: Page201.Chrolis.DeactivateAllLED(self))
        self.ui.Chrolis01_toggleButton.toggled.connect(lambda: Page201.Chrolis.DeactivateLED(self, 0))
        self.ui.Chrolis02_toggleButton.toggled.connect(lambda: Page201.Chrolis.DeactivateLED(self, 1))
        self.ui.Chrolis03_toggleButton.toggled.connect(lambda: Page201.Chrolis.DeactivateLED(self, 2))
        self.ui.Chrolis04_toggleButton.toggled.connect(lambda: Page201.Chrolis.DeactivateLED(self, 3))
        self.ui.Chrolis05_toggleButton.toggled.connect(lambda: Page201.Chrolis.DeactivateLED(self, 4))
        self.ui.Chrolis06_toggleButton.toggled.connect(lambda: Page201.Chrolis.DeactivateLED(self, 5))
        self.ui.Chrolis07_toggleButton.toggled.connect(lambda: Page201.Chrolis.DeactivateLED(self, 6))
        self.ui.Chrolis08_toggleButton.toggled.connect(lambda: Page201.Chrolis.DeactivateLED(self, 7))
        self.ui.Chrolis09_toggleButton.toggled.connect(lambda: Page201.Chrolis.DeactivateLED(self, 8))
        self.ui.Chrolis10_toggleButton.toggled.connect(lambda: Page201.Chrolis.DeactivateLED(self, 9))
        self.ui.Chrolis11_toggleButton.toggled.connect(lambda: Page201.Chrolis.DeactivateLED(self, 10))
        self.ui.Chrolis12_toggleButton.toggled.connect(lambda: Page201.Chrolis.DeactivateLED(self, 11))

        ########################################################################
        # Spectra Page - page401

        # Navigation buttons
        self.icon_DropMenuRight = QIcon()
        self.icon_DropMenuRight.addFile(u":/resources/resources/DropMenuRight.png", QSize(), QIcon.Normal,QIcon.Off)
        self.icon_MenuRight = QIcon()
        self.icon_MenuRight.addFile(u":/resources/resources/MenuRight.png", QSize(), QIcon.Normal, QIcon.Off)

        # Spectra parameters navigation button
        self.ui.Spectra_CenterMenu_container.setMaximumSize(QSize(0, 16777215))
        self.ui.Spectra_RightMenu_container.setMinimumSize(QSize(rightSubMenu_max, 16777215))
        self.ui.Spectra_RightMenu_container_pushButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, self.ui.Spectra_RightMenu_container, rightSubMenu_min, rightSubMenu_max, animation_speed,
                                                                                                          self.ui.Spectra_RightMenu_container_pushButton, self.icon_MenuRight, self.icon_DropMenuRight, True))
        self.ui.OpsinSpectra_tab_pushButton.clicked.connect(lambda: UIFunctions.expandMenu(self, self.ui.Spectra_CenterMenu_container, rightMenu_min, rightMenu_max, animation_speed, True))
        self.ui.LEDSpectra_tab_pushButton.clicked.connect(lambda: UIFunctions.expandMenu(self, self.ui.Spectra_CenterMenu_container, rightMenu_min, rightMenu_max, animation_speed, True))
        self.ui.Spectra_CenterMenu_Hide_pushButton.clicked.connect(lambda: UIFunctions.collapseMenu(self, self.ui.Spectra_CenterMenu_container, rightMenu_min, rightMenu_max, animation_speed, True))

        # Opsin Tab
        self.ui.OpsinSpectra_tab_pushButton.clicked.connect(lambda: self.ui.Spectra_stackedWidget.setCurrentWidget(self.ui.OpsinSpectra_page))
        # Load Data
        self.ui.OpsinSpectra_Load_comboBox.currentIndexChanged.connect(lambda: Page401.Spectra.ChangeOpsinPage(self))
        # Generate Opsin
        self.ui.OpsinSpectra_DisplayOpsin_pushButton.clicked.connect(lambda:Page401.Spectra.GenerateOpsin(self))

        # Spectra Tab
        self.ui.LEDSpectra_tab_pushButton.clicked.connect(lambda: self.ui.Spectra_stackedWidget.setCurrentWidget(self.ui.LEDSpectra_page))
        # Select Folder
        self.ui.LEDSpectra_LoadData_pushButton.clicked.connect(lambda: Page401.LEDSpectra.SelectFolder(self))
        # Load Data
        self.ui.LEDSpectra_Load_comboBox.currentIndexChanged.connect(lambda: Page401.LEDSpectra.LoadData(self))
        # Generate Spectra
        self.ui.LEDSpectra_Display_pushButton.clicked.connect(lambda: Page401.LEDSpectra.GenerateLEDSpectra(self))

        ########################################################################


    # Display
        self.show()

    ## APP EVENTS
    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos





########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(u":/resources/resources/Neuron.png"))
    window = MainWindow()
    sys.exit(app.exec())
########################################################################
## END===>
########