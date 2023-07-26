
def Theme(self):
    self.ui.DarkSolarized = [[0, 30, 38], [0, 43, 54], [7, 54, 66],                                            # 0:DarkBase01, 1:DarkBase02, 2:DarkBase03
                            [220, 50, 47], [133, 153, 0], [38, 139, 210],                                     # 3:Red, 4:Green, 5:Blue
                            [203, 75, 22], [42, 161, 152], [181, 137, 0], [108, 113, 196], [211, 54, 130],    # 6:Orange, 7:Cyan, 8:Yellow, 9:Violet, 10:Magenta
                            [88, 110, 117], [101, 123, 131], [131, 148, 150], [147, 161, 161],                # 11:Content01, 12:Content02, 13:Content03, 14:Content04
                            [238, 232, 213],[253, 246, 227],                                                  # 15:LightBase01, 16:LightBase02
                            [0,153,176]]

def Wavelength_to_RGB(self, wavelength, gamma=0.8):
    wavelength = float(wavelength)

    if wavelength < 365:
        wavelength = 365.
    if wavelength > 780:
        wavelength = 780.
    if wavelength >= 365 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 365) / (440 - 365)
        R = ((-(wavelength - 440) / (440 - 365)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 780:
        attenuation = 0.3 + 0.7 * (780 - wavelength) / (780 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    return (R, G, B)


def LEDZap_Colours(self):
    self.ui.LEDZap_RGB = [[210,255,0],     # 565
                          [0,222,255],     # 482
                          [93,0,198],      # 411
                          [97,0,97],       # 361
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0]]



def Chrolis_Colours(self):
    self.ui.Chrolis_RGB = [[97,0,97],      # 365
                          [99,0,100],      # 366
                          [112,0,152],     # 389
                          [105,0,178],     # 401
                          [89,0,202],      # 413
                          [0,200,255],     # 477
                          [0,251,255],     # 489
                          [112,255,0],     # 535
                          [185,255,0],     # 557
                          [225,255,0],     # 570
                          [255,180,0],     # 603
                          [255,91,0]]      # 627

def Spectra_Colours(self):
    self.ui.Opsin_RGB = [
                         [
                          [75,0,216],
                          [94,255,0],
                          [195,255,0]
                         ],
                         [
                          [97,0,97],
                          [92,0,198],
                          [0,222,255],
                          [210,255,0]
                         ],
                         [
                          [86,0,206],
                          [0,97,255],
                          [0,255,40],
                          [228,255,0]
                         ]
                        ]

    self.ui.LED_RGB = [
                       [
                        [106,0,116],
                        [53,0,231],
                        [0,243,255],
                        [255,233,0]
                       ]
    ]

