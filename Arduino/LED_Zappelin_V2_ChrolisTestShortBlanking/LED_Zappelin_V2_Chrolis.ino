#include "Serial_functions.h"
int NewCurrentMicros;
int diff;


/* ----------------------------------------------------------------------------------*/
/* --------------------------- Settings and Initialisings ---------------------------*/

void setup() {
  HardwareSettings();             // Load Hardware Settings as described in "General_Settings.h"
  SetWavelength();                // Set the LEDs wavelength as described in "LED_Values.h"  
  SetNeoPixelColours();           // Light up LED in sequence when the stimulator is reset
  SCmdAddCommand();               // Initiate Serial Command actions
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Main Loop ------------------------------------*/
  
void loop() {
  SCmd.readSerial();                                 // Wait for Serial Command
  
  CurrentMicros = micros();                          // Pick up current running time in microseconds
  DiffMicros = CurrentMicros - PreviousMicros;       // Calculate 
  tDiffMicros = CurrentMicros - tPreviousMicros;
  
  if (BlankingInvert = false){
    if (BlankingState == true && BlankingFlag == true){
      BlankingFlag = false;    
      bPreviousMicros = CurrentMicros;
      OutputEnable = true;
    }
    if (BlankingState == false){
      BlankingFlag = true;
    }
  }

  if (BlankingInvert = true){
    if (BlankingState == false && BlankingFlag == true){
      BlankingFlag = false;    
      bPreviousMicros = CurrentMicros;
      OutputEnable = true;
    }
    if (BlankingState == true){
      BlankingFlag = true;
    }
  }

  if (PreAdaptationFlag == false){
    if (DiffMicros >= ResolutionMicros) {
      PreviousMicros = micros();

      if (StimulusFlag == true){
        Serial.println(i);
        i += 1;
        if(i >= iLoop){
          i = 1;
        }
      }
    }
  }
  
  if (PreAdaptationFlag == true){
    if (DiffMicros >= PreAdaptMicros) {
      PreviousMicros = micros();
      PreAdaptationFlag = false;

      if (StimulusFlag == true){
        Serial.println(i);
        i += 1;
      }
    }
  }

  if (tDiffMicros >= TriggerTime) {
    tPreviousMicros = micros();

    if (StimulusFlag == true && PreAdaptationFlag == false){

      if (TriggerModeFlag == true) {
        TriggerFlag = true;
        tdPreviousMicros = CurrentMicros;
        digitalWrite(Trigger, HIGH);
        
        tr +=1;
        if (tr >= TriggerMode){
          tr = 0;
        }    
        TriggerTime = TriggerArray[tr];
      }
    }
  }

  if (TriggerFlag == true){ 

    if (CurrentMicros >= tdPreviousMicros+TriggerDuration){
      digitalWrite(Trigger, LOW);
      TriggerFlag = false;
    }
  }

  bDiffMicros = CurrentMicros - bPreviousMicros;
  if (bDiffMicros >= BlankingTime) {
      OutputEnable = false;
  }

  if (OutputEnable == true){
    for (int l = 0; l <= nLED-1; l++) {
      analogWrite(LED_Array[l],ChrolisPWM[l]);
    }
  }
  if (OutputEnable == false){
    for (int l = 0; l <= nLED-1; l++) {
      analogWrite(LED_Array[l],0);
    }
  }
  
}







