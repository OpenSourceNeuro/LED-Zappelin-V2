

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
  
  digitalWrite(Trigger, HIGH);
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
  SCmd.addCommand("S", SetStimulus);
  SCmd.addCommand("M", SetTriggerMode);
  SCmd.addCommand("T", SetTrigger);
  SCmd.addCommand("O", StopStimulus);
  SCmd.addCommand("L1", LED01);
  SCmd.addCommand("L2", LED02);
  SCmd.addCommand("L3", LED03);
  SCmd.addCommand("L4", LED04);
  SCmd.addCommand("T1", Test1);
  SCmd.addCommand("T2", Test2);
  SCmd.addCommand("T3", Test3);
  SCmd.addCommand("T4", Test4);
  SCmd.addCommand("R", SetNeoPixelColours);
  SCmd.addCommand("OFF", LED_Off);
  SCmd.addCommand("ON", LED_On);
  SCmd.addCommand("B", Brightness);
}




