from PySide6.QtWidgets import QFileDialog, QWidget
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter as savgol
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph import MultiPlotWidget
from pyqtgraph.metaarray import *
import pyqtgraph.exporters
import Settings
import Govardovski
from Colours import *
from LED_Zappelin import *

class Spectra():

    def ShowPage(self):
        self.ui.Main_stackedWidget.setCurrentWidget(self.ui.Spectra_Page)
        self.ui.Spectra_stackedWidget.setCurrentWidget(self.ui.OpsinSpectra_page)
        self.ui.OpsinSpectra_stackedWidget.setCurrentWidget(self.ui.Blank_page)
        self.ui.LEDSpectra_Display_stackedWidget.setCurrentWidget(self.ui.LEDSpectra_Blank_page)
        self.ui.OpsinSpectra_Load_comboBox.setCurrentIndex(0)
        self.ui.Spectra_plotWidget.setBackground(self.ui.DarkSolarized[0])

    def ChangeOpsinPage(self):
        self.OpsinIndex = self.ui.OpsinSpectra_Load_comboBox.currentIndex()
        self.ui.OpsinSpectra_stackedWidget.setCurrentIndex(self.OpsinIndex)

    def LoadData(self):
        FileName = QFileDialog.getOpenFileName(self,
                                               caption='Select recording file to load',
                                               dir=".\Spectra",
                                               filter='csv files (*.csv)'
                                               )
        self.ui.OpsinSpectra_Load_label.setText(FileName[0])
        self.ui.opsin = np.loadtxt(FileName[0],delimiter=",",dtype=float)



    def SetGraph(self):
        Theme(self)
        self.ui.Spectra_plotWidget.showGrid(x=True, y=True)
        self.ui.Spectra_plotWidget.setRange(yRange=[0, 1])
        self.ui.Spectra_plotWidget.setRange(xRange=[300, 650])
        self.ui.Spectra_plotWidget.setBackground(self.ui.DarkSolarized[0])
        self.ui.Spectra_plotWidget.setLabel('left', 'Normalised Opsin Absorbance')
        self.ui.Spectra_plotWidget.setLabel('bottom', 'Wavelength', 'nm')

    def SpectraBrush(self):
        self.SpectraIndex = self.ui.OpsinSpectra_Load_comboBox.currentIndex()
        for i in range(len(self.ui.Opsin_RGB[self.SpectraIndex-1])):
            self.ui.Spectra_Brush[self.SpectraIndex-1][i][0] = self.ui.Opsin_RGB[self.SpectraIndex-1][i][0]
            self.ui.Spectra_Brush[self.SpectraIndex-1][i][1] = self.ui.Opsin_RGB[self.SpectraIndex-1][i][1]
            self.ui.Spectra_Brush[self.SpectraIndex-1][i][2] = self.ui.Opsin_RGB[self.SpectraIndex-1][i][2]
            self.ui.Spectra_Brush[self.SpectraIndex-1][i][3] = 100


    def GenerateOpsin(self):
        self.SpectraIndex = self.ui.OpsinSpectra_Load_comboBox.currentIndex()
        self.ui.Spectra_plotWidget.clear()
        Spectra.SetGraph(self)
        Spectra.SpectraBrush(self)
        self.xSpectra = np.linspace(300,800,1000)
        for i in range(len(self.ui.Opsin_RGB[self.SpectraIndex-1])):
            if self.ui.Opsin_toggleButton[self.SpectraIndex-1][i].isChecked():
                self.ySpectra = Govardovski.Govardovski(self.ui.PeakWavelength[self.SpectraIndex-1][i])
                self.ui.Spectra_plotWidget.plot(self.xSpectra, self.ySpectra, fillLevel=0, brush=self.ui.Spectra_Brush[self.SpectraIndex-1][i], pen=self.ui.Spectra_Brush[self.SpectraIndex-1][i], width=50)

class LEDSpectra():

    def SelectFolder(self):
        self.FolderName = QFileDialog.getExistingDirectory(self,
                                                           caption='Select folder where spectrometer recordings are saved',
                                                           dir='./Spectrometer_Recording')

        self.ui.LEDSpectra_LoadData_label.setText(self.FolderName)

    def LoadData(self):
        self.LEDSpectraIndex = self.ui.LEDSpectra_Load_comboBox.currentIndex()

        if self.LEDSpectraIndex == 1:
            self.ui.LEDSpectra_Display_stackedWidget.setCurrentWidget(self.ui.Tetrachromatic_page)


    def SpectraBrush(self):
        self.LEDSpectraIndex = self.ui.LEDSpectra_Load_comboBox.currentIndex()
        for i in range(len(self.ui.LED_RGB[self.LEDSpectraIndex-1])):
            self.ui.LEDSpectra_Brush[self.LEDSpectraIndex-1][i][0] = self.ui.LED_RGB[self.LEDSpectraIndex-1][i][0]
            self.ui.LEDSpectra_Brush[self.LEDSpectraIndex-1][i][1] = self.ui.LED_RGB[self.LEDSpectraIndex-1][i][1]
            self.ui.LEDSpectra_Brush[self.LEDSpectraIndex-1][i][2] = self.ui.LED_RGB[self.LEDSpectraIndex-1][i][2]
            self.ui.LEDSpectra_Brush[self.LEDSpectraIndex-1][i][3] = 255

    def GenerateLEDSpectra(self):
        self.LEDSpectraIndex = self.ui.LEDSpectra_Load_comboBox.currentIndex()
        LEDSpectra.SpectraBrush(self)

        if self.LEDSpectraIndex == 1:
            nLED = 4
            nLoops = 5  # Number of recording loop (5 in the submitted example)
            nPoints = 100  # Number of recording point per LED (100 in the current example (from 1 to 100% light intensity with an increment of 1))
            SpectraNumber = nLoops * nLED * nPoints  # Total recording point number
            ExcludePoints = 7  # Number of point to discard at the end of recording
            FirstPoint = 33  # Start of the recording point in the csv file (33 in the submitted example)
            SpectraStart = 19  # First recording point (in our example: Spectrum000000019)
            lenSpectra = 9  # Length of the file string number (9 for ThorLab Spectrometer)

            self.spectrumPath = self.ui.LEDSpectra_LoadData_label.text()
            self.Spectra = []
            for j in range(0, SpectraNumber):
                FileNumber = str(SpectraStart + j)
                FileNumber = FileNumber.rjust(lenSpectra, '0')
                self.Spectrum_FileName = self.spectrumPath + '/Spectrum' + FileNumber + '.csv'
                self.a = np.asarray(pd.read_csv(self.Spectrum_FileName))[FirstPoint:-1, :].reshape(-1)
                self.a2 = np.asarray([self.a[i][17:] for i in range(self.a.shape[0])]).astype(float)
                self.Spectra.append(self.a2)
            self.Spectra = np.asarray(self.Spectra)
            self.WvsX = np.asarray([self.a[i][:16] for i in range(self.a.shape[0])]).astype(float)
            self.Spectra = self.Spectra.reshape(nLoops, nLED * nPoints, -1)
            self.Spectra = np.mean(self.Spectra, axis=0)


            savgolWindow = 61  # The length of the filter window
            savgolOrder = 2  # The order of the polynomial used to fit the samples.
            savgolDelta = 1  # The spacing of the samples to which the filter will be applied.

            Smoothed = savgol(self.Spectra, savgolWindow, savgolOrder, delta=savgolDelta, axis=-1)
            Smoothed = Smoothed.reshape(nLED, nPoints, -1)
            Smoothed = Smoothed[:, :-ExcludePoints, :]

            LEDNormalised = []
            LEDnormalised = []

            for i in range(nLED):
                LEDNorm = np.divide(Smoothed[i, nPoints - ExcludePoints - 1, :],np.amax(Smoothed[i, nPoints - ExcludePoints - 1, :]))
                LEDNormalised.append(LEDNorm)

                LEDnorm = np.copy(LEDNormalised[i])
                LEDnorm[LEDnorm < 0] = 0
                LEDnormalised.append(LEDnorm)

                self.ui.Spectra_plotWidget.plot(self.WvsX,LEDnormalised[i], fillLevel=0,
                                                brush=self.ui.LEDSpectra_Brush[0][3-i],
                                                pen=self.ui.LEDSpectra_Brush[0][3-i], width=50)
