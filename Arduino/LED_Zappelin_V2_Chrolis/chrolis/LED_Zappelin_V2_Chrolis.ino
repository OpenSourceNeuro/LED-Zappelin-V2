#include "Serial_functions.h"

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
  
  if (DiffMicros >= ResolutionMicros) {
    PreviousMicros = micros();

    if (StimulusFlag == true){
      Serial.println(i);
      i += 1;
      if(i >= iLoop){
        i = 0;
      }
    }
  }
 
  if (tDiffMicros >= TriggerTime ) {
    tPreviousMicros = micros();

    if (StimulusFlag == true){
  
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
}




