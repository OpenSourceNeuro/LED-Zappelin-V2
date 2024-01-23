#include "General_Settings.h"
#include <SerialCommand.h>   // SerialCommand Library by Steven Cogswell https://github.com/shyd/Arduino-SerialCommand
SerialCommand SCmd;


/* ----------------------------------------------------------------------------------*/
/* -------------------------------- Turn all LED off --------------------------------*/
void LED_Off(){
  for (int l = 0; l <= nLED-1; l++) {
    tlc.setPWM(LED_Array[l],0);                        
    strip.setPixelColor(l,strip.ColorHSV(hsv_hue_Array[l],hsv_sat_Array[l],0));
  } 
  tlc.write();   
  strip.show();  
}


/* ----------------------------------------------------------------------------------*/
/* -------------------------------- Turn all LED on -----------------/---------------*/
void LED_On(){
  for (int l = 0; l <= nLED-1; l++) {
    tlc.setPWM(LED_Array[l],100);                        
    strip.setPixelColor(l,strip.ColorHSV(hsv_hue_Array[l],hsv_sat_Array[l],100));
  } 
  tlc.write();   
  strip.show();  
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------- Inititate new stimulation sequence -----------------------*/
void SetTriggerMode(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    TriggerMode = aNumber;
  }

  if (TriggerMode == 0){
    TriggerModeFlag = false;
  }

  if (TriggerMode > 0){
    TriggerModeFlag = true;
  }
}

void SetTrigger(){ 
  if (TriggerMode > 0){
    for (int trig = 0; trig <= TriggerMode-1; trig++){
      arg = SCmd.next();
      if (arg != NULL){
        aNumber = atoi(arg);
        TriggerArray[trig] = aNumber; 
      }
    }
  }
  TriggerTime = TriggerArray[tr]; 
}

void SetStimulus(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    ResolutionMicros = aNumber;
  }
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    iLoop = aNumber;
  }
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    PreAdaptMicros = aNumber;
  }

  i = 1;
  t = 0;
  td = 0;
  tr = 0;
  PreAdaptationFlag = true;

  PreviousMicros = micros();
  tPreviousMicros = micros();
  tdPreviousMicros = micros();


  tdDiffMicros = 0;
  
  TriggerFlag = true;  
  StimulusFlag = true;
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------- Play stimulation sequence ---------------------------*/
void Stimulus1(){
  for (int l = 0; l <= 3; l++) {
    arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower[l] = aNumber;
    } 
    tlc.setPWM(LED_Array[l],LEDPower_Array[l]*LEDPower_Array2[l]/100*LEDPower[l]/100);   
    strip.setPixelColor(l,strip.ColorHSV(hsv_hue_Array[l],hsv_sat_Array[l],hsv_val_Array[l]*LEDPower_Array2[l]/100*LEDPower[l]/100));
  }
}


void Stimulus2(){
  for (int l = 4; l <= 7; l++) {
    arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower[l] = aNumber;
    } 
    tlc.setPWM(LED_Array[l],LEDPower_Array[l]*LEDPower_Array2[l]/100*LEDPower[l]/100);   
    strip.setPixelColor(l,strip.ColorHSV(hsv_hue_Array[l],hsv_sat_Array[l],hsv_val_Array[l]*LEDPower_Array2[l]/100*LEDPower[l]/100));
  }
}


void Stimulus3(){
  for (int l = 8; l <= 11; l++) {
    arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower[l] = aNumber;
    } 
    tlc.setPWM(LED_Array[l],LEDPower_Array[l]*LEDPower_Array2[l]/100*LEDPower[l]/100);   
    strip.setPixelColor(l,strip.ColorHSV(hsv_hue_Array[l],hsv_sat_Array[l],hsv_val_Array[l]*LEDPower_Array2[l]/100*LEDPower[l]/100));
  }
}


void Stimulus(){
  tlc.write();   
  strip.show();  
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------- Stop stimulation sequence ---------------------------*/
void StopStimulus(){
  StimulusFlag = false;
  LED_Off();
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------------- Set LED 01 ------------------------------------*/
void LED01(){
  float aNumber;
  char *arg;
  
  arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower_Array2[0] = aNumber;
    }
}

/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Test LED 01 ----------------------------------*/
void Test1(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    LEDPower[0] = aNumber;
  }

  tlc.setPWM(LED_Array[0],LEDPower_Array[0]*LEDPower[0]/100);   
  strip.setPixelColor(0,strip.ColorHSV(hsv_hue_Array[0],hsv_sat_Array[0],hsv_val_Array[0]*LEDPower[0]/100));
  tlc.write();   
  strip.show();
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------------- Set LED 02 ------------------------------------*/
void LED02(){
  float aNumber;
  char *arg;
  
  arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower_Array2[1] = aNumber;
    }
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Test LED 02 ----------------------------------*/
void Test2(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    LEDPower[1] = aNumber;
  }

  tlc.setPWM(LED_Array[1],LEDPower_Array[1]*LEDPower[1]/100);   
  strip.setPixelColor(1,strip.ColorHSV(hsv_hue_Array[1],hsv_sat_Array[1],hsv_val_Array[1]*LEDPower[1]/100));
  tlc.write();   
  strip.show();
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------------- Set LED 03 ------------------------------------*/
void LED03(){
  float aNumber;
  char *arg;
  
  arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower_Array2[2] = aNumber;
    }
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Test LED 03 ----------------------------------*/
void Test3(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    LEDPower[2] = aNumber;
  }

  tlc.setPWM(LED_Array[2],LEDPower_Array[2]*LEDPower[2]/100);   
  strip.setPixelColor(2,strip.ColorHSV(hsv_hue_Array[2],hsv_sat_Array[2],hsv_val_Array[2]*LEDPower[2]/100));
  tlc.write();   
  strip.show();
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------------- Set LED 04 ------------------------------------*/
void LED04(){
  float aNumber;
  char *arg;
  
  arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower_Array2[3] = aNumber;
    }
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Test LED 04 ----------------------------------*/
void Test4(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    LEDPower[3] = aNumber;
  }

  tlc.setPWM(LED_Array[3],LEDPower_Array[3]*LEDPower[3]/100);   
  strip.setPixelColor(3,strip.ColorHSV(hsv_hue_Array[3],hsv_sat_Array[3],hsv_val_Array[3]*LEDPower[3]/100));
  tlc.write();   
  strip.show();
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------------- Set LED 05 ------------------------------------*/
void LED05(){
  float aNumber;
  char *arg;
  
  arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower_Array2[4] = aNumber;
    }
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Test LED 05 ----------------------------------*/
void Test5(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    LEDPower[4] = aNumber;
  }

  tlc.setPWM(LED_Array[4],LEDPower_Array[4]*LEDPower[4]/100);   
  strip.setPixelColor(4,strip.ColorHSV(hsv_hue_Array[4],hsv_sat_Array[4],hsv_val_Array[4]*LEDPower[4]/100));
  tlc.write();   
  strip.show();
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------------- Set LED 06 ------------------------------------*/
void LED06(){
  float aNumber;
  char *arg;
  
  arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower_Array2[5] = aNumber;
    }
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Test LED 06 ----------------------------------*/
void Test6(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    LEDPower[5] = aNumber;
  }

  tlc.setPWM(LED_Array[5],LEDPower_Array[5]*LEDPower[5]/100);   
  strip.setPixelColor(5,strip.ColorHSV(hsv_hue_Array[5],hsv_sat_Array[5],hsv_val_Array[5]*LEDPower[5]/100));
  tlc.write();   
  strip.show();
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------------- Set LED 07 ------------------------------------*/
void LED07(){
  float aNumber;
  char *arg;
  
  arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower_Array2[6] = aNumber;
    }
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Test LED 07 ----------------------------------*/
void Test7(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    LEDPower[6] = aNumber;
  }

  tlc.setPWM(LED_Array[6],LEDPower_Array[6]*LEDPower[6]/100);   
  strip.setPixelColor(6,strip.ColorHSV(hsv_hue_Array[6],hsv_sat_Array[6],hsv_val_Array[6]*LEDPower[6]/100));
  tlc.write();   
  strip.show();
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------------- Set LED 08 ------------------------------------*/
void LED08(){
  float aNumber;
  char *arg;
  
  arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower_Array2[7] = aNumber;
    }
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Test LED 08 ----------------------------------*/
void Test8(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    LEDPower[7] = aNumber;
  }

  tlc.setPWM(LED_Array[7],LEDPower_Array[7]*LEDPower[7]/100);   
  strip.setPixelColor(7,strip.ColorHSV(hsv_hue_Array[7],hsv_sat_Array[7],hsv_val_Array[7]*LEDPower[7]/100));
  tlc.write();   
  strip.show();
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------------- Set LED 09 ------------------------------------*/
void LED09(){
  float aNumber;
  char *arg;
  
  arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower_Array2[8] = aNumber;
    }
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Test LED 09 ----------------------------------*/
void Test9(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    LEDPower[8] = aNumber;
  }

  tlc.setPWM(LED_Array[8],LEDPower_Array[8]*LEDPower[8]/100);   
  strip.setPixelColor(8,strip.ColorHSV(hsv_hue_Array[8],hsv_sat_Array[8],hsv_val_Array[8]*LEDPower[8]/100));
  tlc.write();   
  strip.show();
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------------- Set LED 10 ------------------------------------*/
void LED10(){
  float aNumber;
  char *arg;
  
  arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower_Array2[9] = aNumber;
    }
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Test LED 10 ----------------------------------*/
void Test10(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    LEDPower[9] = aNumber;
  }

  tlc.setPWM(LED_Array[9],LEDPower_Array[9]*LEDPower[9]/100);   
  strip.setPixelColor(9,strip.ColorHSV(hsv_hue_Array[9],hsv_sat_Array[9],hsv_val_Array[9]*LEDPower[9]/100));
  tlc.write();   
  strip.show();
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------------- Set LED 11 ------------------------------------*/
void LED11(){
  float aNumber;
  char *arg;
  
  arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower_Array2[10] = aNumber;
    }
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Test LED 11 ----------------------------------*/
void Test11(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    LEDPower[10] = aNumber;
  }

  tlc.setPWM(LED_Array[10],LEDPower_Array[10]*LEDPower[10]/100);   
  strip.setPixelColor(10,strip.ColorHSV(hsv_hue_Array[10],hsv_sat_Array[10],hsv_val_Array[10]*LEDPower[10]/100));
  tlc.write();   
  strip.show();
}


/* ----------------------------------------------------------------------------------*/
/* ---------------------------------- Set LED 12 ------------------------------------*/
void LED12(){
  float aNumber;
  char *arg;
  
  arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      LEDPower_Array2[11] = aNumber;
    }
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Test LED 12 ----------------------------------*/
void Test12(){
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    LEDPower[1] = aNumber;
  }

  tlc.setPWM(LED_Array[11],LEDPower_Array[11]*LEDPower[11]/100);   
  strip.setPixelColor(11,strip.ColorHSV(hsv_hue_Array[11],hsv_sat_Array[11],hsv_val_Array[11]*LEDPower[11]/100));
  tlc.write();   
  strip.show();  
}


/* ----------------------------------------------------------------------------------*/
/* --------------------------- Set Proxy LEDs brightness ----------------------------*/
void Brightness(){
  int aNumber;
  char *arg;
  
  arg = SCmd.next();
    if (arg != NULL){
      aNumber = atoi(arg);
      brightness = aNumber;
    }
  strip.setBrightness(brightness); // Set NeoPixel brightness 
}

/* ----------------------------------------------------------------------------------*/
/* ------------------------------- Set NeoPixel LEDs --------------------------------*/
void SetNeoPixelColours(){
  for (int l = 0; l <= nLED-1; l++) {
    strip.setPixelColor(l,strip.ColorHSV(hsv_hue_Array[l],hsv_sat_Array[l],hsv_val_Array[l]));
    strip.show();
    delay(50);
  }
  strip.show();
  delay(500);
  LED_Off();
}

void SCmdAddCommand(){
  SCmd.addCommand("P", Stimulus);
  SCmd.addCommand("P1", Stimulus1);
  SCmd.addCommand("P2", Stimulus2);
  SCmd.addCommand("P3", Stimulus3);
  SCmd.addCommand("S", SetStimulus);
  SCmd.addCommand("M", SetTriggerMode);
  SCmd.addCommand("T", SetTrigger);
  SCmd.addCommand("O", StopStimulus);
  SCmd.addCommand("L1", LED01);
  SCmd.addCommand("L2", LED02);
  SCmd.addCommand("L3", LED03);
  SCmd.addCommand("L4", LED04);
  SCmd.addCommand("L5", LED05);
  SCmd.addCommand("L6", LED06);
  SCmd.addCommand("L7", LED07);
  SCmd.addCommand("L8", LED08);
  SCmd.addCommand("L9", LED09);
  SCmd.addCommand("L10", LED10);
  SCmd.addCommand("L11", LED11);
  SCmd.addCommand("L12", LED12);  
  SCmd.addCommand("T1", Test1);
  SCmd.addCommand("T2", Test2);
  SCmd.addCommand("T3", Test3);
  SCmd.addCommand("T4", Test4);
  SCmd.addCommand("T5", Test5);
  SCmd.addCommand("T6", Test6);
  SCmd.addCommand("T7", Test7);
  SCmd.addCommand("T8", Test8);
  SCmd.addCommand("T9", Test9);
  SCmd.addCommand("T10", Test10);
  SCmd.addCommand("T11", Test11);
  SCmd.addCommand("T12", Test12);
  SCmd.addCommand("R", SetNeoPixelColours);
  SCmd.addCommand("OFF", LED_Off);
  SCmd.addCommand("ON", LED_On);
  SCmd.addCommand("B", Brightness);
}