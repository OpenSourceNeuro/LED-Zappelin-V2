
boolean   OldNeopixel  = true;              // Set Neopixel stick version (RGB vs RGBW)
int       nLED         = 12;                // Total number of LED 

/* ----------------------------------------------------------------------------------*/
/* ------------------------------ LED Wavelength (nm) -------------------------------*/

const int Wavelength01 = 365;
const int Wavelength02 = 366;
const int Wavelength03 = 385;
const int Wavelength04 = 405;
const int Wavelength05 = 420;
const int Wavelength06 = 475;
const int Wavelength07 = 490;
const int Wavelength08 = 525;
const int Wavelength09 = 543;
const int Wavelength10 = 570;
const int Wavelength11 = 610;
const int Wavelength12 = 625;

int Wavelength_Array[] {Wavelength01,Wavelength02,Wavelength03,Wavelength04,Wavelength05,Wavelength06,Wavelength07,Wavelength08,Wavelength09,Wavelength10,Wavelength11,Wavelength12};


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
int hsv_hue1;
int hsv_hue2;
int hsv_hue3;
int hsv_hue4;
int hsv_hue5;
int hsv_hue6;
int hsv_hue7;
int hsv_hue8;
int hsv_hue9;
int hsv_hue10;
int hsv_hue11;
int hsv_hue12;


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

