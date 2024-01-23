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
import Page201
from Colours import *




def ChrolisSetup(self):
    self.ui.BaudRate = 921600
    Theme(self)
    self.SerialFlag = False
    self.serial_port = serial.Serial()
    # Generate toggle buttons for Chrolis
    self.ui.Blanking_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                              active_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[15]),
                                              width=50
                                              )
    self.ui.Blanking_toggleButton_layout.addWidget(self.ui.Blanking_toggleButton)

    self.ui.ChrolisAll_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                               circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                               active_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[15])
                                               )
    self.ui.ChrolisAll_toggleButton_layout.addWidget(self.ui.ChrolisAll_toggleButton)

    self.ui.Chrolis01_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                              active_color='#%02x%02x%02x' % tuple(self.ui.Chrolis_RGB[0])
                                              )
    self.ui.Chrolis01_toggleButton_layout.addWidget(self.ui.Chrolis01_toggleButton)

    self.ui.Chrolis02_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                              active_color='#%02x%02x%02x' % tuple(self.ui.Chrolis_RGB[1])
                                              )
    self.ui.Chrolis02_toggleButton_layout.addWidget(self.ui.Chrolis02_toggleButton)

    self.ui.Chrolis03_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                              active_color='#%02x%02x%02x' % tuple(self.ui.Chrolis_RGB[2])
                                              )
    self.ui.Chrolis03_toggleButton_layout.addWidget(self.ui.Chrolis03_toggleButton)

    self.ui.Chrolis04_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                              active_color='#%02x%02x%02x' % tuple(self.ui.Chrolis_RGB[3])
                                              )
    self.ui.Chrolis04_toggleButton_layout.addWidget(self.ui.Chrolis04_toggleButton)

    self.ui.Chrolis05_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                              active_color='#%02x%02x%02x' % tuple(self.ui.Chrolis_RGB[4])
                                              )
    self.ui.Chrolis05_toggleButton_layout.addWidget(self.ui.Chrolis05_toggleButton)

    self.ui.Chrolis06_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                              active_color='#%02x%02x%02x' % tuple(self.ui.Chrolis_RGB[5])
                                              )
    self.ui.Chrolis06_toggleButton_layout.addWidget(self.ui.Chrolis06_toggleButton)

    self.ui.Chrolis07_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                              active_color='#%02x%02x%02x' % tuple(self.ui.Chrolis_RGB[6])
                                              )
    self.ui.Chrolis07_toggleButton_layout.addWidget(self.ui.Chrolis07_toggleButton)

    self.ui.Chrolis08_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                              active_color='#%02x%02x%02x' % tuple(self.ui.Chrolis_RGB[7])
                                              )
    self.ui.Chrolis08_toggleButton_layout.addWidget(self.ui.Chrolis08_toggleButton)

    self.ui.Chrolis09_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                              active_color='#%02x%02x%02x' % tuple(self.ui.Chrolis_RGB[8])
                                              )
    self.ui.Chrolis09_toggleButton_layout.addWidget(self.ui.Chrolis09_toggleButton)

    self.ui.Chrolis10_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                              active_color='#%02x%02x%02x' % tuple(self.ui.Chrolis_RGB[9])
                                              )
    self.ui.Chrolis10_toggleButton_layout.addWidget(self.ui.Chrolis10_toggleButton)

    self.ui.Chrolis11_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                              active_color='#%02x%02x%02x' % tuple(self.ui.Chrolis_RGB[10])
                                              )
    self.ui.Chrolis11_toggleButton_layout.addWidget(self.ui.Chrolis11_toggleButton)

    self.ui.Chrolis12_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(self.ui.DarkSolarized[0]),
                                              active_color='#%02x%02x%02x' % tuple(self.ui.Chrolis_RGB[11])
                                              )
    self.ui.Chrolis12_toggleButton_layout.addWidget(self.ui.Chrolis12_toggleButton)


    self.ProxyLED_value = self.ui.Chrolis_ProxyLED_Slider.value()
    self.ProxyLED_Value = int(self.ProxyLED_value / 255 * 100)
    self.ui.Chrolis_ProxyLED_value.setText(str(self.ProxyLED_Value) + ' %')


    self.ui.Chrolis01_toggleButton.setChecked(True)
    self.Chrolis01_Val = self.ui.Chrolis01_Slider.value()
    self.ui.Chrolis01_Value.setText(str(self.Chrolis01_Val) + ' %')

    self.ui.Chrolis02_toggleButton.setChecked(True)
    self.Chrolis02_Val = self.ui.Chrolis02_Slider.value()
    self.ui.Chrolis02_Value.setText(str(self.Chrolis02_Val) + ' %')

    self.ui.Chrolis03_toggleButton.setChecked(True)
    self.Chrolis03_Val = self.ui.Chrolis03_Slider.value()
    self.ui.Chrolis03_Value.setText(str(self.Chrolis03_Val) + ' %')

    self.ui.Chrolis04_toggleButton.setChecked(True)
    self.Chrolis04_Val = self.ui.Chrolis04_Slider.value()
    self.ui.Chrolis04_Value.setText(str(self.Chrolis04_Val) + ' %')

    self.ui.Chrolis05_toggleButton.setChecked(True)
    self.Chrolis05_Val = self.ui.Chrolis05_Slider.value()
    self.ui.Chrolis05_Value.setText(str(self.Chrolis05_Val) + ' %')

    self.ui.Chrolis06_toggleButton.setChecked(True)
    self.Chrolis06_Val = self.ui.Chrolis06_Slider.value()
    self.ui.Chrolis06_Value.setText(str(self.Chrolis06_Val) + ' %')

    self.ui.Chrolis07_toggleButton.setChecked(True)
    self.Chrolis07_Val = self.ui.Chrolis07_Slider.value()
    self.ui.Chrolis07_Value.setText(str(self.Chrolis07_Val) + ' %')

    self.ui.Chrolis08_toggleButton.setChecked(True)
    self.Chrolis08_Val = self.ui.Chrolis08_Slider.value()
    self.ui.Chrolis08_Value.setText(str(self.Chrolis08_Val) + ' %')

    self.ui.Chrolis09_toggleButton.setChecked(True)
    self.Chrolis09_Val = self.ui.Chrolis09_Slider.value()
    self.ui.Chrolis09_Value.setText(str(self.Chrolis09_Val) + ' %')

    self.ui.Chrolis10_toggleButton.setChecked(True)
    self.Chrolis10_Val = self.ui.Chrolis10_Slider.value()
    self.ui.Chrolis10_Value.setText(str(self.Chrolis10_Val) + ' %')

    self.ui.Chrolis11_toggleButton.setChecked(True)
    self.Chrolis11_Val = self.ui.Chrolis11_Slider.value()
    self.ui.Chrolis11_Value.setText(str(self.Chrolis11_Val) + ' %')

    self.ui.Chrolis12_toggleButton.setChecked(True)
    self.Chrolis12_Val = self.ui.Chrolis12_Slider.value()
    self.ui.Chrolis12_Value.setText(str(self.Chrolis12_Val) + ' %')

    self.ui.ChrolisAll_toggleButton.setChecked(True)
    self.ChrolisAll_LED_Val = self.ui.ChrolisAll_LED_Slider.value()
    self.ui.ChrolisAll_LED_value.setText(str(self.ChrolisAll_LED_Val) + ' %')



    self.ui.Blanking_toggleButton.toggled.connect(lambda: Page201.Chrolis.Blanking(self))
    self.ui.Blanking_lineEdit.textChanged.connect(lambda: Page201.Chrolis.BlankingtValue(self))

    self.ui.ChrolisAll_toggleButton.toggled.connect(lambda: Page201.Chrolis.ActivateChrolisAll(self))
    self.ui.ChrolisAll_LED_Slider.valueChanged.connect(lambda: Page201.Chrolis.GetChrolisAll(self))
    self.ui.ChrolisAll_LED_Slider.valueChanged.connect(lambda: Page201.PlayTest(self))

    self.ui.Chrolis01_toggleButton.toggled.connect(lambda: Page201.Chrolis.ActivateChrolis(self,0))
    self.ui.Chrolis01_Slider.valueChanged.connect(lambda: Page201.Chrolis.GetChrolis(self,0))
    self.ui.Chrolis01_Slider.valueChanged.connect(lambda: Page201.PlayTestLED(self, 0))

    self.ui.Chrolis02_toggleButton.toggled.connect(lambda: Page201.Chrolis.ActivateChrolis(self,1))
    self.ui.Chrolis02_Slider.valueChanged.connect(lambda: Page201.Chrolis.GetChrolis(self,1))
    self.ui.Chrolis02_Slider.valueChanged.connect(lambda: Page201.PlayTestLED(self, 1))

    self.ui.Chrolis03_toggleButton.toggled.connect(lambda: Page201.Chrolis.ActivateChrolis(self,2))
    self.ui.Chrolis03_Slider.valueChanged.connect(lambda: Page201.Chrolis.GetChrolis(self,2))
    self.ui.Chrolis03_Slider.valueChanged.connect(lambda: Page201.PlayTestLED(self, 2))

    self.ui.Chrolis04_toggleButton.toggled.connect(lambda: Page201.Chrolis.ActivateChrolis(self,3))
    self.ui.Chrolis04_Slider.valueChanged.connect(lambda: Page201.Chrolis.GetChrolis(self,3))
    self.ui.Chrolis04_Slider.valueChanged.connect(lambda: Page201.PlayTestLED(self, 3))

    self.ui.Chrolis05_toggleButton.toggled.connect(lambda: Page201.Chrolis.ActivateChrolis(self,4))
    self.ui.Chrolis05_Slider.valueChanged.connect(lambda: Page201.Chrolis.GetChrolis(self,4))
    self.ui.Chrolis05_Slider.valueChanged.connect(lambda: Page201.PlayTestLED(self, 4))

    self.ui.Chrolis06_toggleButton.toggled.connect(lambda: Page201.Chrolis.ActivateChrolis(self,5))
    self.ui.Chrolis06_Slider.valueChanged.connect(lambda: Page201.Chrolis.GetChrolis(self,5))
    self.ui.Chrolis06_Slider.valueChanged.connect(lambda: Page201.PlayTestLED(self, 5))

    self.ui.Chrolis07_toggleButton.toggled.connect(lambda: Page201.Chrolis.ActivateChrolis(self,6))
    self.ui.Chrolis07_Slider.valueChanged.connect(lambda: Page201.Chrolis.GetChrolis(self,6))
    self.ui.Chrolis07_Slider.valueChanged.connect(lambda: Page201.PlayTestLED(self, 6))

    self.ui.Chrolis08_toggleButton.toggled.connect(lambda: Page201.Chrolis.ActivateChrolis(self,7))
    self.ui.Chrolis08_Slider.valueChanged.connect(lambda: Page201.Chrolis.GetChrolis(self,7))
    self.ui.Chrolis08_Slider.valueChanged.connect(lambda: Page201.PlayTestLED(self, 7))

    self.ui.Chrolis09_toggleButton.toggled.connect(lambda: Page201.Chrolis.ActivateChrolis(self,8))
    self.ui.Chrolis09_Slider.valueChanged.connect(lambda: Page201.Chrolis.GetChrolis(self,8))
    self.ui.Chrolis09_Slider.valueChanged.connect(lambda: Page201.PlayTestLED(self, 8))

    self.ui.Chrolis10_toggleButton.toggled.connect(lambda: Page201.Chrolis.ActivateChrolis(self,9))
    self.ui.Chrolis10_Slider.valueChanged.connect(lambda: Page201.Chrolis.GetChrolis(self,9))
    self.ui.Chrolis10_Slider.valueChanged.connect(lambda: Page201.PlayTestLED(self, 9))

    self.ui.Chrolis11_toggleButton.toggled.connect(lambda: Page201.Chrolis.ActivateChrolis(self,10))
    self.ui.Chrolis11_Slider.valueChanged.connect(lambda: Page201.Chrolis.GetChrolis(self,10))
    self.ui.Chrolis11_Slider.valueChanged.connect(lambda: Page201.PlayTestLED(self, 10))

    self.ui.Chrolis12_toggleButton.toggled.connect(lambda: Page201.Chrolis.ActivateChrolis(self,11))
    self.ui.Chrolis12_Slider.valueChanged.connect(lambda: Page201.Chrolis.GetChrolis(self,11))
    self.ui.Chrolis12_Slider.valueChanged.connect(lambda: Page201.PlayTestLED(self, 11))

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


