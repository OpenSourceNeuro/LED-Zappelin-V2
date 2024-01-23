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
    self.ui.LED_Display_lineEdit = [self.ui.LED01_Display_lineEdit,
                                    self.ui.LED02_Display_lineEdit,
                                    self.ui.LED03_Display_lineEdit,
                                    self.ui.LED04_Display_lineEdit,
                                    self.ui.LED05_Display_lineEdit,
                                    self.ui.LED06_Display_lineEdit,
                                    self.ui.LED07_Display_lineEdit,
                                    self.ui.LED08_Display_lineEdit,
                                    self.ui.LED09_Display_lineEdit,
                                    self.ui.LED10_Display_lineEdit,
                                    self.ui.LED11_Display_lineEdit,
                                    self.ui.LED12_Display_lineEdit
                                    ]

    self.ui.LED_toggleButton_layout = [self.ui.LED01_toggleButton_layout,
                                       self.ui.LED02_toggleButton_layout,
                                       self.ui.LED03_toggleButton_layout,
                                       self.ui.LED04_toggleButton_layout,
                                       self.ui.LED05_toggleButton_layout,
                                       self.ui.LED06_toggleButton_layout,
                                       self.ui.LED07_toggleButton_layout,
                                       self.ui.LED08_toggleButton_layout,
                                       self.ui.LED09_toggleButton_layout,
                                       self.ui.LED10_toggleButton_layout,
                                       self.ui.LED11_toggleButton_layout,
                                       self.ui.LED12_toggleButton_layout
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