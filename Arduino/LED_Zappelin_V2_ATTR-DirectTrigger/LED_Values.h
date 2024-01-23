
boolean   OldNeopixel  = true;              // Set Neopixel stick version (RGB vs RGBW)
int       nLED         = 4;                // Total number of LED 

/* ----------------------------------------------------------------------------------*/
/* ------------------------------ LED Wavelength (nm) -------------------------------*/

const int Wavelength01 = 473;
const int Wavelength02 = 473;
const int Wavelength03 = 473;
const int Wavelength04 = 473;

int Wavelength_Array[] {Wavelength01,Wavelength02,Wavelength03,Wavelength04};


/* ----------------------------------------------------------------------------------*/
/* ----------------- Max LED power ( to be set during calibration) ------------------*/

const int max_LED01 = 4095;  
const int max_LED02 = 4095;  
const int max_LED03 = 4095;  
const int max_LED04 = 4095;  

int LEDPower_Array[] = {max_LED01, max_LED02, max_LED03, max_LED04};


/* ----------------------------------------------------------------------------------*/
/* ----------------------------  Max Intensity LED power  ---------------------------*/

int max_LED_Power = 100;

const int max01 = max_LED_Power;  // LED maximum intensity 1
const int max02 = max_LED_Power;  // LED maximum intensity 2
const int max03 = max_LED_Power;  // LED maximum intensity 3
const int max04 = max_LED_Power;  // LED maximum intensity 4

int LEDPower_Array2[] = {max01, max02, max03, max04};


/* ----------------------------------------------------------------------------------*/
/* ----------------------------------- LED arrays -----------------------------------*/

int led01 = 0;   // Define 1st Channel
int led02 = 1;   // Define 2nd Channel
int led03 = 2;   // Define 3rd Channel
int led04 = 3;   // Define 4th Channel

int LED_Array[] = {led01, led02, led03, led04};


/* ----------------------------------------------------------------------------------*/
/* ------------------------ Stimuli relative LED power (%) --------------------------*/

int LED1_Power = 100;
int LED2_Power = 100;
int LED3_Power = 100;
int LED4_Power = 100;

int LEDPower[] = {LED1_Power, LED2_Power, LED3_Power, LED4_Power};

/* ----------------------------------------------------------------------------------*/
/* -------------------------------- Neopixel HSV hue --------------------------------*/

int bits = 65535;
int hsv_hue1;
int hsv_hue2;
int hsv_hue3;
int hsv_hue4;

int hsv_hue_Array[] = {hsv_hue1, hsv_hue2, hsv_hue3, hsv_hue4};


/* ----------------------------------------------------------------------------------*/
/* ---------------------------- Neopixel HSV saturation -----------------------------*/

int hsv_sat = 255;

int hsv_sat1 = hsv_sat;
int hsv_sat2 = hsv_sat;
int hsv_sat3 = hsv_sat;
int hsv_sat4 = hsv_sat;

int hsv_sat_Array[] = {hsv_sat1, hsv_sat2, hsv_sat3, hsv_sat4};


/* ----------------------------------------------------------------------------------*/
/* ------------------------------- Neopixel HSV value -------------------------------*/

int hsv_val = 100;

int hsv_val1 = hsv_val;
int hsv_val2 = hsv_val;
int hsv_val3 = hsv_val;
int hsv_val4 = hsv_val;

int hsv_val_Array[] = {hsv_val1, hsv_val2, hsv_val3, hsv_val4};



void SetWavelength(){
  for (int i = 0; i <= nLED-1; i++) {
    float Wave = Wavelength_Array[i];

    // Convert wavelength into RGB
    float attenuation;
    float rr;
    float gg;
    float bb;

    if (Wave <= 365){
      Wave = 365;
    }
    if (Wave >= 780){
      Wave = 780;
    }

    if (Wave>=365 && Wave<440){
      attenuation = 0.3 + 0.7 * (Wave - 365) / (440 - 365);
      rr = -(Wave - 440) / (440 - 365) * attenuation;
      gg = 0.0;
      bb = attenuation;
    }
    else if (Wave>=440 && Wave<490){
      rr = 0.0;
      gg = (Wave - 440) / (490 - 400);
      bb = 1.0;
    }
    else if (Wave>=490 && Wave<510){
      rr = 0.0;
      gg = 1.0;
      bb = (Wave - 510) / (510 - 490);
    }
    else if (Wave>=510 && Wave<580){
      rr = (Wave - 510) / (580 - 510);
      gg = 1.0;
      bb = 0.0;
    }
    else if (Wave>=580 && Wave<645){
      rr = 1.0;
      gg = -(Wave - 645) / (645 - 580);
      bb = 0.0;
    }
    else if (Wave>=645 && Wave<780){
      attenuation = 0.3 + 0.7 * (780 - Wave) / (780 - 645);
      rr = attenuation;
      gg = 0.0;
      bb = 0.0;
    }
    else {
      rr = 0.0;
      gg = 0.0;
      bb = 0.0;
    }

    // Convert RGB to Hue
    float Hue;
    int   HSV_Hue;
    float maxC = max(max(rr,gg),bb);
    float minC = min(min(rr,gg),bb);
    float rangeC = maxC - minC;

    float rC = (maxC-rr) / rangeC;
    float gC = (maxC-gg) / rangeC;
    float bC = (maxC-bb) / rangeC;

    if (minC == maxC){
      Hue = 0;
    }
    else if (rr == maxC){
      Hue = bC - gC;
    }
    else if (gg == maxC){
      Hue = 2.0 + rC - bC;
    }
    else {
      Hue = 4.0 + gC - rC;
    }
    Hue = (Hue / 6.0);
    if (OldNeopixel == false){
      HSV_Hue = round(bits - (Hue * bits));
    }
    if (OldNeopixel == true){
      HSV_Hue = round(Hue * bits);
    }
    hsv_hue_Array[i] = HSV_Hue;
  }
}

