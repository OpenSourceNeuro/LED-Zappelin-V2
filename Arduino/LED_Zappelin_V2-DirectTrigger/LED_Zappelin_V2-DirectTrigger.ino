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
  TriggerState = digitalRead(Trigger);
  
  CurrentMicros = micros();                          // Pick up current running time in microseconds
  DiffMicros = CurrentMicros - PreviousMicros;       // Calculate 
  
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

  if (TriggerState == HIGH){
    LED_On();
  }
  else if (TriggerState == LOW){
    LED_Off();
  }

}




