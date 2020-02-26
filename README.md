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
* Run ```python -i armController.py``` (on local machine)

Be aware of the ip address of the pi and change that in the class "Swift" in the file ```swiftController.py```

### Commands
The ```armController.py``` creates an "arm" object that contains all functions to send command over tcp to the rpi. THe folowing commands can be used to move the arm after ```python -i armController.py``` is run.
```
arm.moveToPos(x,y,z,e)

arm.moveXToPos(pos)
arm.moveYToPos(pos)
arm.moveZToPos(pos)
arm.moveEToPos(pos)

amr.moveXYZRel(dx,dy,dz,de)

arm.moveXRel(dist)
arm.moveYRel(dist)
arm.moveZRel(dist)
arm.moveERel(dist)
```

## Swift Pro Firmware (Base on Marlin https://www.marlinfw.org/)

<img align="top" width=175 src="buildroot/share/pixmaps/logo/SwiftPro.png" />

### Document & Support

Visit http://www.ufactory.cc/#/en/support/ for more details.

### License

Swift Pro Firmware is published under the [GPL license](/LICENSE) 
