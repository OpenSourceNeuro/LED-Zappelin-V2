import numpy as np

def Govardovski(PeakWavelength):
    Wavelength = np.linspace(300,800,1000)

    ##### AlphaBand ######
    A = 69.7
    a = 0.8795 + 0.0459 * np.exp(-np.square(PeakWavelength - 300) / 11940)
    B = 28
    b = 0.922
    C = -14.9
    c = 1.104
    D = 0.674
    x = PeakWavelength / Wavelength
    alphaband = 1 / (np.exp(A * (a - x)) + np.exp(B * (b - x)) + np.exp(C * (c - x)) + D)

    ##### BetaBand ######
    Ab = 0.26  # Beta value at peak
    b = -40.5 + 0.195 * PeakWavelength  # Beta bandwidth
    Lambda = 189 + 0.315 * PeakWavelength  # Beta peak
    betaband = Ab * np.exp(-1 * ((Wavelength - Lambda) / b) ** 2)
    return alphaband + betaband


