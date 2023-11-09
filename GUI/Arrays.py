from LED_Zappelin import Ui_MainWindow
from Settings import *




def LEDZap_Arrays(self):
    self.ui.LEDZap_nLED = 4

    self.ui.LEDZap_LED_toggleButton = [self.ui.LED01_toggleButton,
                                       self.ui.LED02_toggleButton,
                                       self.ui.LED03_toggleButton,
                                       self.ui.LED04_toggleButton,
                                       self.ui.All_toggleButton
                                       ]

    self.ui.LEDZap_LED_Slider = [self.ui.LED01_Slider,
                                 self.ui.LED02_Slider,
                                 self.ui.LED03_Slider,
                                 self.ui.LED04_Slider,
                                 self.ui.All_LED_Slider
                                ]

    self.ui.LEDZap_LED_Value = [self.ui.LED01_Value,
                                self.ui.LED02_Value,
                                self.ui.LED03_Value,
                                self.ui.LED04_Value,
                                self.ui.All_LED_value
                                ]
    self.ui.LED_Display_lineEdit = [self.ui.LED01_Display_lineEdit,
                                    self.ui.LED02_Display_lineEdit,
                                    self.ui.LED03_Display_lineEdit,
                                    self.ui.LED04_Display_lineEdit
                                    ]

    self.ui.LED_toggleButton_layout = [self.ui.LED01_toggleButton_layout,
                                       self.ui.LED02_toggleButton_layout,
                                       self.ui.LED03_toggleButton_layout,
                                       self.ui.LED04_toggleButton_layout
                                       ]


    self.ui.LEDZap_Dataframe = ["LED01",
                                 "LED02",
                                 "LED03",
                                 "LED04"
                                 ]

    LEDZap_df_LED01 = None
    LEDZap_df_LED02 = None
    LEDZap_df_LED03 = None
    LEDZap_df_LED04 = None

    self.ui.LEDZap_Df = [LEDZap_df_LED01,
                          LEDZap_df_LED02,
                          LEDZap_df_LED03,
                          LEDZap_df_LED04
                          ]

    self.ui.LEDZap_Brush = [[0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]
                            ]

