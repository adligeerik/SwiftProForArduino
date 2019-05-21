# Linear Movement for uArm
This repo is forked from ufactory and has been modified so that the arm will move linear on aluminum tracks. The firmware has been changed to use the extruder motor as the 4th axis. Use the ```develop``` branch.

## Hardware used

* uArm Swift
* Raspberry Pi 
* Printed parts
* Aluminium profiles
* Tripods
* LiPo battery
* DCDC converter
* Opto endstops
* Bearings (4pc 19mmØ, 3pc 22mmØ)

### Raspberry Pi
The Paspberry Pi runs [DietPi](https://dietpi.com). The RPi recives messages on port 8002 and forwards them to a USB port with socat. The following command is exacuted on startup on the RPi:

```bash
socat tcp-listen:8002,reuseaddr,fork /dev/ttyACM0,b115200,raw,echo=0,crnl
```

## How to use
* Install necessary firmware on RPi 
* Flash uArm with the Marlin.ino firmware
* Run ```python -i armController.py```

## Swift Pro Firmware (Base on Marlin https://www.marlinfw.org/)

<img align="top" width=175 src="buildroot/share/pixmaps/logo/SwiftPro.png" />

### Document & Support

Visit http://www.ufactory.cc/#/en/support/ for more details.

### License

Swift Pro Firmware is published under the [GPL license](/LICENSE) 
