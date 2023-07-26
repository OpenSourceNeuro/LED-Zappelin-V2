
/* ----------------------------------------------------------------------------------*/
/* ----------------- Max LED power ( to be set during calibration) ------------------*/

const int max_LED01 = 4095;  
const int max_LED02 = 4095;  
const int max_LED03 = 4095;  
const int max_LED04 = 4095;  
const int max_LED05 = 4095;  
const int max_LED06 = 4095;  
const int max_LED07 = 4095;  
const int max_LED08 = 4095;  
const int max_LED09 = 4095;  
const int max_LED10 = 4095;  
const int max_LED11 = 4095;  
const int max_LED12 = 4095;  

int LEDPower_Array[] = {max_LED01, max_LED02, max_LED03, max_LED04, max_LED05, max_LED06, max_LED07, max_LED08, max_LED09, max_LED10, max_LED11, max_LED12 };


/* ----------------------------------------------------------------------------------*/
/* ----------------------------  Max Intensity LED power  ---------------------------*/

int max_LED_Power = 100;

const int max01 = max_LED_Power;  // LED maximum intensity 1
const int max02 = max_LED_Power;  // LED maximum intensity 2
const int max03 = max_LED_Power;  // LED maximum intensity 3
const int max04 = max_LED_Power;  // LED maximum intensity 4
const int max05 = max_LED_Power;  // LED maximum intensity 5
const int max06 = max_LED_Power;  // LED maximum intensity 6
const int max07 = max_LED_Power;  // LED maximum intensity 7
const int max08 = max_LED_Power;  // LED maximum intensity 8
const int max09 = max_LED_Power;  // LED maximum intensity 9
const int max10 = max_LED_Power;  // LED maximum intensity 10
const int max11 = max_LED_Power;  // LED maximum intensity 11
const int max12 = max_LED_Power;  // LED maximum intensity 12

int LEDPower_Array2[] = {max01, max02, max03, max04, max05, max06, max07, max08, max09, max10, max11, max12};


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- LED arrays -----------------------------------*/

int led01 = 0;   // Define 1st Channel
int led02 = 1;   // Define 2nd Channel
int led03 = 2;   // Define 3rd Channel
int led04 = 3;   // Define 4th Channel
int led05 = 4;   // Define 5th Channel
int led06 = 5;   // Define 6th Channel
int led07 = 6;   // Define 7th Channel
int led08 = 7;   // Define 8th Channel
int led09 = 8;   // Define 9th Channel
int led10 = 9;   // Define 10th Channel
int led11 = 10;  // Define 11th Channel
int led12 = 11;  // Define 12th Channel

int LED_Array[] = {led01, led02, led03, led04, led05, led06, led07, led08, led09, led10, led11, led12};


/* ----------------------------------------------------------------------------------*/
/* ------------------------ Stimuli relative LED power (%) --------------------------*/

int LED1_Power = 0;
int LED2_Power = 0;
int LED3_Power = 0;
int LED4_Power = 0;
int LED5_Power = 0;
int LED6_Power = 0;
int LED7_Power = 0;
int LED8_Power = 0;
int LED9_Power = 0;
int LED10_Power = 0;
int LED11_Power = 0;
int LED12_Power = 0;

int LEDPower[] = {LED1_Power, LED2_Power, LED3_Power, LED4_Power, LED5_Power, LED6_Power, LED7_Power, LED8_Power, LED9_Power, LED10_Power, LED11_Power, LED12_Power};

/* ----------------------------------------------------------------------------------*/
/* -------------------------------- Neopixel HSV hue --------------------------------*/

int bits = 65535;
int hsv_hue1 = bits - 54612;
int hsv_hue2 = bits - 54496;
int hsv_hue3 = bits - 51713;
int hsv_hue4 = bits - 50163;
int hsv_hue5 = bits - 48514;
int hsv_hue6 = bits - 35105;
int hsv_hue7 = bits - 32942;
int hsv_hue8 = bits - 17052;
int hsv_hue9 = bits - 13903;
int hsv_hue10 = bits - 12190;
int hsv_hue11 = bits - 7701;
int hsv_hue12 = bits - 3910;

int hsv_hue_Array[] = {hsv_hue1, hsv_hue2, hsv_hue3, hsv_hue4, hsv_hue5, hsv_hue6, hsv_hue7, hsv_hue8, hsv_hue9, hsv_hue10, hsv_hue11, hsv_hue12};


/* ----------------------------------------------------------------------------------*/
/* ---------------------------- Neopixel HSV saturation -----------------------------*/

int hsv_sat = 255;

int hsv_sat1 = hsv_sat;
int hsv_sat2 = hsv_sat;
int hsv_sat3 = hsv_sat;
int hsv_sat4 = hsv_sat;
int hsv_sat5 = hsv_sat;
int hsv_sat6 = hsv_sat;
int hsv_sat7 = hsv_sat;
int hsv_sat8 = hsv_sat;
int hsv_sat9 = hsv_sat;
int hsv_sat10 = hsv_sat;
int hsv_sat11 = hsv_sat;
int hsv_sat12 = hsv_sat;

int hsv_sat_Array[] = {hsv_sat1, hsv_sat2, hsv_sat3, hsv_sat4, hsv_sat5, hsv_sat6, hsv_sat7, hsv_sat8, hsv_sat9, hsv_sat10, hsv_sat11, hsv_sat12};


/* ----------------------------------------------------------------------------------*/
/* ------------------------------- Neopixel HSV value -------------------------------*/

int hsv_val = 100;

int hsv_val1 = hsv_val;
int hsv_val2 = hsv_val;
int hsv_val3 = hsv_val;
int hsv_val4 = hsv_val;
int hsv_val5 = hsv_val;
int hsv_val6 = hsv_val;
int hsv_val7 = hsv_val;
int hsv_val8 = hsv_val;
int hsv_val9 = hsv_val;
int hsv_val10 = hsv_val;
int hsv_val11 = hsv_val;
int hsv_val12 = hsv_val;

int hsv_val_Array[] = {hsv_val1, hsv_val2, hsv_val3, hsv_val4, hsv_val5, hsv_val6, hsv_val7, hsv_val8, hsv_val9, hsv_val10, hsv_val11, hsv_val12};

