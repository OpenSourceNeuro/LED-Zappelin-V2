#include "Serial_functions.h"

/* ----------------------------------------------------------------------------------*/
/* --------------------------- Settings and Initialisings ---------------------------*/

void setup() {
  HardwareSettings();
  SetNeoPixelColours();
  SCmdAddCommand();
  
}


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- Main Loop ------------------------------------*/
  
void loop() {
  SCmd.readSerial();
  
  CurrentMicros = micros();
  DiffMicros = CurrentMicros - PreviousMicros;
  
  if (DiffMicros >= ResolutionMicros) {
    PreviousMicros = micros();

    if (StimulusFlag == true){
      Serial.println(i);
      i += 1;
      t += 1;
      if (TriggerFlag == true) {
        td += 1;
      }

      if (t >= TriggerTime) {
        t = 0;
        TriggerFlag = true;
        digitalWrite(Trigger, HIGH);
      }

      if (td >= TriggerDuration){
        digitalWrite(Trigger, LOW);
        TriggerFlag = false;
        td = 0;
      }

      if(i >= iLoop){
        i = 0;
      }
    }
  }
}