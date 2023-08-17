<p align="left">
<img width="270" height="170" src="./Images/SpikyLogo.png">
</p>

<h1 align="center"> Spikeling v2.2 - Assembly Manual</h1></p>


<br></br>


## Overview

<p align="justify">
This page contains detailed assembly instructions for both version of LEDF Zappelin', and includes a parts list for purchasing all electronics components.
Instructions on how to upload and update the microcontroller code and how to calibrate the device can be found <a href=""> <strong>here</strong> </a>
</p>

 The Arduino code and 3D printing files (SCAD and STL) can be downloaded [here](https://github.com/BadenLab/LED-Zappelin/tree/master/3D%20Designs), and further modified to fit customise purposes. The aim of this device is to finely control LEDs used in combination with a 2-photon microscope.

The device consists of a custom-designed PCB, an [ESP32 development board](https://learn.adafruit.com/adafruit-huzzah32-esp32-feather) (or an Arduino Nano if the stimulator does not need to be combined with a 2 photon microscope), a [LED driver](https://learn.adafruit.com/tlc5947-tlc59711-pwm-led-driver-breakout/overview) and various off-the-shelf components.

***

- [Assembling the Stimulator](#Assembling-the-Stimulator)
- [Programming the Stimulator](#Programming-the-ESP32)
- [Operating the Stimulator](#Operating-the-Stimulator)
- [Calibrating the Stimulator](#Calibrating-the-Stimulator)

***
<img align="right" width="600" height="300" src="./Images/LED-Zappelin-V2.png">
