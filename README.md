<<<<<<< HEAD
<p align="left"><img width="270" height="170" src="./Images/SpikyLogo.png">

<h1 align="center"> LED Zappelin' v2</h1></p>
<h3 align="center">  An Open Source and versatile LED controller for arbitrary spectrum visual stimulation and optogenetics during two-photon imaging.</h3></p>
<p align="center"><h6 align="right">developed by M.J.Y. Zimmermann, A.M. Chagas & T. Baden</h6></p>

<br>




This project is licensed under the <a href="https://www.gnu.org/licenses/gpl-3.0.html">GNU General Public License v3.0</a><br>
The hardware is licensed under the <a href="https://cern-ohl.web.cern.ch">CERN OHL v1.2</a>


***


<p style='text-align: justify;'>
Two-photon microscopy is a cornerstone technique in neuroscience research, but combining this technology with spectrally arbitrary light stimulation can be challenging due to crosstalk between stimulation light and fluorescence detection.
To overcome this limitation, we present LED Zappelin': a simple and low-cost electronic solution to rapidly time-interleave stimulation and detection epochs during scans.
</p>

The second version of this project allows user to either:

  - Independently drive up to 24 arbitrary spectrum LEDs to meet user requirements. Using the <a href="https://www.ti.com/lit/ds/symlink/tlc5947.pdf">LTC5947 LED driver</a>.
  - Control external light source generator such as the <a href="https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=13597">Thorlabs Chrolis</a>. Using TTL logic circuits.

<p style='text-align: justify;'>
In the <a href=https://pubmed.ncbi.nlm.nih.gov/35498254/>original publication</a>, we demonstrate the utility of our stimulator for colour vision experiments on the in vivo tetrachromatic zebrafish retina and for optogenetic circuit mapping in Drosophila.
</p>


<br>


- [An open and versatile LED controler](#Introduction)
- [A £100 DIY efficient stimulator](https://github.com/BadenLab/LED-Zappelin/blob/master/Bills%20of%20Materials/BOM%20-%20Stimulator.csv)
- [A stimulator for visual neuroscience](#Colour-Vision-Experiment)
- [A stimulator for optogenetics](#Optogenetics-Experiment)
- [A detailed assembly and instruction manual](https://github.com/BadenLab/LED-Zappelin/blob/master/Instruction%20Manual/README.md)
- [A step by step calibration script](https://github.com/BadenLab/LED-Zappelin/blob/master/Instruction%20Manual/Stimulator%20Calibration/Stimulator_Calibration.ipynb)
- [Repository Structure](#Repository-Structure)


## Introduction

<p align="justify">
Combining two-photon imaging with additional light stimulation – for example for visual stimulation or for driving optogenetic actuators – has remained challenging because the stimulation light can interfere with fluorescence detection. This can result in light artefacts in the image and/or may damage sensitive fluorescence detection equipment (e.g. photomultiplier tubes, PMTs).
</p>

<p align="justify">
A temporal separation between light stimulation and fluorescence detection, for example during the scan-retrace, can ameliorate these problems.
This problem can be readily solved electronically, for example through use of a microcontroller.
</p>

<p align="justify">
Here, we present such a solution. Our system can either line-synch up to 24 independent LED channels or can be connected to external commercial light sources, and can be assembled from off-the-shelf components for substantially below $200. This provides for flexible options of spectrally diverse light stimulation during two-photon scanning and comfortably provides sufficient power to drive standard optogenetics actuators such as CsChrimson.
</p>

<p align="justify">
Alongside, we also provided custom casing files (for either 3d print or laser-cut), designed suggestions for optically combining LED banks using Thorlabs parts, and an alternative 3D-printed LED holder and microscope chamber.
</p>

<p align="justify">
The device is built around an ESP32, a microcontroller which exchange signals with the recording setup, drive the light sources and runs on C++. However, users do not need to interfere with the source code as we provide an intuitive and interactive Graphical User Interface (GUI), from which all functions and variables can be manipulated.
<a href="">Here</a>, is the full user guide documentation.
</p>

<img align="center" src="https://github.com/BadenLab/LED-Zappelin/blob/master/Images/Fig1.png">

<h5 align="justify"> a) A fully assembled stimulator. b) Rendering of the custom-printed circuit board which accommodates the microcontroller, the LED driver and up to 24 LED channels. c) Schematics illustrating the circuit that controls the LED output. The blanking input can be inverted by a switch before reaching the output enable pin on the LED driver (electronically switching off the LEDs) and sending the signal to the micro-controller. A second switch control the blanking signal voltage as it needs to be adapted depending on the logic of the microcontroller used (3.3V for ESP32, 5V for Arduino). The microcontroller controls the LED driver through an SPI connection and send trigger signal output to an external. d) Illustration of the raster scan method described. The “blanking signal” is synchronous with the scanning logic, enabling the LEDs during the scanning mirrors retrace (black) and shutting them off during the acquisition (red), therefore providing temporal separation between stimulation and detection (Modified from (Euler et al. 2019)</h5>

***

<p align="justify">The stimulator runs synchronous to the recording system using TTL triggers. TTL signals correspond to scanning mirror retrace periods and are used to turn ON and OFF LEDs, thus avoiding swamping the PMTs by stimulation light.

<p align="justify">On the PCB, we incorporated a signal inverter which can be enabled through a jumper (see below) and that can modulated the TTL signal sign. This customisable option thus offers the possibility for a single design to be easily adapted to multiple imaging systems.</p>

<img align="center" src="https://github.com/BadenLab/LED-Zappelin/blob/master/Images/Fig2.png">
<h5 align="justify"> a) Oscilloscope reading of the blanking signal (blue) efficiently switching off an LED (yellow). The blanking is operated here without noticeable delay. b) Same as a), showing for a 1ms scanning cycle, the two possible configurations for the blanking signal input, with a low (top) and a high (bottom) blanking signal input respectively for an inverted and original signal input. </h5>

***

<p align="justify"> The use of a dedicated constant current LED driver tends to improve LED stability over time as well as its life span. Such driver ensures that the current drawn by the LED never leads to thermal runaways that might cause irreversible damage. This is particularly essential for short wavelength LEDs which tend to rapidly decay, thus necessitating regular recalibration or replacement. </p>

<img align="center" src="https://github.com/BadenLab/LED-Zappelin/blob/master/Images/Fig3.png">
<h5 align="justify">  a) Power recording of a 4 LED system using the TLC5947 (solid lines) and their expected brightness if directly controlled by a microcontroller (dashed lines). All LEDs have been set up to the same power (40nW), with equal max intensities values in the Arduino code. b) Same as a) but with LEDs set up at different max intensities in the Arduino code. Here the linearity of the LED intensity output remains constant. </5>

***
=======
# LED-Zappelin-V2
>>>>>>> 1892e51c7560366fad7b1b9efeeaa54bd3a136fd
