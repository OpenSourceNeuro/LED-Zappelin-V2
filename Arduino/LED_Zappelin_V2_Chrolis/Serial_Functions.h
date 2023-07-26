#include "General_Settings.h"
#include <SerialCommand.h>   // SerialCommand Library by Steven Cogswell https://github.com/shyd/Arduino-SerialCommand
SerialCommand SCmd;

/* ----------------------------------------------------------------------------------*/
/* -------------------------------- Turn all LED off --------------------------------*/
void LED_Off(){
  for (int l = 0; l <= nLED-1; l++) {
    analogWrite(LED_Array[l],0);                        
    strip.setPixelColor(l,strip.ColorHSV(hsv_hue_Array[l],hsv_sat_Array[l],0));
  } 
    
  strip.show();  
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------- Inititate new stimulation sequence -----------------------*/
void SetStimulus(){
    i = 1;
    t = 0;
    td = 0;

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

    TriggerTime = 1000 / (ResolutionMicros/1000);
    TriggerDuration = TriggerDur / (ResolutionMicros/1000);

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
    analogWrite(LED_Array[l],LEDPower_Array[l]*LEDPower_Array2[l]/100*LEDPower[l]/100);   
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
    analogWrite(LED_Array[l],LEDPower_Array[l]*LEDPower_Array2[l]/100*LEDPower[l]/100);   
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
    analogWrite(LED_Array[l],LEDPower_Array[l]*LEDPower_Array2[l]/100*LEDPower[l]/100);   
    strip.setPixelColor(l,strip.ColorHSV(hsv_hue_Array[l],hsv_sat_Array[l],hsv_val_Array[l]*LEDPower_Array2[l]/100*LEDPower[l]/100));
  }
}


void Stimulus(){
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
/* ------------------------------- Set NeoPixel LEDs --------------------------------*/
void SetNeoPixelColours(){
  for (int l = 0; l <= nLED-1; l++) {
    strip.setPixelColor(l,strip.ColorHSV(hsv_hue_Array[l],hsv_sat_Array[l],100));
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


}