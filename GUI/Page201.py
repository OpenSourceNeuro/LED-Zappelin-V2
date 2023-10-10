from PySide6 import QtCore, QtGui, QtWidgets, QtSerialPort
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtWidgets import QFileDialog, QWidget
from PySide6.QtCore import QIODevice, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QCoreApplication, QFileInfo
import pyqtgraph as pg

import Settings
from SerialMonitor import *
from Colours import *
from Arrays import *

import serial
import os
import time
import numpy as np
import pandas as pd
from sys import platform

portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
        if platform == "linux" or platform == "linux2":
            portList.append(port.systemLocation())
        else:
            portList.append(port.portName())


class Chrolis():

    def ShowPage(self):
        self.ui.Main_stackedWidget.setCurrentWidget(self.ui.Chrolis_Page)
        self.ui.Chrolis_Display_stackedWidget.setCurrentWidget(self.ui.Chrolis_Display_page1)


    # Serial Port Functions
    def ChangePort(self):
        self.COM = self.ui.Chrolis_SelectPortComboBox.currentText()
        self.BaudRate = self.ui.BaudRate
        self.serial_port = serial.Serial(self.COM, self.BaudRate)
        if self.serial_port.is_open:
            self.ui.Chrolis_ConnectButton.setEnabled(True)
            self.ui.Chrolis_SerialFlag = True
            self.serial_port.close()
            self.ui.Chrolis_Serial_label.setText('COM port ' + str(self.COM) + ' selected. Now click on the "Connect Chrolis" button')
        else:
            self.ui.Chrolis_Serial_label.setText('Nope! try another COM port')

    def ConnectSerial(self):
        if self.ui.Chrolis_SerialFlag == True:
            self.ui.Chrolis_ConnectFlag = False
            self.COM = self.ui.Chrolis_SelectPortComboBox.currentText()
            self.BaudRate = self.ui.BaudRate
            self.serial_port = serial.Serial(port=self.COM, baudrate=self.BaudRate)
            self.ui.Chrolis_ConnectButton.setText("Connected")
            self.ui.Chrolis_Serial_label.setText('LED Zappelin connected')
            self.ui.Chrolis_ConnectButton.setStyleSheet("color: rgb" + str(tuple(self.ui.DarkSolarized[3])) + ";\n"
                                                        "background-color: rgb" + str(tuple(self.ui.DarkSolarized[11])) + ";\n"
                                                        "border: 1px solid rgb" + str(tuple(self.ui.DarkSolarized[14])) + ";\n"
                                                        "border-radius: 10px;"
                                                        )
            self.ui.Chrolis_SerialFlag = False

        else:
            self.ui.Chrolis_Serial_label.setText('Select a COM port first, preferably the one to which LED Zappelin is connected')

        if self.ui.Chrolis_ConnectFlag == True:
            self.serial_port.close()
            self.ui.Chrolis_ConnectFlag = False
            self.ui.Chrolis_SerialFlag = True
            self.ui.Chrolis_ConnectButton.setText("Disconnected")
            self.ui.Chrolis_Serial_label.setText('LED Zappelin disconnected')

            self.ui.Chrolis_ConnectButton.setStyleSheet("color: rgb" + str(tuple(self.ui.DarkSolarized[14])) + ";\n"
                                                       "background-color: rgb" + str(tuple(self.ui.DarkSolarized[2])) + ";\n"
                                                       "border: 1px solid rgb" + str(tuple(self.ui.DarkSolarized[14])) + ";\n"
                                                       "border-radius: 10px;"
                                                       )


    def ActivateChrolisAll(self):
        if self.ui.ChrolisAll_toggleButton.isChecked():
            self.ChrolisAll_LED_Val = self.ui.ChrolisAll_LED_Slider.value()
            for i in range (self.ui.Chrolis_nLED+1):
                self.ui.Chrolis_LED_toggleButton[i].setChecked(True)
                self.ui.Chrolis_LED_Slider[i].setEnabled(True)
                self.ui.Chrolis_LED_Slider[i].setValue(self.ChrolisAll_LED_Val)
                self.ui.Chrolis_LED_Value[i].setText(str(self.ChrolisAll_LED_Val) + ' %')

            if self.serial_port.is_open:
                pass
            else:
                self.ui.Chrolis_Serial_label.setText('LED Zappelin is not connected: LED value change will not be applied')

        else:
            for i in range (self.ui.Chrolis_nLED+1):
                self.ui.Chrolis_LED_toggleButton[i].setChecked(False)
                self.ui.Chrolis_LED_Slider[i].setEnabled(False)
                self.ui.Chrolis_LED_Value[i].setText('')

            if self.serial_port.is_open:
                pass
            else:
                self.ui.Chrolis_Serial_label.setText('LED Zappelin is not connected: LED value change will not be applied')


    def ActivateChrolis(self,i):
        if self.ui.Chrolis_LED_toggleButton[i].isChecked():
            self.ui.Chrolis_LED_Slider[i].setEnabled(True)
            self.Chrolis_LED_val = self.ui.Chrolis_LED_Slider[i].value()
            self.ui.Chrolis_LED_Value[i].setText(str(self.Chrolis_LED_val) + ' %')
            if self.serial_port.is_open:
                self.serial_port.write(str('L' + str(i + 1) + (' ') + str(self.ChrolisAll_LED_Val) + '\n').encode('utf-8'))
                time.sleep(0.01)
            else:
                self.ui.Chrolis_Serial_label.setText('LED Zappelin is not connected: LED value change will not be applied')
        else:
            self.ui.Chrolis_LED_Slider[i].setEnabled(False)
            self.ui.Chrolis_LED_Value[i].setText('')
            if self.serial_port.is_open:
                pass
            else:
                self.ui.Chrolis_Serial_label.setText('LED Zappelin is not connected: LED value change will not be applied')


    def GetChrolisAll(self):
        self.ui.GetChrolisFlag = False
        self.ChrolisAll_LED_Val = self.ui.ChrolisAll_LED_Slider.value()
        for i in range (self.ui.Chrolis_nLED+1):
            self.ui.Chrolis_LED_Slider[i].setValue(self.ChrolisAll_LED_Val)
            self.ui.Chrolis_LED_Value[i].setText(str(self.ChrolisAll_LED_Val) + ' %')
            if self.serial_port.is_open:
                self.serial_port.write(str('L' + str(i + 1) + (' ') + str(self.ChrolisAll_LED_Val) + '\n').encode('utf-8'))
                time.sleep(0.01)
            else:
                self.ui.Chrolis_Serial_label.setText('LED Zappelin is not connected: LED value change will not be applied')

        self.ui.GetChrolisFlag = True


    def GetChrolis(self,i):
        if self.ui.GetChrolisFlag == True:
            self.Chrolis_Val = self.ui.Chrolis_LED_Slider[i].value()
            self.ui.Chrolis_LED_Value[i].setText(str(self.Chrolis_Val) + ' %')
            if self.serial_port.is_open:
                self.serial_port.write(str('L' + str(i + 1) + (' ') + str(self.Chrolis_Val) + '\n').encode('utf-8'))
            else:
                self.ui.Chrolis_Serial_label.setText('LED Zappelin is not connected: LED value change will not be applied')


    def DeactivateLED(self,i):
        if self.ui.Chrolis_LED_toggleButton[i].isChecked() == False:
            self.ui.Chrolis_LED_Slider[i].setValue(0)
            self.ui.Chrolis_LED_Value[i].setText('Off')


    def DeactivateAllLED(self):
        if self.ui.ChrolisAll_toggleButton.isChecked() == False:
            for i in range(self.ui.Chrolis_nLED + 1):
                self.ui.Chrolis_LED_Slider[i].setValue(0)
                self.ui.Chrolis_LED_Value[i].setText('Off')






def PlayStimuli(self):
    self.currentLoop = 1
    self.Stim = []
    self.Data = 0

    def ReadStimulus(self):
        if self.ui.Chrolis_StimulusFlag == True:
            FileName = self.ui.Chrolis_Stimulus_Label.text()

            Df = pd.read_csv(FileName)
            for i in range (self.ui.Chrolis_nLED):
                self.ui.Chrolis_Df[i] = Df[self.ui.Chrolis_Dataframe[i]]
                self.Stim.append(self.ui.Chrolis_Df[i])

            self.df_StimRes = Df["Resolution"]
            self.df_nEntries = Df["nEntries"]
            self.df_Trigger = Df["Trigger"]
            self.df_PreAdapt = Df["PreAdaptation"]

            self.Stim.append(self.df_StimRes)
            self.Stim.append(self.df_nEntries)
            self.Stim.append(self.df_Trigger)
            self.Stim.append(self.df_PreAdapt)

            return self.Stim

        else:
            self.ui.Chrolis_Serial_label.setText('Load a stimulus to play first')

    self.Stim = ReadStimulus(self)



    def SetTriggerMode(self):
        self.TriggerMode = int(self.Stim[14][0])

        if self.TriggerMode == 0:
            self.serial_port.write(str('M ' + str(self.TriggerMode) + '\n').encode('utf-8'))

        elif self.TriggerMode > 0:
            self.serial_port.write(str('M ' + str(self.TriggerMode) + '\n').encode('utf-8'))


    def SetTrigger(self):
        self.TriggerMode = int(self.Stim[14][0])

        if self.TriggerMode > 0:
            self.TriggerString = ""
            for i in range(self.TriggerMode):
                self.TriggerString += ' ' + str(int(self.Stim[14][i+1]))
            self.serial_port.write(str('T' + self.TriggerString + '\n').encode('utf-8'))
        elif self.TriggerMode == 0:
            pass


    def SetStimulus(self):
        self.serial_port.write(str('S ' + str(self.Stim[12][0]) + ' '
                                   + str(self.Stim[13][0]) + ' '
                                   + str(self.Stim[15][0]) + ' '
                                   + '\n').encode('utf-8'))

        for i in range(self.ui.Chrolis_nLED):
            Chrolis.GetChrolis(self,i)

    def SetNumberofLoop(self):
        self.ui.NumberofLoop = int(self.ui.Chrolis_NumbeofLoop.text())

    if self.ui.Chrolis_StimulusFlag:
        SetTriggerMode(self)
        SetTrigger(self)
        SetStimulus(self)
        SetNumberofLoop(self)
        self.ui.Chrolis_PlayingFlag = True
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: PlayStimulus(self))
        self.timer.start()


    def PlayStimulus(self):
        if self.ui.Chrolis_StimulusFlag == True:
            if self.ui.Chrolis_PlayingFlag == True:
                self.ui.Chrolis_PlayingFlag = False
                self.ui.Chrolis_StartStimulusFlag = True
                self.ui.Chrolis_Serial_label.setText("Playing Stimulus: Loop 0")
                self.ui.Chrolis_Start_pushButton.setStyleSheet("color: rgb(250, 250, 250);\n"
                                                               "background-color: rgb(220, 50, 47);")
        else:
            self.ui.Chrolis_Serial_label.setText('Load a stimulus to play first')


        if self.ui.Chrolis_StartStimulusFlag == True:
            self.serial_port.write(str('P1 ' + str(self.Stim[0][int(self.Data)]) + ' '
                                       + str(self.Stim[1][int(self.Data)]) + ' '
                                       + str(self.Stim[2][int(self.Data)]) + ' '
                                       + str(self.Stim[3][int(self.Data)]) + ' '
                                       + '\n').encode('utf-8'))
            self.serial_port.write(str('P2 ' + str(self.Stim[4][int(self.Data)]) + ' '
                                       + str(self.Stim[5][int(self.Data)]) + ' '
                                       + str(self.Stim[6][int(self.Data)]) + ' '
                                       + str(self.Stim[7][int(self.Data)]) + ' '
                                       + '\n').encode('utf-8'))
            self.serial_port.write(str('P3 ' + str(self.Stim[8][int(self.Data)]) + ' '
                                       + str(self.Stim[9][int(self.Data)]) + ' '
                                       + str(self.Stim[10][int(self.Data)]) + ' '
                                       + str(self.Stim[11][int(self.Data)]) + ' '
                                       + '\n').encode('utf-8'))
            self.serial_port.write(str('P' + '\n').encode('utf-8'))

            self.Data = ReadSerial(self)

            if int(self.Data) == 1:
                self.ui.Chrolis_Serial_label.setText("Playing Stimulus: Loop " + str(self.currentLoop))
                self.currentLoop = self.currentLoop + 1

            if self.ui.NumberofLoop > 0:
                if self.currentLoop == self.ui.NumberofLoop + 2:
                    StopStimulus(self)




    # Read Serial and return data
    def ReadSerial(self):
        self.rx = self.serial_port.readline()
        self.rx_serial = str(self.rx, 'utf8')
        return self.rx_serial


def LoadStimulus(self):
    self.ui.Chrolis_StimulusFlag = True
    self.FileName, _ = QFileDialog.getOpenFileName(self,
                                           caption='Select a stimulus',
                                           dir="./Stimuli",
                                           filter='csv files (*.csv)'
                                           )

    self.ui.Chrolis_Stimulus_Label.setText(self.FileName)



def StopStimulus(self):
    if self.ui.Chrolis_StartStimulusFlag == True:
        self.ui.Chrolis_StartStimulusFlag = False
        self.ui.Chrolis_Start_pushButton.setStyleSheet("color: rgb(147, 161, 161);\n"
                                                       "background-color: rgb(7, 54, 66);")

        self.serial_port.write(('O '+ '\n').encode('utf-8'))
        self.ui.Chrolis_Serial_label.setText('Stimulus stopped')

    else:
        self.ui.Chrolis_Serial_label.setText('No stimulus to stop at the moment')


class Chrolis_Stimuli():

    def SetGraph(self):
        Theme(self)
        self.ui.Chrolis_Display1.showGrid(x=True,y=True)
        self.ui.Chrolis_Display1.setRange(yRange=[0,100])
        self.ui.Chrolis_Display1.setBackground(self.ui.DarkSolarized[0])
        self.ui.Chrolis_Display1.setLabel('left', 'Stimulus Intensity', 'a.u.')
        self.ui.Chrolis_Display1.setLabel('bottom', 'time', 'ms')


    def DrawGraph(self):
        if self.ui.Chrolis_StimulusFlag == True:
            self.ui.Chrolis_Display1.clear()

            Chrolis_Stimuli.ChrolisBrush(self)

            self.FileName = self.ui.Chrolis_Stimulus_Label.text()
            self.Df = pd.read_csv(self.FileName)
            self.Resolution = self.Df["Resolution"][0] / 1000
            self.nEntries = self.Df["nEntries"][0]
            self.xStim = np.linspace(0,int(self.nEntries)*int(self.Resolution),int(self.nEntries))


            for i in range(self.ui.Chrolis_nLED):
                if self.ui.Chrolis_LED_toggleButton[i].isChecked():
                    self.yStim = self.Df[self.ui.Chrolis_Dataframe[i]]
                    self.ui.Chrolis_Display1.plot(self.xStim,self.yStim,fillLevel=-0.3,brush=self.ui.Chrolis_Brush[i])



            self.ui.Chrolis_LED_counter = 0
            self.ui.Chrolis_LED_Index = []
            for i in range(self.ui.Chrolis_nLED):
                if self.ui.Chrolis_LED_toggleButton[i].isChecked():
                    self.ui.Chrolis_LED_counter += 1
                    self.ui.Chrolis_LED_Index.append(i)

            def clearLayout(layout):
                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()

            clearLayout(self.ui.Chrolis_Display2_Layout)

            for i in range(self.ui.Chrolis_LED_counter):
                self.ui.Chrolis_Graph = pg.PlotWidget()
                self.ui.Chrolis_Graph.showGrid(x=True, y=True)
                self.ui.Chrolis_Graph.setRange(yRange=[0, 100])
                self.ui.Chrolis_Graph.setBackground(self.ui.DarkSolarized[0])
                self.Chrolis_Curve = pg.PlotCurveItem()
                self.ui.Chrolis_Graph.addItem(self.Chrolis_Curve)
                self.ui.Chrolis_Display2_Layout.addWidget(self.ui.Chrolis_Graph)
                self.yStim = self.Df[self.ui.Chrolis_Dataframe[self.ui.Chrolis_LED_Index[i]]]
                self.ui.Chrolis_Graph.plot(self.xStim, self.yStim, fillLevel=-0.3, brush=self.ui.Chrolis_Brush[self.ui.Chrolis_LED_Index[i]])

        else:
            self.ui.Chrolis_Serial_label.setText('Load a stimulus to display first')


    def ChrolisBrush(self):
        for i in range (self.ui.Chrolis_nLED):
            self.transparency = self.ui.Chrolis_LED_Slider[i].value()
            self.ui.Chrolis_Brush[i][0] = self.ui.Chrolis_RGB[i][0]
            self.ui.Chrolis_Brush[i][1] = self.ui.Chrolis_RGB[i][1]
            self.ui.Chrolis_Brush[i][2] = self.ui.Chrolis_RGB[i][2]
            self.ui.Chrolis_Brush[i][3] = self.transparency*2


def ChrolisLoadPreSet(self):
    self.FileName, _ = QFileDialog.getOpenFileName(self,
                                           caption='Select a LED settings file',
                                           dir="./LED_Settings",
                                           filter='csv files (*.csv)'
                                           )
    self.ui.Chrolis_Preselect_Label.setText(self.FileName)

def ChrolisApplyPreSet(self):
    self.FileName = self.ui.Chrolis_Preselect_Label.text()
    self.Df_PreSelect = pd.read_csv(self.FileName)
    self.ui.Chrolis01_Slider.setValue(self.Df_PreSelect["LED01"][0])
    self.ui.Chrolis02_Slider.setValue(self.Df_PreSelect["LED02"][0])
    self.ui.Chrolis03_Slider.setValue(self.Df_PreSelect["LED03"][0])
    self.ui.Chrolis04_Slider.setValue(self.Df_PreSelect["LED04"][0])
    self.ui.Chrolis05_Slider.setValue(self.Df_PreSelect["LED05"][0])
    self.ui.Chrolis06_Slider.setValue(self.Df_PreSelect["LED06"][0])
    self.ui.Chrolis07_Slider.setValue(self.Df_PreSelect["LED07"][0])
    self.ui.Chrolis08_Slider.setValue(self.Df_PreSelect["LED08"][0])
    self.ui.Chrolis09_Slider.setValue(self.Df_PreSelect["LED09"][0])
    self.ui.Chrolis10_Slider.setValue(self.Df_PreSelect["LED10"][0])
    self.ui.Chrolis11_Slider.setValue(self.Df_PreSelect["LED11"][0])
    self.ui.Chrolis12_Slider.setValue(self.Df_PreSelect["LED12"][0])



def SetChrolisBrightness(self):
    self.ProxyLED_value = self.ui.Chrolis_ProxyLED_Slider.value()

    self.ProxyLED_Value = int(self.ProxyLED_value / 255 * 100)
    self.ui.Chrolis_ProxyLED_value.setText(str(self.ProxyLED_Value) + ' %')
    self.ui.Chrolis_Serial_label.setText('Proxy LED brightness changed to ' + str(self.ProxyLED_Value) + '%')


    self.serial_port.write(str('B ' + str(self.ProxyLED_value)
                               + '\n').encode('utf-8'))


def TestLED(self):
    for i in range(self.ui.Chrolis_nLED):

        self.Chrolis_Val = self.ui.Chrolis_LED_Slider[i].value()
        if self.serial_port.is_open:
            self.serial_port.write(str('T' + str(i + 1) + (' ') + str(self.Chrolis_Val) + '\n').encode('utf-8'))
            print(str('T' + str(i + 1) + (' ') + str(self.Chrolis_Val) ))
            time.sleep(0.01)
        else:
            self.ui.Chrolis_Serial_label.setText('LED Zappelin is not connected: LEDs will not light up')

