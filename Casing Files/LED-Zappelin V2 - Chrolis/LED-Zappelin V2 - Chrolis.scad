Acrylic_Wall = 3;
tol = 0.1;
Smoothness = 60;
xxx = 300;

x_PCB = 120;
y_PCB = 100;
z_PCB = 2;
r_PCB = 3;
r_Acrylic = 5;

PCB_Spacing = 2.54;

r_hex = 5.65/2;
hex_bottom = 8;
hex_middle = 18+8;
hex_top = 8;


// // // Switches // // //
DXF = 1;
transparent = 0.8;

PCB = 10;

BNC = 10;
DPDT = 10;
ESP32 = 10;
SUBD25 = 10;
NeoPixel = 10;

Hex_Bottom = 10;
Hex_Middle = 10;
Hex_Top = 10;

Acrylic_Bottom  = 10;
Acrylic_Top  = 10;
Acrylic_Front  = 10;
Acrylic_Back  = 10;
Acrylic_Left  = 10;
Acrylic_Right  = 1;

// // // Parameters // // // //

x_BNC90 = 14.8;
y_BNC90 = 14.9;
z_BNC90 = 13.1;
h1_BNC90 = 10.5;
r1_BNC90 = 12.8/2;
h2_BNC90 = 9.8;
r2_BNC90 = 9.6/2;
h_pinBNC90 = 4.2;
r_pinBNC90 = 0.89/2;
offset_pinBNC90 = 0.2;

x_Switch = 8.8;
y_Switch = 13.7;
z_Switch = 8.8;
r_Switch = 6/2;
h_Switch = 2.7;
hpos_Switch = 4.4;
xoffset_pinSwitch = 1.86;
yoffset_pinSwitch = 7.62;
h_pinSwitch = 4.2;
r_pinSwitch = 0.6/2;
xoffset_pinSwitch1 = 25;
xoffset_pinSwitch2 = 25+PCB_Spacing;
xoffset_pinSwitch3 = 25-PCB_Spacing;
xoffset_pinSwitch4 = 50;
xoffset_pinSwitch5 = 50+PCB_Spacing;
xoffset_pinSwitch6 = 50-PCB_Spacing;
yoffset_pinSwitch1 = y_PCB-88.07;
yoffset_pinSwitch2 = y_PCB-90.62;

xpos1_M3 = 20;
xpos2_M3 = 100;
ypos1_M3 = 20;
ypos2_M3 = 80;
ypos11_M3 = 30;
ypos22_M3 = 70;
r_M3 = 3/2;

r_Hole = 0.5+tol;
ypos_BNC90_1 = y_PCB-80;
ypos_BNC90_1bis = y_PCB-82.54;
ypos_BNC90_2 = y_PCB-20;
ypos_BNC90_2bis = y_PCB-22.5;
xpos_BNC90 = 12.4;
xpos_Switch_1 = 22.3;
xpos_Switch_1bis = 27.7;
xpos_Switch_2 = 47.3;
xpos_Switch_2bis = 52.7;
ypos_Switch = y_PCB-95.7;



x_ESP = 55;
y_ESP = 28;
z_ESP = 11.5;
x_USB = 6;
y_USB = 10;
z_USB = 7.25;
h_USB = 2;
xpos_ESP = 4.3;
ypos_ESP = y_ESP/2 + 25/2;
r_pinUSB = 0.6/2;
h_pinUSB = 5;

x_Neo = 101.6;
y_Neo = 2;
z_Neo = 10.16;
r_Neo = 2/2;
xpos1_Neo = 12.7;
xpos2_Neo = 38.1;
xpos3_Neo = 63.5;
xpos4_Neo = 88.9;
zpos_Neo = 8.128;
x_NeoPixel = x_Neo;
z_NeoPixel = 5;
zoffset_NeoPixel = 1.25;

xpos_ESP32 = 5.09;
ypos1_ESP32 = 37.3;
ypos2_ESP32 = 62.7;

x1pos_SUBD = 76.2;
x2pos_SUBD = 77.575;
y1pos_SUBD = 80;
y2pos_SUBD = 82.85;
y11pos_SUBD = 20;
y22pos_SUBD = 17.2;

x_SUBD = 53.04;
y_SUBD = 12.4;
z_SUBD = 12.5;
spacing_SUBD = 2.77;
x1pin_SUBD = x_SUBD/2 - 6*spacing_SUBD;
x2pin_SUBD = x_SUBD/2 - spacing_SUBD/2 - 5*spacing_SUBD;
y1pin_SUBD = 8.1;
y2pin_SUBD = 8.1+2.84;
rpin_SUBD = 0.6/2;
hpin_SUBD = 3.18;



xmargin_Acrylic = 10;
ymargin_Acrylic = 10;
x_Acrylic = x_PCB + 2*xmargin_Acrylic;
y_Acrylic = y_PCB + 2*ymargin_Acrylic;
z_Acrylic = Acrylic_Wall;

x_AcrylicFront = x_PCB;
y_AcrylicFront = Acrylic_Wall;
z_AcrylicFront = z_PCB + hex_bottom + hex_middle ;

x_AcrylicSide = Acrylic_Wall;
y_AcrylicSide = y_PCB;
z_AcrylicSide = z_PCB + hex_bottom + hex_middle;

margin = 0.5;
y1margin_AcrylicFront = margin;
y2margin_AcrylicFront = margin;

x1margin_AcrylicSide = margin;
x2margin_AcrylicSide = margin;
x1margin_AcrylicFront = x1margin_AcrylicSide+Acrylic_Wall;
x2margin_AcrylicFront = x2margin_AcrylicSide+Acrylic_Wall;

y1margin_AcrylicSide = y1margin_AcrylicFront;
y2margin_AcrylicSide = y2margin_AcrylicFront;

// // // Functions // // //

if (PCB == 1){
    difference(){
        PCB();
        PCB_Holes();
    }
}

if (BNC == 1){
    translate([xpos_BNC90,ypos_BNC90_1,0])BNC90();
    translate([xpos_BNC90,ypos_BNC90_2,0])BNC90();
}

if (DPDT == 1){
    translate([xpos_Switch_1,ypos_Switch,0])Switch();
    translate([xpos_Switch_2,ypos_Switch,0])Switch();
}

if (ESP32 == 1){
    ESP();
}

if (SUBD25 == 1){
    translate([x2pos_SUBD,y_PCB-y2pos_SUBD,0])SUBD25();
    translate([x2pos_SUBD+11*2.77,y_PCB-y22pos_SUBD,0])rotate([0,0,180])SUBD25();
}

if (NeoPixel == 1 ){
    NeoPixel();
}

if (Hex_Bottom == 1){
    translate([xpos1_M3,ypos1_M3,-hex_bottom])Hex(hex_bottom);
    translate([xpos2_M3,ypos11_M3,-hex_bottom])Hex(hex_bottom);
    translate([xpos1_M3,ypos2_M3,-hex_bottom])Hex(hex_bottom);
    translate([xpos2_M3,ypos22_M3,-hex_bottom])Hex(hex_bottom);
}

if (Hex_Middle == 1){
    translate([xpos1_M3,ypos1_M3,z_PCB])Hex(hex_middle);
    translate([xpos2_M3,ypos11_M3,z_PCB])Hex(hex_middle);
    translate([xpos1_M3,ypos2_M3,z_PCB])Hex(hex_middle);
    translate([xpos2_M3,ypos22_M3,z_PCB])Hex(hex_middle);
}

if (Hex_Top == 1){
    translate([xpos1_M3,ypos1_M3,hex_middle+2*z_PCB])Hex(hex_top);
    translate([xpos2_M3,ypos11_M3,hex_middle+2*z_PCB])Hex(hex_top);
    translate([xpos1_M3,ypos2_M3,hex_middle+2*z_PCB])Hex(hex_top);
    translate([xpos2_M3,ypos22_M3,hex_middle+2*z_PCB])Hex(hex_top);
}

if (Acrylic_Bottom == 1 && DXF == 0){
    Acrylic_Botom();}
if (Acrylic_Bottom == 1 && DXF == 1){
    Acrylic_Botom_DXF();}

if (Acrylic_Top == 1 && DXF == 0){
    Acrylic_Top();}
if (Acrylic_Top == 1 && DXF == 1){
    Acrylic_Top_DXF();}

if (Acrylic_Front == 1 && DXF == 0){
    Acrylic_Front();}
if (Acrylic_Front == 1 && DXF == 1){
    Acrylic_Front_DXF();}

if (Acrylic_Back == 1 && DXF == 0){
    Acrylic_Back();}
if (Acrylic_Back == 1 && DXF == 1){
    Acrylic_Back_DXF();}

if (Acrylic_Left == 1 && DXF == 0){
    Acrylic_Left();}
if (Acrylic_Left == 1 && DXF == 1){
    Acrylic_Left_DXF();}
    
if (Acrylic_Right == 1 && DXF == 0){
    Acrylic_Right();}
if (Acrylic_Right == 1 && DXF == 1){
    Acrylic_Right_DXF();}

// // // Modules // // //


module PCB(){
    color([0.1,0.8,0])translate([r_PCB,r_PCB,0])minkowski(){
        cube([x_PCB-2*r_PCB,y_PCB-2*r_PCB,z_PCB-tol]);
        cylinder(r=r_PCB,h=tol,$fn=Smoothness);
    }
}


module BNC90(){
    color([1,1,1])translate([-x_BNC90+offset_pinBNC90+r_pinBNC90,-y_BNC90/2,z_PCB])cube([x_BNC90,y_BNC90,z_BNC90]);
    color([1,1,1])translate([-x_BNC90+offset_pinBNC90+r_pinBNC90-h1_BNC90,0,z_BNC90/2+z_PCB])rotate([0,90,0])cylinder(r=r1_BNC90+tol,h=h1_BNC90,$fn=Smoothness);
    color([192/255,192/255,192/255])translate([-x_BNC90+offset_pinBNC90+r_pinBNC90-h1_BNC90-h2_BNC90,0,z_BNC90/2+z_PCB])rotate([0,90,0])cylinder(r=r2_BNC90,h=h2_BNC90,$fn=Smoothness);
    translate([0,0,-h_pinBNC90+z_PCB])cylinder(r=r_pinBNC90,h=h_pinBNC90,$fn=Smoothness);
    translate([0,-PCB_Spacing,-h_pinBNC90+z_PCB])cylinder(r=r_pinBNC90,h=h_pinBNC90,$fn=Smoothness);
}


module Switch(){
    translate([-xoffset_pinSwitch,-y_Switch+yoffset_pinSwitch,z_PCB]){
        color([0.8,0.1,0.1])cube([x_Switch,y_Switch,z_Switch]);
        color([192/255,192/255,192/255])translate([x_Switch/2,0,hpos_Switch])rotate([90,0,0])cylinder(r=r_Switch+tol,h=h_Switch+xxx,$fn=Smoothness);
        translate([xoffset_pinSwitch,y_Switch-yoffset_pinSwitch,-h_pinSwitch+z_PCB])cylinder(r=r_pinSwitch,h=h_pinSwitch,$fn=Smoothness);
        translate([x_Switch-xoffset_pinSwitch,y_Switch-yoffset_pinSwitch,-h_pinSwitch+z_PCB])cylinder(r=r_pinSwitch,h=h_pinSwitch,$fn=Smoothness);
        translate([xoffset_pinSwitch,y_Switch-yoffset_pinSwitch+2*PCB_Spacing,-h_pinSwitch+z_PCB])cylinder(r=r_pinSwitch,h=h_pinSwitch,$fn=Smoothness);
        translate([xoffset_pinSwitch+PCB_Spacing,y_Switch-yoffset_pinSwitch+2*PCB_Spacing,-h_pinSwitch+z_PCB])cylinder(r=r_pinSwitch,h=h_pinSwitch,$fn=Smoothness);
        translate([xoffset_pinSwitch+2*PCB_Spacing,y_Switch-yoffset_pinSwitch+2*PCB_Spacing,-h_pinSwitch+z_PCB])cylinder(r=r_pinSwitch,h=h_pinSwitch,$fn=Smoothness);
        translate([xoffset_pinSwitch,y_Switch-yoffset_pinSwitch+3*PCB_Spacing,-h_pinSwitch+z_PCB])cylinder(r=r_pinSwitch,h=h_pinSwitch,$fn=Smoothness);
        translate([xoffset_pinSwitch+PCB_Spacing,y_Switch-yoffset_pinSwitch+3*PCB_Spacing,-h_pinSwitch+z_PCB])cylinder(r=r_pinSwitch,h=h_pinSwitch,$fn=Smoothness);
        translate([xoffset_pinSwitch+2*PCB_Spacing,y_Switch-yoffset_pinSwitch+3*PCB_Spacing,-h_pinSwitch+z_PCB])cylinder(r=r_pinSwitch,h=h_pinSwitch,$fn=Smoothness);
    }
}


module ESP(){
    translate([-xpos_ESP+xpos_ESP32,-ypos_ESP+ypos2_ESP32,z_PCB]){cube([x_ESP,y_ESP,z_ESP]);
        translate([-xxx,y_ESP/2-y_USB/2,z_ESP+h_USB-z_USB/2])cube([x_USB+xxx,y_USB,z_USB]);
        for (i = [0:1:1]){
            for (j = [0:1:18]){
                translate([xpos_ESP+j*2.54,ypos_ESP-i*25,-h_pinUSB])cylinder(r=r_pinUSB,h=h_pinUSB,$fn=Smoothness);
            }
        }  
    }  
}


module SUBD25(){
    translate([-x2pin_SUBD,-y1pin_SUBD-xxx,z_PCB]){
        cube([x_SUBD,y_SUBD+xxx,z_SUBD]);
        for (i = [0:1:12]){
            translate([x1pin_SUBD+(i*spacing_SUBD),y2pin_SUBD,-hpin_SUBD])cylinder(r=rpin_SUBD,h=hpin_SUBD,$fn=Smoothness);
        }
        for (i = [0:1:11]){
            translate([x2pin_SUBD+(i*spacing_SUBD),y1pin_SUBD,-hpin_SUBD])cylinder(r=rpin_SUBD,h=hpin_SUBD,$fn=Smoothness);
        }
    }
}


module NeoPixel(){
    translate([x_PCB/2-x_Neo/2,0,z_PCB+hex_middle-z_Neo-0.5])difference(){
        cube([x_Neo,y_Neo,z_Neo]);
        translate([xpos1_Neo,-tol,zpos_Neo])rotate([-90,0,0])cylinder(r=r_Neo,h=y_Neo+2*tol,$fn=Smoothness);
        translate([xpos2_Neo,-tol,zpos_Neo])rotate([-90,0,0])cylinder(r=r_Neo,h=y_Neo+2*tol,$fn=Smoothness);
        translate([xpos3_Neo,-tol,zpos_Neo])rotate([-90,0,0])cylinder(r=r_Neo,h=y_Neo+2*tol,$fn=Smoothness);
        translate([xpos4_Neo,-tol,zpos_Neo])rotate([-90,0,0])cylinder(r=r_Neo,h=y_Neo+2*tol,$fn=Smoothness);
    }
}

module NeoPixelHole(){
    translate([x_PCB/2-x_Neo/2,0,z_PCB+hex_middle-z_Neo-0.5]){
        translate([xpos1_Neo,-tol-xxx,zpos_Neo])rotate([-90,0,0])cylinder(r=r_Neo+tol,h=y_Neo+2*tol+xxx,$fn=Smoothness);
        translate([xpos2_Neo,-tol-xxx,zpos_Neo])rotate([-90,0,0])cylinder(r=r_Neo+tol,h=y_Neo+2*tol+xxx,$fn=Smoothness);
        translate([xpos3_Neo,-tol-xxx,zpos_Neo])rotate([-90,0,0])cylinder(r=r_Neo+tol,h=y_Neo+2*tol+xxx,$fn=Smoothness);
        translate([xpos4_Neo,-tol-xxx,zpos_Neo])rotate([-90,0,0])cylinder(r=r_Neo+tol,h=y_Neo+2*tol+xxx,$fn=Smoothness);
        translate([0,-xxx,zoffset_NeoPixel])cube([x_NeoPixel,xxx,z_NeoPixel]);
    }
}


module PCB_Holes(){
    translate([xpos_BNC90,ypos_BNC90_1,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xpos_BNC90,ypos_BNC90_1bis,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xpos_BNC90,ypos_BNC90_2,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xpos_BNC90,ypos_BNC90_2bis,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    
    translate([xpos_Switch_1,ypos_Switch,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xpos_Switch_1bis,ypos_Switch,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xpos_Switch_2,ypos_Switch,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xpos_Switch_2bis,ypos_Switch,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    
    translate([xoffset_pinSwitch1,yoffset_pinSwitch1,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xoffset_pinSwitch2,yoffset_pinSwitch1,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xoffset_pinSwitch3,yoffset_pinSwitch1,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xoffset_pinSwitch1,yoffset_pinSwitch2,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xoffset_pinSwitch2,yoffset_pinSwitch2,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xoffset_pinSwitch3,yoffset_pinSwitch2,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    
    translate([xoffset_pinSwitch4,yoffset_pinSwitch1,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xoffset_pinSwitch5,yoffset_pinSwitch1,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xoffset_pinSwitch6,yoffset_pinSwitch1,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xoffset_pinSwitch4,yoffset_pinSwitch2,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xoffset_pinSwitch5,yoffset_pinSwitch2,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xoffset_pinSwitch6,yoffset_pinSwitch2,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    
    translate([xpos1_M3,ypos1_M3,-tol])cylinder(r=r_M3,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xpos2_M3,ypos11_M3,-tol])cylinder(r=r_M3,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xpos1_M3,ypos2_M3,-tol])cylinder(r=r_M3,h=z_PCB+2*tol,$fn=Smoothness);
    translate([xpos2_M3,ypos22_M3,-tol])cylinder(r=r_M3,h=z_PCB+2*tol,$fn=Smoothness);
    
    for (i = [0:1:18]){
        translate([xpos_ESP32+i*2.54,ypos1_ESP32,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
        translate([xpos_ESP32+i*2.54,ypos2_ESP32,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    }
    
    for (i = [0:1:12]){
        translate([x1pos_SUBD+(i*spacing_SUBD),y_PCB-y11pos_SUBD,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    }
    for (i = [0:1:11]){
        translate([x2pos_SUBD+(i*spacing_SUBD),y_PCB-y22pos_SUBD,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    }
    
    for (i = [0:1:12]){
        translate([x1pos_SUBD+(i*spacing_SUBD),y_PCB-y1pos_SUBD,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    }
    for (i = [0:1:11]){
        translate([x2pos_SUBD+(i*spacing_SUBD),y_PCB-y2pos_SUBD,-tol])cylinder(r=r_Hole,h=z_PCB+2*tol,$fn=Smoothness);
    }
}


module Hex(height){
    color([255/255,215/255,0])cylinder(r=r_hex,h=height,$fn=8);
}


module Acrylic_Botom(){
    //color([0,1,0])difference(){
    color([0,0,0.8,transparent])difference(){
        translate([-xmargin_Acrylic+r_Acrylic,-ymargin_Acrylic+r_Acrylic,-hex_bottom-z_Acrylic]){
            minkowski(){
                cube([x_Acrylic-2*r_Acrylic,y_Acrylic-2*r_Acrylic,z_Acrylic-1]);
                cylinder(r=r_Acrylic,h=1,$fn=Smoothness);
            }
        }
        translate([xpos1_M3,ypos1_M3,-hex_bottom-z_Acrylic-tol])cylinder(r=r_M3,h=z_Acrylic+2*tol,$fn=Smoothness);
        translate([xpos2_M3,ypos1_M3,-hex_bottom-z_Acrylic-tol])cylinder(r=r_M3,h=z_Acrylic+2*tol,$fn=Smoothness);
        translate([xpos1_M3,ypos2_M3,-hex_bottom-z_Acrylic-tol])cylinder(r=r_M3,h=z_Acrylic+2*tol,$fn=Smoothness);
        translate([xpos2_M3,ypos2_M3,-hex_bottom-z_Acrylic-tol])cylinder(r=r_M3,h=z_Acrylic+2*tol,$fn=Smoothness);
        for (i = [0:2:9]){
            translate([x_AcrylicFront+x2margin_AcrylicSide-tol,-y1margin_AcrylicSide-Acrylic_Wall+(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide+2*Acrylic_Wall)*(i+1)/11-tol,-2*Acrylic_Wall-hex_bottom-tol])cube([Acrylic_Wall+2*tol,(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide)/11+2*tol,2*Acrylic_Wall+tol]);
            translate([-x1margin_AcrylicSide-x_AcrylicSide-tol,-y1margin_AcrylicSide-Acrylic_Wall+(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide+2*Acrylic_Wall)*(i+1)/11-tol,-2*Acrylic_Wall-hex_bottom-tol])cube([Acrylic_Wall+2*tol,(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide)/11+2*tol,2*Acrylic_Wall+tol]);
            translate([-x1margin_AcrylicFront+(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)*(i+1)/11-tol,y_PCB+y2margin_AcrylicFront-tol,-2*Acrylic_Wall-hex_bottom-tol])cube([(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)/9+2*tol,Acrylic_Wall+2*tol,2*Acrylic_Wall+tol]);
           translate([-x1margin_AcrylicFront+(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)*(i+1)/11-tol,-y1margin_AcrylicFront-y_AcrylicFront-tol,-2*Acrylic_Wall-hex_bottom-tol])cube([(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)/10+2*tol,Acrylic_Wall+2*tol,2*Acrylic_Wall+tol]);
        } 
        
    }
}
module Acrylic_Top(){
    //color([0,1,0])difference(){
    color([0,0,0.8,transparent])difference(){
        translate([-xmargin_Acrylic+r_Acrylic,-ymargin_Acrylic+r_Acrylic,z_PCB+hex_middle]){
            minkowski(){
                cube([x_Acrylic-2*r_Acrylic,y_Acrylic-2*r_Acrylic,z_Acrylic-1]);
                cylinder(r=r_Acrylic,h=1,$fn=Smoothness);
            }
        }
        translate([xpos1_M3,ypos1_M3,z_PCB+hex_middle+z_PCB+hex_top-tol])cylinder(r=r_M3,h=z_Acrylic+2*tol,$fn=Smoothness);
        translate([xpos2_M3,ypos1_M3,z_PCB+hex_middle+z_PCB+hex_top-tol])cylinder(r=r_M3,h=z_Acrylic+2*tol,$fn=Smoothness);
        translate([xpos1_M3,ypos2_M3,z_PCB+hex_middle+z_PCB+hex_top-tol])cylinder(r=r_M3,h=z_Acrylic+2*tol,$fn=Smoothness);
        translate([xpos2_M3,ypos2_M3,z_PCB+hex_middle+z_PCB+hex_top-tol])cylinder(r=r_M3,h=z_Acrylic+2*tol,$fn=Smoothness);
        for (i = [0:2:9]){            
            translate([x_AcrylicFront+x2margin_AcrylicSide-tol,-y1margin_AcrylicSide-Acrylic_Wall+(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide+2*Acrylic_Wall)*(i+1)/11-tol,z_AcrylicFront-hex_bottom])cube([Acrylic_Wall+2*tol,(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide)/11+2*tol,2*Acrylic_Wall+tol]);
            translate([-x1margin_AcrylicSide-x_AcrylicSide-tol,-y1margin_AcrylicSide-Acrylic_Wall+(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide+2*Acrylic_Wall)*(i+1)/11-tol,z_AcrylicFront-hex_bottom])cube([Acrylic_Wall+2*tol,(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide)/11+2*tol,2*Acrylic_Wall+tol]);
            translate([-x1margin_AcrylicFront+(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)*(i+1)/11-tol,y_PCB+y2margin_AcrylicFront-tol,z_AcrylicFront-hex_bottom])cube([(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)/9+2*tol,Acrylic_Wall+2*tol,2*Acrylic_Wall+tol]);
            translate([-x1margin_AcrylicFront+(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)*(i+1)/11-tol,-y1margin_AcrylicFront-y_AcrylicFront-tol,z_AcrylicFront-hex_bottom])cube([(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)/10+2*tol,Acrylic_Wall+2*tol,2*Acrylic_Wall+tol]);
        }
    }
}
module Acrylic_Front(){
    color([0,0,0.8,transparent]){
    //color([1,0,0]){
        difference(){
            translate([-x1margin_AcrylicFront,-y1margin_AcrylicFront-y_AcrylicFront,-hex_bottom])cube([x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront,y_AcrylicFront,z_AcrylicFront]);
            translate([xpos_Switch_1,ypos_Switch,0])Switch();
            translate([xpos_Switch_2,ypos_Switch,0])Switch();
            NeoPixelHole();
            for (i = [0:2:6]){
                translate([-x1margin_AcrylicFront-tol,-y1margin_AcrylicFront-Acrylic_Wall-tol,-hex_bottom+z_AcrylicSide*(i+1)/6])cube([Acrylic_Wall+2*tol,Acrylic_Wall+2*tol,z_AcrylicSide/6]);
                translate([x_AcrylicFront+x2margin_AcrylicFront-Acrylic_Wall-tol,-y1margin_AcrylicFront-Acrylic_Wall-tol,-hex_bottom+z_AcrylicSide*(i+1)/6])cube([Acrylic_Wall+2*tol,Acrylic_Wall+2*tol,z_AcrylicSide/6]);
            }
            translate([x2pos_SUBD,y_PCB-y2pos_SUBD,0])SUBD25();
        }
        for (i = [0:2:9]){
            translate([-x1margin_AcrylicFront+(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)*(i+1)/11,-y1margin_AcrylicFront-y_AcrylicFront,-Acrylic_Wall-hex_bottom])cube([(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)/10,Acrylic_Wall,Acrylic_Wall]);
            translate([-x1margin_AcrylicFront+(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)*(i+1)/11,-y1margin_AcrylicFront-y_AcrylicFront,z_AcrylicFront-hex_bottom])cube([(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)/10,Acrylic_Wall,Acrylic_Wall]);
        }
    }
}
module Acrylic_Back(){
    color([0,0,0.8,transparent]){
    //color([1,0,0]){
        difference(){
            translate([-x1margin_AcrylicFront,y_PCB+y2margin_AcrylicFront,-hex_bottom])cube([x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront,y_AcrylicFront,z_AcrylicFront]);
            for (i = [0:2:6]){
                translate([-x1margin_AcrylicFront-tol,y_PCB+y2margin_AcrylicFront-tol,-hex_bottom+z_AcrylicSide*(i+1)/6])cube([Acrylic_Wall+2*tol,Acrylic_Wall+2*tol,z_AcrylicSide/6]);
                translate([x_AcrylicFront+x2margin_AcrylicFront-Acrylic_Wall-tol,y_PCB+y2margin_AcrylicFront-tol,-hex_bottom+z_AcrylicSide*(i+1)/6])cube([Acrylic_Wall+2*tol,Acrylic_Wall+2*tol,z_AcrylicSide/6]);
            }
            translate([x2pos_SUBD+11*2.77,y_PCB-y22pos_SUBD,0])rotate([0,0,180])SUBD25();
        }
        for (i = [0:2:9]){
            translate([-x1margin_AcrylicFront+(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)*(i+1)/11,y_PCB+y2margin_AcrylicFront,-Acrylic_Wall-hex_bottom])cube([(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)/9,Acrylic_Wall,Acrylic_Wall]);
            translate([-x1margin_AcrylicFront+(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)*(i+1)/11,y_PCB+y2margin_AcrylicFront,z_AcrylicFront-hex_bottom])cube([(x_AcrylicFront+x1margin_AcrylicFront+x2margin_AcrylicFront)/9,Acrylic_Wall,Acrylic_Wall]);
        }
    }
}
module Acrylic_Left(){
    color([0,0,0.8,transparent]){
    //color([0,0,1]){
        difference(){
            translate([-x1margin_AcrylicSide-x_AcrylicSide,-y1margin_AcrylicSide,-hex_bottom])cube([x_AcrylicSide,y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide,z_AcrylicSide]);
            translate([xpos_BNC90,ypos_BNC90_1,0])BNC90();
            translate([xpos_BNC90,ypos_BNC90_2,0])BNC90();
            ESP();
        }
        difference(){
            translate([-x1margin_AcrylicSide-x_AcrylicSide,-y1margin_AcrylicSide-Acrylic_Wall,-hex_bottom])cube([Acrylic_Wall,Acrylic_Wall,z_AcrylicSide]);
            for (i = [0:2:6]){
                translate([-x1margin_AcrylicSide-x_AcrylicSide-tol,-y1margin_AcrylicSide-Acrylic_Wall-tol,z_AcrylicSide*i/6-hex_bottom-tol])cube([Acrylic_Wall+2*tol,Acrylic_Wall+2*tol,z_AcrylicSide/6+2*tol]);
            }
        }
        difference(){
            translate([-x1margin_AcrylicSide-x_AcrylicSide,y_AcrylicSide+y1margin_AcrylicSide,-hex_bottom])cube([Acrylic_Wall,Acrylic_Wall,z_AcrylicSide]);
            for (i = [0:2:6]){
                translate([-x1margin_AcrylicSide-x_AcrylicSide-tol,y_AcrylicSide+y1margin_AcrylicSide-tol,z_AcrylicSide*i/6-hex_bottom-tol])cube([Acrylic_Wall+2*tol,Acrylic_Wall+2*tol,z_AcrylicSide/6+2*tol]);
            }
        }
        for (i = [0:2:9]){
            translate([-x1margin_AcrylicSide-x_AcrylicSide,-y1margin_AcrylicSide-Acrylic_Wall+(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide+2*Acrylic_Wall)*(i+1)/11,-Acrylic_Wall-hex_bottom])cube([Acrylic_Wall,(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide)/11,Acrylic_Wall]);
            translate([-x1margin_AcrylicSide-x_AcrylicSide,-y1margin_AcrylicSide-Acrylic_Wall+(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide+2*Acrylic_Wall)*(i+1)/11,z_AcrylicFront-hex_bottom])cube([Acrylic_Wall,(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide)/11,Acrylic_Wall]);
        }
    }
}
module Acrylic_Right(){
    color([0,0,0.8,transparent]){
    //color([0,0,1]){
        difference(){
            translate([x_PCB+x2margin_AcrylicSide,-y1margin_AcrylicSide,-hex_bottom])cube([x_AcrylicSide,y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide,z_AcrylicSide]);
            }
        difference(){
            translate([x_AcrylicFront+x2margin_AcrylicSide,-y1margin_AcrylicSide-Acrylic_Wall,-hex_bottom])cube([Acrylic_Wall,Acrylic_Wall,z_AcrylicSide]);
            for (i = [0:2:6]){
                translate([x_AcrylicFront+x2margin_AcrylicSide-tol,-y1margin_AcrylicSide-Acrylic_Wall-tol,z_AcrylicSide*i/6-hex_bottom-tol])cube([Acrylic_Wall+2*tol,Acrylic_Wall+2*tol,z_AcrylicSide/6+2*tol]);
            }
        }
        difference(){
            translate([x_AcrylicFront+x2margin_AcrylicSide,y_AcrylicSide+y1margin_AcrylicSide,-hex_bottom])cube([Acrylic_Wall,Acrylic_Wall,z_AcrylicSide]);
            for (i = [0:2:6]){
                translate([x_AcrylicFront+x2margin_AcrylicSide-tol,y_AcrylicSide+y1margin_AcrylicSide-tol,z_AcrylicSide*i/6-hex_bottom-tol])cube([Acrylic_Wall+2*tol,Acrylic_Wall+2*tol,z_AcrylicSide/6+2*tol]);
            }
        }
        for (i = [0:2:9]){
            translate([x_AcrylicFront+x2margin_AcrylicSide,-y1margin_AcrylicSide-Acrylic_Wall+(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide+2*Acrylic_Wall)*(i+1)/11,-Acrylic_Wall-hex_bottom])cube([Acrylic_Wall,(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide)/11,Acrylic_Wall]);
            translate([x_AcrylicFront+x2margin_AcrylicSide,-y1margin_AcrylicSide-Acrylic_Wall+(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide+2*Acrylic_Wall)*(i+1)/11,z_AcrylicFront-hex_bottom])cube([Acrylic_Wall,(y_AcrylicSide+y1margin_AcrylicSide+y2margin_AcrylicSide)/11,Acrylic_Wall]);
        }
    }
}




module Acrylic_Botom_DXF(){
    projection()Acrylic_Botom();
}
module Acrylic_Top_DXF(){
    projection()Acrylic_Top();
}
module Acrylic_Front_DXF(){
    projection()rotate([-90,0,0])Acrylic_Front();
}
module Acrylic_Back_DXF(){
    projection()rotate([90,0,0])Acrylic_Back();
}
module Acrylic_Left_DXF(){
    projection()rotate([0,-90,0])Acrylic_Left();
}
module Acrylic_Right_DXF(){
    projection()rotate([0,90,0])Acrylic_Right();
}


          


            
        