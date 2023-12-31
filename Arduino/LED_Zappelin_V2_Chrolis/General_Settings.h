/*          ---  General Settings  ---
*/
#include "LED_Values.h"                     // Include LED Values defined in the second tab
#include <Adafruit_NeoPixel.h>



#define   Blank          35                 // Optional feature to prevent LED to light up 
#define   NeoPixel       32                 // NeoPixel pin
#define   NeoPixel_LED   16                 // Number of NeoPixel LEDs

#define   Trigger        33                 // Trigger channel must be connected to pin A0/DAC2
#define   pin_LED01      25                 // 2 - 1
#define   pin_LED02      23                 // 1 - 1
#define   pin_LED03      22                 // 1 - 2
#define   pin_LED04      21                 // 1 - 3
#define   pin_LED05      26                 // 2 - 2
#define   pin_LED06      19                 // 1 - 4
#define   pin_LED07      27                 // 2 - 3 
#define   pin_LED08      14                 // 2 - 4
#define   pin_LED09      18                 // 1 - 5
#define   pin_LED10      5                  // 1 - 6
#define   pin_LED11      12                 // 2 - 5 
#define   pin_LED12      13                 // 2 - 6 

  int LED_Array[] = {pin_LED01, pin_LED02, pin_LED03, pin_LED04, pin_LED05, pin_LED06, pin_LED07, pin_LED08, pin_LED09, pin_LED10, pin_LED11, pin_LED12};
  //Adafruit_NeoPixel strip(NeoPixel_LED, NeoPixel, NEO_GRB + NEO_RGBW);
    Adafruit_NeoPixel strip(NeoPixel_LED, NeoPixel, NEO_GRB + NEO_KHZ800);



/* ----------------------------------------------------------------------------------*/
/* ------------------------------- Global Variables ---------------------------------*/

word           BaudRate      = 921600;      // Baud Rate speed
char           sCmd;                        // Serial monitor 
float          aNumber;
char           *arg;

bool           StimulusFlag = false;
bool           flag;
int            i;                           // Iteration loop factor
int            iLoop;
int            CurrentMicros;               // Current Microsecond clock
int            PreviousMicros;              // Microsecond clock stamp
int            DiffMicros;                  // Difference in microseconds between the clock and the stamp
int            tPreviousMicros;             // Microsecond clock stamp
int            tDiffMicros;                 // Difference in microseconds between the clock and the stamp
int            tdPreviousMicros;            // Microsecond clock stamp
int            tdDiffMicros;                // Difference in microseconds between the clock and the stamp
int            ResolutionMicros;            // Microseconds delay between two i iteration
int            PreAdaptMicros;              // Preadaptation period in microseconds
bool           PreAdaptationFlag;
bool           TriggerModeFlag;
int            TriggerMode;                 // Set the Trigger mode
int            TriggerArray[100];

int            t;                           // Trigger counter
int            td;                          // Trigger Pulse counter
int            tr;                          // TriggerTime array counter
bool           TriggerFlag = false;         // Trigger Flag
int            TriggerTime;                 // Lenght of the Trigger loop in ms 
int            TriggerDuration = 100000;    // Length of the Trigger signal in us 

int            brightness    = 100;         // NeoPixel brightness (max = 255)
int            l;                           // LED iteration factor


/* ----------------------------------------------------------------------------------*/
/* --------------------- LED Zappelion' initialising conditions ---------------------*/

void HardwareSettings(){
  
// Initialise the serial communication with PC
  Serial.begin(BaudRate);                      
  
// Initialise the Neopixel Strip
  if (OldNeopixel == true){
    Adafruit_NeoPixel strip(NeoPixel_LED, NeoPixel, NEO_GRB + NEO_KHZ800);
  }
  strip.begin();           
  strip.show();                    // Turn OFF all pixels ASAP
  strip.setBrightness(brightness); // Set NeoPixel brightness 

// Set pins
  pinMode(Trigger, OUTPUT);  
  digitalWrite(Trigger, LOW);  
  pinMode(Blank, INPUT);
  digitalWrite(Blank, HIGH);
  pinMode(13,OUTPUT);
  digitalWrite(Trigger, LOW); 

// Initialise parameters
  l = 0;
  t = 0;
  td = 0;
  TriggerFlag = false;
  CurrentMicros = 0;
  PreviousMicros = 0;
  DiffMicros = 0;
  tPreviousMicros = 0;
  tDiffMicros = 0;
  tdPreviousMicros = 0;
  flag = true;
}


