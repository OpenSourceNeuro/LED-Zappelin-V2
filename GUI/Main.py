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
from Colours import *

from LED_Zappelin import Ui_MainWindow

# Import GUI page scripts
import Page000, Page101


# Setting UART parameters
#ports = Settings.COM()
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    if sys.platform == "linux" or sys.platform == "linux2":
        portList.append(port.systemLocation())
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

        # Generate toggle buttons for LEDZap
        LEDZapSetup(self)

        LEDZap_Arrays(self)

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
        self.ui.Menu_Frame.setMinimumSize(QSize(leftMenu_min, 16777215))
        self.ui.DropMenu_pushButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, self.ui.Menu_Frame, leftMenu_min, leftMenu_max, animation_speed,
                                                                                   self.ui.DropMenu_pushButton, self.icon_MenuLeft, self.icon_DropMenuLeft, True))

        # Left Menu Container
        self.ui.LEDZappelin_pushButton.clicked.connect(lambda: Page101.LED_Zappelin.ShowPage(self))
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
        self.ui.TestLEDFlag = False
        self.ui.TestLEDPlayFlag = False
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
        self.ui.LEDZap_Start_pushButton.clicked.connect(lambda: Page101.PlayStimuliButton(self))
        self.ui.LEDZap_Start_pushButton.clicked.connect(lambda: Page101.PlayStimuli(self))

        # Sop Stimulus
        self.ui.LEDZap_Stop_pushButton.clicked.connect(lambda: Page101.StopStimulus(self))

        # Load Stimulus
        self.ui.LEDZap_Load_pushButton.clicked.connect(lambda: Page101.LoadStimulus(self))

        # Display Stimulus
        self.ui.LEDZap_Display_pushButton.clicked.connect(lambda: Page101.LEDZap_Stimuli.DrawGraph(self))

        # Test LEDs
        self.ui.LEDZap_Test_pushButton.clicked.connect(lambda: Page101.TestLED(self))

        # Graph Display page
        self.ui.LED_Zap_Display1_pushButton.clicked.connect(lambda: self.ui.LED_Zap_Display_stackedWidget.setCurrentWidget(self.ui.LED_Zap_Display_page2))
        self.ui.LED_Zap_Display2_pushButton.clicked.connect(lambda: self.ui.LED_Zap_Display_stackedWidget.setCurrentWidget(self.ui.LED_Zap_Display_page1))

        # Load LED Settings
        self.ui.Preselect_Load_frame_pushButton.clicked.connect(lambda: Page101.LoadPreSet(self))
        # Apply LED Settings
        self.ui.Preselect_Apply_pushButton.clicked.connect(lambda: Page101.ApplyPreSet(self))


        # Proxy LED slider
        self.ui.LEDZap_ProxyLED_Slider.valueChanged.connect(lambda: Page101.SetBrightness(self))


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