# Swift Pro Firmware V4.1.0 (Base on [Grbl v0.9j](https://github.com/grbl/grbl) )

----------

## Update Summary for v4.1.0
* Transplant Grbl framework.
* Optimize stepper motor performance.
* Fix servo shake in end-effector.

## Features
* **not support study mode temporarily**.
* **not support app control temporarily**.
### For serial terminal control

First, connect to uArm using the serial terminal of your choice.Set the baud rate to 115200 as 8-N-1 (8-bits, no parity, and 1-stop bit.) .Cmd list reference to [protocol documents](doc/).

* move cmd support **G0,G1,G2004,G2201,G2202,G2204,G2205**.
* setting cmd support **M17,M204,M2019,M2120,M2121,M2122,M2201,M2202,M2203,M2210,M2215,M2220,M2221,M2222,M2231,M2232,M2233,M2400,M2401,M2410,M2411**.                                                                                                                                                                           
not support temporarily **M2211,M2212,M2213,M2234,M2240,M2241,M2245**.
* query cmd support 
**P2200,P2201,P2202,P2203,P2204,P2205,P2206,P2220,P2221,P2231,P2231,P2232,P2233,P2234,P2242,P2400**.                                                                  
not support temporarily **P2240,P2241**.

### For uArmStudio control

- BLOCKLY is not support **input** and **Grove** module temporarily.
- Draw/Laser is not support temporarily.
- 3D Printing is not support temporarily.

 
----------

### 1、Flashing Firmware to uArm
#### To Determine your uArm's COM port:

* Windows XP: Right click on "My Computer", select "Properties", select "Device Manager".
* Windows 7: Click "Start" -> Right click "Computer" -> Select "Manage" -> Select "Device Manager" from left pane.
* In the tree, expand "Ports (COM & LPT)".
* Your uArm will be the **Arduino Mega 2560 (COMX)**, where the “X” represents the COM number, for example COM6.
* If there are multiple USB serial ports, right click each one and check the manufacturer, the Arduino will be "FTDI".
#### To flash  hex to Swift Pro:

* Download the [hex](hex/)
* Download and extract [XLoader](http://xloader.russemotto.com/XLoader.zip).
* Open XLoader and select your uArm's COM port from the drop down menu on the lower left.
* Select the appropriate device from the dropdown list titled "Device".
* Check that Xloader set the correct baud rate for the device: 115200 for Mega (ATMEGA2560).
* Now use the browse button on the top right of the form to browse to your grbl hex file.
* Once your hex file is selected, click "Upload"
The upload process generally takes about 10 seconds to finish. Once completed, a message will appear in the bottom left corner of XLoader telling you how many bytes were uploaded. If there was an error, it would show instead of the total bytes uploaded. Steps should be similar and may be done through the command prompt.

### 2、Control your uArm
you have three ways to control your uArm:

* using the serial terminal
* using the Python library
* using the uArmStudio



## License

Swift Pro Firmware is published under the [GPL license](/LICENSE) 







