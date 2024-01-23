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
import Page000, Page201


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
        Chrolis_Colours(self)

        # Generate toggle buttons for Chrolis
        ChrolisSetup(self)

        Chrolis_Arrays(self)


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
        self.ui.LEDZappelin_pushButton.clicked.connect(lambda: Page201.Chrolis.ShowPage(self))

        ########################################################################
        # Home Page - page000
        # Display Home page on start up
        self.ui.Main_stackedWidget.setCurrentWidget(self.ui.Home_Page)

        self.ui.AppName_pushButton.clicked.connect(lambda: self.ui.Main_stackedWidget.setCurrentWidget(self.ui.Home_Page))


        ########################################################################
        # Chrolis Page - page201

        # Display page201 when Chrolis button is clicked
        self.ui.LEDZappelin_pushButton.clicked.connect(lambda: Page201.Chrolis.ShowPage(self))

        #Init Flag and Monitor
        self.ui.Chrolis_Serial_label.setText('Select a COM port to connect LED Zappelin device')
        self.ui.Chrolis_ConnectFlag = False
        self.ui.Chrolis_SerialFlag = False
        self.ui.Chrolis_StimulusFlag = False
        self.ui.Chrolis_StartStimulusFlag = False
        self.ui.Chrolis_PlayingFlag = False
        self.ui.GetChrolisFlag = True
        self.ui.TestLEDFlag = False
        self.ui.TestLEDPlayFlag = False
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
        self.ui.Chrolis_Start_pushButton.clicked.connect(lambda: Page201.PlayStimuliButton(self))
        self.ui.Chrolis_Start_pushButton.clicked.connect(lambda: Page201.PlayStimuli(self))

        # Sop Stimulus
        self.ui.Chrolis_Stop_pushButton.clicked.connect(lambda: Page201.StopStimulus(self))

        # Load Stimulus
        self.ui.Chrolis_Load_pushButton.clicked.connect(lambda: Page201.LoadStimulus(self))

        # Display Stimulus
        self.ui.Chrolis_Display_pushButton.clicked.connect(lambda: Page201.Chrolis_Stimuli.DrawGraph(self))

        # Test LEDs
        self.ui.Chrolis_Test_pushButton.clicked.connect(lambda: Page201.TestLED(self))


        # Graph Display page
        self.ui.Chrolis_Display1_pushButton.clicked.connect(lambda: self.ui.Chrolis_Display_stackedWidget.setCurrentWidget(self.ui.Chrolis_Display_page2))
        self.ui.Chrolis_Display2_pushButton.clicked.connect(lambda: self.ui.Chrolis_Display_stackedWidget.setCurrentWidget(self.ui.Chrolis_Display_page1))

        # Load LED Settings
        self.ui.Chrolis_Preselect_Load_frame_pushButton.clicked.connect(lambda: Page201.ChrolisLoadPreSet(self))
        # Apply LED Settings
        self.ui.Chrolis_Preselect_Apply_pushButton.clicked.connect(lambda: Page201.ChrolisApplyPreSet(self))

        # Proxy LED slider
        self.ui.Chrolis_ProxyLED_Slider.valueChanged.connect(lambda: Page201.SetChrolisBrightness(self))


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