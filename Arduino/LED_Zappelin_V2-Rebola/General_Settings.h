/*          ---  General Settings  ---
*/
#include "LED_Values.h"                     // Include LED Values defined in the second tab
#include <SPI.h>                            // Include the arduino serial port interface library
#include "Adafruit_TLC5947.h"               // Include the Adafruit TLC5947 libvrary. For better result one may change the number of channel defined in the Adafruit_TLC5947.cpp library
#include <Adafruit_NeoPixel.h>


#define   MISO           23                 // TLC SPI connection, Data Out
#define   MOSI           19                 // TLC SPI connection, Data In 
#define   CLK            18                 // TLC SPI connection, Clock 
#define   latch          5                  // TLC Latch
#define   Blank          17                 // TLC Ouput Enable, Also Optional feature to prevent LED to light up when powering up the TLC board

#define   NeoPixel       25                 // NeoPixel pin
#define   NeoPixel_LED   16                 // Number of NeoPixel LEDs

#define   Trigger        26                 // Trigger channel 


    Adafruit_TLC5947 tlc = Adafruit_TLC5947(1, CLK, MISO, latch);
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
int            ResolutionMicros;            // Microseconds delay between two i iteration
int            PreAdaptMicros;              // Preadaptation period in microseconds
bool           PreAdaptationFlag;

bool           TriggerState;

int            brightness    = 100;         // NeoPixel brightness (max = 255)
int            l;                           // LED iteration factor


/* ----------------------------------------------------------------------------------*/
/* --------------------- LED Zappelion' initialising conditions ---------------------*/
void HardwareSettings(){
  
// Initialise the serial communication with PC
  Serial.begin(BaudRate);                      
  
// Initialise the Adafruit TLC driver 
  tlc.begin();
  tlc.write();  

// Initialise the Neopixel Strip
  if (OldNeopixel == true){
    Adafruit_NeoPixel strip(NeoPixel_LED, NeoPixel, NEO_GRB + NEO_KHZ800);
  }
  strip.begin();           
  strip.show();                    // Turn OFF all pixels ASAP
  strip.setBrightness(brightness); // Set NeoPixel brightness 

// Set pins
  pinMode(Trigger, INPUT);   
  pinMode(Blank, INPUT);
  digitalWrite(Blank, HIGH);
  pinMode(13,OUTPUT);


// Initialise parameters
  l = 0;
  CurrentMicros = 0;
  PreviousMicros = 0;
  DiffMicros = 0;
  flag = true;
  TriggerState = LOW;
}


