/*          ---  General Settings  ---
*/
#include "LED_Values.h"                     // Include LED Values defined in the second tab
#include <SPI.h>                            // Include the arduino serial port interface library
#include "Adafruit_TLC5947.h"               // Include the Adafruit TLC5947 libvrary. For better result one may change the number of channel defined in the Adafruit_TLC5947.cpp library
#include <Adafruit_NeoPixel.h>


#define   MOSI           23                 // TLC SPI connection, Date Out
#define   MISO           19                 // TLC SPI connection,Data In 
#define   CLK            18                 // TLC SPI connection, Clock 
#define   latch          5                  // TLC Latch
#define   Blank          17                 // TLC Ouput Enable, Also Optional feature to prevent LED to light up when powering up the TLC board

#define   NeoPixel       25                 // NeoPixel pin
#define   NeoPixel_LED   16                 // Number of NeoPixel LEDs

#define   Trigger        26                 // Trigger channel must be connected to pin A0/DAC2



    Adafruit_TLC5947 tlc = Adafruit_TLC5947(1, CLK, MOSI, latch);
    Adafruit_NeoPixel strip(NeoPixel_LED, NeoPixel, NEO_GRB + NEO_RGBW);//NEO_KHZ800);



/* ----------------------------------------------------------------------------------*/
/* ------------------------------- Global Variables ---------------------------------*/

word           BaudRate      = 921600;      // Baud Rate speed
char           sCmd;                        // Serial monitor 
float          aNumber;
char           *arg;

boolean        StimulusFlag = false;
boolean        flag;
int            i;                           // Iteration loop factor
int            iLoop;
int            CurrentMicros;               // Current Microsecond clock
int            PreviousMicros;              // Microsecond clock stamp
int            DiffMicros;                  // Difference in microseconds between the clock and the stamp
int            ResolutionMicros;            // Microseconds delay between two i iteration

int            t;                           // Trigger counter
int            td;                          // Trigger Pulse counter
boolean        TriggerFlag = false;         // Trigger Flag
int            TriggerTime;                 // Lenght of the Trigger loop in ms 
int            TriggerDur = 25;             // Length of the Trigger signal in ms 
int            TriggerDuration;

int            brightness    = 100;         // NeoPixel brightness (max = 255)
int            l;                           // LED iteration factor
int            nLED          = 12;          // Total number of LED 

/* ----------------------------------------------------------------------------------*/
/* --------------------- LED Zappelion' initialising conditions ---------------------*/

void HardwareSettings(){
  
// Initialise the serial communication with PC
  Serial.begin(BaudRate);                      
  
// Initialise the Adafruit TLC driver 
  tlc.begin();
  tlc.write();  

// Initialise the Neopixel Strip
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
  flag = true;
}