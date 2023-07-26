from LED_Zappelin import Ui_MainWindow
from Settings import *




def LEDZap_Arrays(self):
    self.ui.LEDZap_nLED = 12

    self.ui.LEDZap_LED_toggleButton = [self.ui.LED01_toggleButton,
                                       self.ui.LED02_toggleButton,
                                       self.ui.LED03_toggleButton,
                                       self.ui.LED04_toggleButton,
                                       self.ui.LED05_toggleButton,
                                       self.ui.LED06_toggleButton,
                                       self.ui.LED07_toggleButton,
                                       self.ui.LED08_toggleButton,
                                       self.ui.LED09_toggleButton,
                                       self.ui.LED10_toggleButton,
                                       self.ui.LED11_toggleButton,
                                       self.ui.LED12_toggleButton,
                                       self.ui.All_toggleButton
                                       ]

    self.ui.LEDZap_LED_Slider = [self.ui.LED01_Slider,
                                 self.ui.LED02_Slider,
                                 self.ui.LED03_Slider,
                                 self.ui.LED04_Slider,
                                 self.ui.LED05_Slider,
                                 self.ui.LED06_Slider,
                                 self.ui.LED07_Slider,
                                 self.ui.LED08_Slider,
                                 self.ui.LED09_Slider,
                                 self.ui.LED10_Slider,
                                 self.ui.LED11_Slider,
                                 self.ui.LED12_Slider,
                                 self.ui.All_LED_Slider
                                ]

    self.ui.LEDZap_LED_Value = [self.ui.LED01_Value,
                                self.ui.LED02_Value,
                                self.ui.LED03_Value,
                                self.ui.LED04_Value,
                                self.ui.LED05_Value,
                                self.ui.LED06_Value,
                                self.ui.LED07_Value,
                                self.ui.LED08_Value,
                                self.ui.LED09_Value,
                                self.ui.LED10_Value,
                                self.ui.LED11_Value,
                                self.ui.LED12_Value,
                                self.ui.All_LED_value
                                ]

    self.ui.LEDZap_Dataframe = ["LED01",
                                 "LED02",
                                 "LED03",
                                 "LED04",
                                 "LED05",
                                 "LED06",
                                 "LED07",
                                 "LED08",
                                 "LED09",
                                 "LED10",
                                 "LED11",
                                 "LED12"
                                 ]

    LEDZap_df_LED01 = None
    LEDZap_df_LED02 = None
    LEDZap_df_LED03 = None
    LEDZap_df_LED04 = None
    LEDZap_df_LED05 = None
    LEDZap_df_LED06 = None
    LEDZap_df_LED07 = None
    LEDZap_df_LED08 = None
    LEDZap_df_LED09 = None
    LEDZap_df_LED10 = None
    LEDZap_df_LED11 = None
    LEDZap_df_LED12 = None

    self.ui.LEDZap_Df = [LEDZap_df_LED01,
                          LEDZap_df_LED02,
                          LEDZap_df_LED03,
                          LEDZap_df_LED04,
                          LEDZap_df_LED05,
                          LEDZap_df_LED06,
                          LEDZap_df_LED07,
                          LEDZap_df_LED08,
                          LEDZap_df_LED09,
                          LEDZap_df_LED10,
                          LEDZap_df_LED11,
                          LEDZap_df_LED12
                          ]

    self.ui.LEDZap_Brush = [[0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]
                            ]


def Chrolis_Arrays(self):
    self.ui.Chrolis_nLED = 12

    self.ui.Chrolis_LED_toggleButton = [self.ui.Chrolis01_toggleButton,
                                        self.ui.Chrolis02_toggleButton,
                                        self.ui.Chrolis03_toggleButton,
                                        self.ui.Chrolis04_toggleButton,
                                        self.ui.Chrolis05_toggleButton,
                                        self.ui.Chrolis06_toggleButton,
                                        self.ui.Chrolis07_toggleButton,
                                        self.ui.Chrolis08_toggleButton,
                                        self.ui.Chrolis09_toggleButton,
                                        self.ui.Chrolis10_toggleButton,
                                        self.ui.Chrolis11_toggleButton,
                                        self.ui.Chrolis12_toggleButton,
                                        self.ui.ChrolisAll_toggleButton
                                        ]

    self.ui.Chrolis_LED_Slider = [self.ui.Chrolis01_Slider,
                         self.ui.Chrolis02_Slider,
                         self.ui.Chrolis03_Slider,
                         self.ui.Chrolis04_Slider,
                         self.ui.Chrolis05_Slider,
                         self.ui.Chrolis06_Slider,
                         self.ui.Chrolis07_Slider,
                         self.ui.Chrolis08_Slider,
                         self.ui.Chrolis09_Slider,
                         self.ui.Chrolis10_Slider,
                         self.ui.Chrolis11_Slider,
                         self.ui.Chrolis12_Slider,
                         self.ui.ChrolisAll_LED_Slider
                         ]

    self.ui.Chrolis_LED_Value = [self.ui.Chrolis01_Value,
                         self.ui.Chrolis02_Value,
                         self.ui.Chrolis03_Value,
                         self.ui.Chrolis04_Value,
                         self.ui.Chrolis05_Value,
                         self.ui.Chrolis06_Value,
                         self.ui.Chrolis07_Value,
                         self.ui.Chrolis08_Value,
                         self.ui.Chrolis09_Value,
                         self.ui.Chrolis10_Value,
                         self.ui.Chrolis11_Value,
                         self.ui.Chrolis12_Value,
                         self.ui.ChrolisAll_LED_value
                         ]

    self.ui.Chrolis_Dataframe = ["LED01",
                                "LED02",
                                "LED03",
                                "LED04",
                                "LED05",
                                "LED06",
                                "LED07",
                                "LED08",
                                "LED09",
                                "LED10",
                                "LED11",
                                "LED12"
                                ]

    chrolis_df_LED01 = None
    chrolis_df_LED02 = None
    chrolis_df_LED03 = None
    chrolis_df_LED04 = None
    chrolis_df_LED05 = None
    chrolis_df_LED06 = None
    chrolis_df_LED07 = None
    chrolis_df_LED08 = None
    chrolis_df_LED09 = None
    chrolis_df_LED10 = None
    chrolis_df_LED11 = None
    chrolis_df_LED12 = None

    self.ui.Chrolis_Df = [chrolis_df_LED01,
                          chrolis_df_LED02,
                          chrolis_df_LED03,
                          chrolis_df_LED04,
                          chrolis_df_LED05,
                          chrolis_df_LED06,
                          chrolis_df_LED07,
                          chrolis_df_LED08,
                          chrolis_df_LED09,
                          chrolis_df_LED10,
                          chrolis_df_LED11,
                          chrolis_df_LED12
                          ]


    self.ui.Chrolis_Brush = [[0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]
                            ]

def Spectra_Arrays(self):
    self.ui.PeakWavelength = [
                              [420, 530, 560],        # human
                              [361, 411, 482, 565],   # zebrafish
                              [415, 455, 508, 571]    # chicken
                             ]


    self.ui.Opsin_toggleButton = [
                                  [self.ui.Human_Blue_toggleButton,
                                   self.ui.Human_Green_toggleButton,
                                   self.ui.Human_Red_toggleButton,
                                  ],
                                  [self.ui.Zebrafish_UV_toggleButton,
                                   self.ui.Zebrafish_Blue_toggleButton,
                                   self.ui.Zebrafish_Green_toggleButton,
                                   self.ui.Zebrafish_Red_toggleButton
                                  ],
                                  [self.ui.Chicken_UV_toggleButton,
                                   self.ui.Chicken_Blue_toggleButton,
                                   self.ui.Chicken_Green_toggleButton,
                                   self.ui.Chicken_Red_toggleButton
                                  ],
                                 ]



    self.ui.Spectra_Brush = [
                             [
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                             ],
                             [
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0]
                             ],
                             [
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0]
                             ]
                            ]

    self.ui.LEDSpectra_Brush = [
                                [
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0]
                                ],
                                [
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0]
                                ],
                                [
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0]
                                ]
                               ]





