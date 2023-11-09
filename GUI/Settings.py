import sys
import serial
from Main import MainWindow
import resources_rc
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QPropertyAnimation
from PySide6.QtWidgets import QSizeGrip

from py_toggle import PyToggle
import Page101, Page201
from Colours import *


def LEDZapSetup(self):
    self.ui.BaudRate = 921600
    Theme(self)
    self.SerialFlag = False
    self.serial_port = serial.Serial()
    # Generate toggle buttons ofr LEDZap
    self.ui.All_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                        circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                        active_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[15])
                                        )
    self.ui.All_toggleButton_layout.addWidget(self.ui.All_toggleButton)

    self.ui.LED01_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                          circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                          active_color='#%02x%02x%02x' % tuple(self.ui.LEDZap_RGB[0])
                                          )
    self.ui.LED01_toggleButton_layout.addWidget(self.ui.LED01_toggleButton)

    self.ui.LED02_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                          circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                          active_color='#%02x%02x%02x' % tuple(self.ui.LEDZap_RGB[1])
                                          )
    self.ui.LED02_toggleButton_layout.addWidget(self.ui.LED02_toggleButton)

    self.ui.LED03_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                          circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                          active_color='#%02x%02x%02x' % tuple(self.ui.LEDZap_RGB[2])
                                          )
    self.ui.LED03_toggleButton_layout.addWidget(self.ui.LED03_toggleButton)

    self.ui.LED04_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                          circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                          active_color='#%02x%02x%02x' % tuple(self.ui.LEDZap_RGB[3])
                                          )
    self.ui.LED04_toggleButton_layout.addWidget(self.ui.LED04_toggleButton)



    self.ProxyLED_value = self.ui.LEDZap_ProxyLED_Slider.value()
    self.ProxyLED_Value = int(self.ProxyLED_value / 255 * 100)
    self.ui.LEDZap_ProxyLED_value.setText(str(self.ProxyLED_Value) + ' %')

    self.ui.LED01_toggleButton.setChecked(True)
    self.LED01_Val = self.ui.LED01_Slider.value()
    self.ui.LED01_Value.setText(str(self.LED01_Val) + ' %')

    self.ui.LED02_Slider.setEnabled(False)
    self.ui.LED02_Slider.setValue(0)
    self.ui.LED03_Slider.setEnabled(False)
    self.ui.LED03_Slider.setValue(0)
    self.ui.LED04_Slider.setEnabled(False)
    self.ui.LED04_Slider.setValue(0)

    self.ui.All_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.ActivateAllLED(self))
    self.ui.All_LED_Slider.valueChanged.connect(lambda: Page101.LED_Zappelin.GetAllLED(self))

    self.ui.LED01_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.ActivateLED(self,0))
    self.ui.LED01_Slider.valueChanged.connect(lambda: Page101.LED_Zappelin.GetLED(self,0))

    self.ui.LED02_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.ActivateLED(self,1))
    self.ui.LED02_Slider.valueChanged.connect(lambda: Page101.LED_Zappelin.GetLED(self,1))

    self.ui.LED03_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.ActivateLED(self,2))
    self.ui.LED03_Slider.valueChanged.connect(lambda: Page101.LED_Zappelin.GetLED(self,2))

    self.ui.LED04_toggleButton.toggled.connect(lambda: Page101.LED_Zappelin.ActivateLED(self,3))
    self.ui.LED04_Slider.valueChanged.connect(lambda: Page101.LED_Zappelin.GetLED(self,3))


    self.ui.All_LED_Slider.setEnabled(False)
    self.ui.All_LED_Slider.setValue(0)



animation_speed = 500
leftMenu_min = 40
leftMenu_max = 180
centerMenu_min = 0
centerMenu_max = 200
rightMenu_min = 0
rightMenu_max = 200
rightSubMenu_min = 40
rightSubMenu_max = 200

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

        def maximize_restore(self):
            global GLOBAL_STATE
            status = GLOBAL_STATE

            # IF NOT MAXIMIZED
            if status == 0:
                self.showMaximized()
                self.ui.Expand_pushButton.setIcon(self.icon_reduce)

                # SET GLOBAL TO 1
                GLOBAL_STATE = 1
                self.ui.Expand_pushButton.setToolTip("Restore")

            else:
                GLOBAL_STATE = 0
                self.showNormal()
                self.ui.Expand_pushButton.setIcon(self.icon_expand)
                self.resize(self.width() + 1, self.height() + 1)
                self.ui.Expand_pushButton.setToolTip("Maximize")

        ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
        def returnStatus():
            return GLOBAL_STATE


        ## ==> UI DEFINITIONS
        def uiDefinitions(self):

            # REMOVE TITLE BAR
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

            # MAXIMIZE / RESTORE
            self.ui.Expand_pushButton.clicked.connect(lambda: UIFunctions.maximize_restore(self))

            # MINIMIZE
            self.ui.Reduce_pushButton.clicked.connect(lambda: self.showMinimized())

            # CLOSE
            self.ui.Exit_pushButton.clicked.connect(lambda: self.close())

            ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
            self.sizegrip = QSizeGrip(self.ui.SizeGrip_Frame)
            self.sizegrip.setToolTip("Resize Window")



        def toggleMenu(self, menu, standard, maxWidth, duration, pushButton, icon_min, icon_max, enable):
                if enable:
                        #Get width
                        width = menu.width()

                        #Extend
                        if width == standard:
                                widthExtended = maxWidth
                                pushButton.setIcon(icon_max)
                        #Retract
                        else:
                                widthExtended = standard
                                pushButton.setIcon(icon_min)

                        #Animation
                        self.animation = QPropertyAnimation(menu, b"minimumWidth")
                        self.animation.setDuration(duration)
                        self.animation.setStartValue(width)
                        self.animation.setEndValue(widthExtended)
                        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                        self.animation.start()

        def expandMenu(self, menu, standard, maxWidth, duration, enable):
                if enable:
                        width = menu.width()
                        if width == standard:
                            #Animation
                            self.animation = QPropertyAnimation(menu, b"minimumWidth")
                            self.animation.setDuration(duration)
                            self.animation.setStartValue(standard)
                            self.animation.setEndValue(maxWidth)
                            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                            self.animation.start()

        def collapseMenu(self, menu, standard, maxWidth, duration, enable):
                if enable:
                        width = menu.width()
                        if width == maxWidth:
                            #Animation
                            self.animation = QPropertyAnimation(menu, b"minimumWidth")
                            self.animation.setDuration(duration)
                            self.animation.setStartValue(maxWidth)
                            self.animation.setEndValue(standard)
                            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                            self.animation.start()


