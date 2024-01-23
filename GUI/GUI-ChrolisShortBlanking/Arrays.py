from LED_Zappelin import Ui_MainWindow
from Settings import *


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